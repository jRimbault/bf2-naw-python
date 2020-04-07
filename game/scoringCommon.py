# common scoring

import host
import bf2

import game.common
import game.players
from game.stats import constants

SCORE_KILL = 2
SCORE_TEAMKILL = -4
SCORE_SUICIDE = -1
SCORE_REVIVE = 2
SCORE_TEAMDAMAGE = 0
SCORE_TEAMVEHICLEDAMAGE = 0
SCORE_DESTROYREMOTECONTROLLED = 1

SCORE_KILLASSIST_DRIVER = 1
SCORE_KILLASSIST_PASSENGER = 0
SCORE_KILLASSIST_TARGETER = 1
SCORE_KILLASSIST_DAMAGE = 1

REPAIR_POINT_LIMIT = 100
HEAL_POINT_LIMIT = 100
GIVEAMMO_POINT_LIMIT = 100
TEAMDAMAGE_POINT_LIMIT = 50
TEAMVEHICLEDAMAGE_POINT_LIMIT = 50

REPLENISH_POINT_MIN_INTERVAL = 30  # seconds

# sub score
NORMAL = 0
SKILL = 1
RPL = 2
CMND = 3


def init():
    game.players.init()
    # set limits for how many repair HPs etc are needed to get a callback
    bf2.gameLogic.setHealPointLimit(HEAL_POINT_LIMIT)
    bf2.gameLogic.setRepairPointLimit(REPAIR_POINT_LIMIT)
    bf2.gameLogic.setGiveAmmoPointLimit(GIVEAMMO_POINT_LIMIT)
    bf2.gameLogic.setTeamDamagePointLimit(TEAMDAMAGE_POINT_LIMIT)
    bf2.gameLogic.setTeamVehicleDamagePointLimit(TEAMVEHICLEDAMAGE_POINT_LIMIT)

    host.registerGameStatusHandler(onGameStatusChanged)

    if bf2.g_debug:
        print "scoring common init"


def onGameStatusChanged(status):
    if status == bf2.GameStatus.Playing:
        host.registerHandler("PlayerKilled", onPlayerKilled)
        host.registerHandler("PlayerDeath", onPlayerDeath)
        host.registerHandler("PlayerRevived", onPlayerRevived)
        host.registerHandler("PlayerHealPoint", onPlayerHealPoint)
        host.registerHandler("PlayerRepairPoint", onPlayerRepairPoint)
        host.registerHandler("PlayerGiveAmmoPoint", onPlayerGiveAmmoPoint)
        host.registerHandler("PlayerTeamDamagePoint", onPlayerTeamDamagePoint)
        host.registerHandler("VehicleDestroyed", onVehicleDestroyed)

    elif status == bf2.GameStatus.EndGame:

        giveCommanderEndScore(
            bf2.playerManager.getCommander(1), bf2.gameLogic.getWinner()
        )
        giveCommanderEndScore(
            bf2.playerManager.getCommander(2), bf2.gameLogic.getWinner()
        )


# give commander score for every player score
def addScore(player, points, subScore=NORMAL, subPoints=-1):

    # commander doesnt get score for regular actions, only for pure commander tasks. he also gets punishing points.
    if not player.isCommander() or subScore == CMND or points < 0:
        player.score.score += points
        if subPoints == -1:
            subPoints = points

        # sub score
        if subScore == RPL:
            player.score.rplScore += subPoints
        if subScore == SKILL:
            player.score.skillScore += subPoints
        if subScore == CMND:
            player.score.cmdScore += subPoints

    # commander score
    commander = bf2.playerManager.getCommander(player.getTeam())
    if (
        commander != None
        and commander.isValid()
        and subScore != CMND
        and player != commander
        and points > 0
    ):
        preScore = commander.score.score
        numPlayers = bf2.playerManager.getNumberOfAlivePlayersInTeam(
            commander.getTeam()
        )
        if numPlayers > 0:
            commander.score.score += float(points) / numPlayers
            scoreGotten = commander.score.score - preScore
            if scoreGotten > 0:
                commander.score.cmdScore += scoreGotten


def giveCommanderEndScore(player, winningTeam):
    if player == None:
        return
    if player.getTeam() != winningTeam:
        return

    # double the commander score and add to regular score
    player.score.score = (
        player.score.score + player.score.fracScore - player.score.cmdScore
    ) + player.score.cmdScore * 2
    player.score.cmdScore = player.score.cmdScore * 2


