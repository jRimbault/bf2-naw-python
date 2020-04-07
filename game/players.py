# -*- coding: iso-8859-15 -*-
# wookie sniper mod players script by Scouty (14-03-2008)
# provides player position/rotation/speed functions
# modified and included for the AIX mod custom scoring

import bf2
import host

import game.common

speedtimer = None

SPEEDTIMER_INTERVAL = 0.5


def init():
    host.registerGameStatusHandler(gameStatus)


def gameStatus(status):
    global speedtimer
    if status == bf2.GameStatus.Playing:
        try:
            speedtimer.destroy()
        except:
            pass
        speedtimer = None
        speedtimer = bf2.Timer(speedCalculation, SPEEDTIMER_INTERVAL, 1)
        speedtimer.setRecurring(SPEEDTIMER_INTERVAL)

    if status == bf2.GameStatus.EndGame:
        try:
            speedtimer.destroy()
        except:
            pass
        speedtimer = None


def speedCalculation(data):
    try:
        for player in bf2.playerManager.getPlayers():
            curpos = getPosition(player)

            if not hasattr(player, "oldpos"):
                player.oldpos = curpos

            player.speed = (
                game.common.vectordistance(curpos, player.oldpos) / SPEEDTIMER_INTERVAL
            )
            player.oldpos = curpos
    except:
        game.common.printException()


def getSpeed(player):
    if hasattr(player, "speed"):
        return player.speed
    else:
        return 0


def getPosition(player):
    vehicle = player.getVehicle()
    if vehicle != None:
        return vehicle.getPosition()
    elif hasattr(player, "oldpos"):
        return player.oldpos
    else:
        return [-5000.0, -5000.0, -5000.0]


def getrotation(player):
    vehicle = player.getVehicle()
    if vehicle != None:
        return vehicle.getRotation()
    else:
        return [0.0, 0.0, 0.0]


def getname(player):
    parts = player.getName().split(" ")
    if len(parts) == 1:
        name = parts[0]
    elif len(parts) == 2:
        name = parts[1]
    else:
        name = ""

    return name


def gettag(player):
    parts = player.getName().split(" ")
    if len(parts) == 2:
        tag = parts[0]
    else:
        tag = ""

    return tag