def onPlayerKilled(victim, attacker, weapon, assists, object):

    killedByEmptyVehicle = False
    countAssists = False

    # killed by unknown, no score
    if attacker == None:

        # check if killed by vehicle in motion
        if weapon == None and object != None:
            if hasattr(object, "lastDrivingPlayerIndex"):
                attacker = bf2.playerManager.getPlayerByIndex(
                    object.lastDrivingPlayerIndex
                )
                killedByEmptyVehicle = True

        if attacker == None and bf2.g_debug:
            print "No attacker found"

    victimVehicle = victim.getVehicle()

    # killed by remote controlled vehicle, no score awarded in this game
    if object and object.isPlayerControlObject and object.getIsRemoteControlled():
        pass

    # no attacker, killed by object
    elif attacker == None:
        pass

    # killed by self
    elif attacker == victim:

        # no suicides from own wreck
        if killedByEmptyVehicle and object.getIsWreck():
            return

        attacker.score.suicides += 1
        addScore(attacker, SCORE_SUICIDE, RPL)

    # killed by own team
    elif attacker.getTeam() == victim.getTeam():

        # no teamkills from wrecks
        if object != None and object.getIsWreck():
            return

        # no teamkills from artillery
        if weapon:
            attackerVehicle = bf2.objectManager.getRootParent(weapon)
            if (
                attackerVehicle.isPlayerControlObject
                and attackerVehicle.getIsRemoteControlled()
            ):
                return

        attacker.score.TKs += 1
        addScore(attacker, SCORE_TEAMKILL, RPL)

        countAssists = True

    # killed by enemy
    else:
        attacker.score.kills += 1
        addScore(attacker, SCORE_KILL, SKILL)

        countAssists = True

        # headshot/range/speed message
        bf2.Timer(delayedPlayerKilled, 0.1, 1, createData(victim, attacker, weapon))

    # kill assist
    if countAssists and victim:

        for a in assists:
            assister = a[0]
            assistType = a[1]

            if assister.getTeam() != victim.getTeam():

                # passenger
                if assistType == 0:
                    assister.score.passengerAssists += 1
                    addScore(assister, SCORE_KILLASSIST_PASSENGER, RPL)
                # targeter
                elif assistType == 1:
                    assister.score.targetAssists += 1
                    addScore(assister, SCORE_KILLASSIST_TARGETER, RPL)
                # damage
                elif assistType == 2:
                    assister.score.damageAssists += 1
                    addScore(assister, SCORE_KILLASSIST_DAMAGE, RPL)
                # driver passenger
                elif assistType == 3:
                    assister.score.driverAssists += 1
                    addScore(assister, SCORE_KILLASSIST_DRIVER, RPL)
                else:
                    # unknown kill type
                    pass


def onPlayerDeath(victim, vehicle):
    victim.score.deaths += 1


def onPlayerRevived(victim, attacker):
    if attacker == None or victim == None or attacker.getTeam() != victim.getTeam():
        return

    attacker.score.revives += 1
    addScore(attacker, SCORE_REVIVE, RPL)

    bf2.gameLogic.sendGameEvent(attacker, 10, 4)  # 10 = Replenish, 4 = Revive


# prevent point-exploiting by replenishing same player again
def checkGrindBlock(player, object):

    if object.isPlayerControlObject:
        defPlayers = object.getOccupyingPlayers()
        if len(defPlayers) > 0:
            defPlayer = defPlayers[0]

            if not hasattr(player, "lastReplenishPointMap"):
                player.lastReplenishPointMap = {}
            else:
                if defPlayer.index in player.lastReplenishPointMap:
                    if (
                        player.lastReplenishPointMap[defPlayer.index]
                        + REPLENISH_POINT_MIN_INTERVAL
                        > host.timer_getWallTime()
                    ):
                        return True

            player.lastReplenishPointMap[defPlayer.index] = host.timer_getWallTime()

    return False


def onPlayerHealPoint(player, object):
    if checkGrindBlock(player, object):
        return

    player.score.heals += 1
    addScore(player, 1, RPL)
    bf2.gameLogic.sendGameEvent(player, 10, 0)  # 10 = Replenish, 0 = Heal

    giveDriverSpecialPoint(player)


def onPlayerRepairPoint(player, object):
    if checkGrindBlock(player, object):
        return

    player.score.repairs += 1
    addScore(player, 1, RPL)
    bf2.gameLogic.sendGameEvent(player, 10, 1)  # 10 = Replenish, 1 = Repair

    giveDriverSpecialPoint(player)


def onPlayerGiveAmmoPoint(player, object):
    if checkGrindBlock(player, object):
        return

    player.score.ammos += 1
    addScore(player, 1, RPL)
    bf2.gameLogic.sendGameEvent(player, 10, 2)  # 10 = Replenish, 2 = Ammo

    giveDriverSpecialPoint(player)


def giveDriverSpecialPoint(player):

    # special point given to driver, if someone in vehicle gets an abilitypoint
    vehicle = player.getVehicle()
    if vehicle:
        rootVehicle = bf2.objectManager.getRootParent(vehicle)
        driver = rootVehicle.getOccupyingPlayers()[0]

        if driver != None and driver != player and driver.getVehicle() == rootVehicle:
            driver.score.driverSpecials += 1
            addScore(driver, 1, RPL)
            bf2.gameLogic.sendGameEvent(
                driver, 10, 3
            )  # 10 = Replenish, 3 = DriverAbility


def onPlayerTeamDamagePoint(player, object):
    vehicleType = constants.getVehicleType(object.templateName)

    if not player.isCommander():
        if vehicleType == constants.VEHICLE_TYPE_SOLDIER:
            player.score.teamDamages += 1
            addScore(player, SCORE_TEAMDAMAGE, RPL)
        else:
            player.score.teamVehicleDamages += 1
            addScore(player, SCORE_TEAMVEHICLEDAMAGE, RPL)


# prevent point-exploiting by replenishing same player again
def checkGrindBlockRemote(player, object):

    if not hasattr(player, "lastDestroyedRemote"):
        player.lastDestroyedRemote = {}
    else:
        if object in player.lastDestroyedRemote:
            if (
                player.lastDestroyedRemote[object] + REPLENISH_POINT_MIN_INTERVAL
                > host.timer_getWallTime()
            ):
                return True

    player.lastDestroyedRemote[object] = host.timer_getWallTime()
    return False


def onVehicleDestroyed(vehicle, attacker):
    if (
        attacker != None
        and vehicle.getTeam() != 0
        and vehicle.getTeam() != attacker.getTeam()
        and vehicle.getIsRemoteControlled()
    ):
        if not checkGrindBlockRemote(attacker, vehicle):
            addScore(attacker, SCORE_DESTROYREMOTECONTROLLED, RPL)
            bf2.gameLogic.sendGameEvent(
                attacker, 10, 5
            )  # 10 = Replenish, 5 = DestroyStrategic


# to display distance when sniping


def createData(victim, attacker, weapon):
    try:
        # attacker data
        if attacker != None:
            attackerName = attacker.getName()
            attackerPosition = game.players.getPosition(attacker)
        else:
            attackerName = None
            attackerPosition = None

        # victim data
        if victim != None:
            victimName = victim.getName()
            victimPosition = game.players.getPosition(victim)
            victimSpeed = game.players.getSpeed(victim)
        else:
            victimName = None
            victimPosition = None
            victimSpeed = None

        return {
            "attacker": {
                "actor": attacker,
                "name": attackerName,
                "position": attackerPosition,
            },
            "victim": {
                "actor": victim,
                "name": victimName,
                "position": victimPosition,
                "speed": victimSpeed,
            },
            "weapon": weapon,
        }
    except:
        game.common.printException()

    return {}


# takes the data bundle made by `createData` as input
def delayedPlayerKilled(data):
    try:
        if not isSniperRifle(data["weapon"]):
            return

        attacker = data["attacker"]
        victim = data["victim"]

        hitRegionText = getHitRegion(victim["actor"])
        speedText = getSpeedDescription(victim["speed"])
        killDistance = getKillDistance(attacker["position"], victim["position"])

        game.common.sayAll(
            " ".join(
                [
                    attacker["name"],
                    "got a",
                    str(int(killDistance)),
                    "m",
                    hitRegionText,
                    "on a",
                    speedText,
                    "target",
                ]
            )
        )
    except:
        game.common.printException()


def getSpeedDescription(speed):
    if speed != None:
        if speed > 6:
            return "running"
        elif speed > 3:
            return "walking"
        elif speed > 0.5:
            return "semi-stationary"

    return "stationary"


def isSniperRifle(weapon):
    return (
        weapon is not None
        and constants.getWeaponType(weapon.templateName) == constants.WEAPON_TYPE_SNIPER
    )


def getHitRegion(victim):
    if victim is not None and victim.isManDown() == 0:
        return "headshot"
    return "bodyshot"


def getKillDistance(attackerPosition, victimPosition):
    if attackerPosition != None and victimPosition != None:
        return game.common.vectordistance(attackerPosition, victimPosition)
    return 1
