# stats keys

import host
import string
from bf2 import g_debug


VEHICLE_TYPE_ARMOR = 0
VEHICLE_TYPE_AVIATOR = 1
VEHICLE_TYPE_AIRDEFENSE = 2
VEHICLE_TYPE_HELICOPTER = 3
VEHICLE_TYPE_TRANSPORT = 4
VEHICLE_TYPE_ARTILLERY = 5
VEHICLE_TYPE_GRNDDEFENSE = 6

VEHICLE_TYPE_PARACHUTE = 7
VEHICLE_TYPE_SOLDIER = 8

VEHICLE_TYPE_NIGHTVISION = 9
VEHICLE_TYPE_GASMASK = 10

NUM_VEHICLE_TYPES = 11
VEHICLE_TYPE_UNKNOWN = NUM_VEHICLE_TYPES


WEAPON_TYPE_ASSAULT = 0
WEAPON_TYPE_ASSAULTGRN = 1
WEAPON_TYPE_CARBINE = 2
WEAPON_TYPE_LMG = 3
WEAPON_TYPE_SNIPER = 4
WEAPON_TYPE_PISTOL = 5
WEAPON_TYPE_ATAA = 6
WEAPON_TYPE_SMG = 7
WEAPON_TYPE_SHOTGUN = 8

WEAPON_TYPE_KNIFE = 10
WEAPON_TYPE_C4 = 11
WEAPON_TYPE_CLAYMORE = 12
WEAPON_TYPE_HANDGRENADE = 13
WEAPON_TYPE_SHOCKPAD = 14
WEAPON_TYPE_ATMINE = 15
WEAPON_TYPE_TARGETING = 16

WEAPON_TYPE_GRAPPLINGHOOK = 17
WEAPON_TYPE_ZIPLINE = 18

WEAPON_TYPE_TACTICAL = 19

NUM_WEAPON_TYPES = 20
WEAPON_TYPE_UNKNOWN = NUM_WEAPON_TYPES


KIT_TYPE_AT = 0
KIT_TYPE_ASSAULT = 1
KIT_TYPE_ENGINEER = 2
KIT_TYPE_MEDIC = 3
KIT_TYPE_SPECOPS = 4
KIT_TYPE_SUPPORT = 5
KIT_TYPE_SNIPER = 6

NUM_KIT_TYPES = 7
KIT_TYPE_UNKNOWN = NUM_KIT_TYPES


ARMY_USA = 0
ARMY_MEC = 1
ARMY_CHINESE = 2
ARMY_SEALS = 3
ARMY_SAS = 4
ARMY_SPETZNAS = 5
ARMY_MECSF = 6
ARMY_REBELS = 7
ARMY_INSURGENTS = 8
ARMY_EURO = 9
ARMY_GER = 10
ARMY_UKR = 11

NUM_ARMIES = 12
ARMY_UNKNOWN = NUM_ARMIES


vehicleTypeMap = {
    "usapc_lav25": VEHICLE_TYPE_ARMOR,
    "apc_btr90": VEHICLE_TYPE_ARMOR,
    "apc_wz551": VEHICLE_TYPE_ARMOR,
    "ustnk_m1a2": VEHICLE_TYPE_ARMOR,
    "rutnk_t90": VEHICLE_TYPE_ARMOR,
    "tnk_type98": VEHICLE_TYPE_ARMOR,
    "usair_f18": VEHICLE_TYPE_AVIATOR,
    "ruair_mig29": VEHICLE_TYPE_AVIATOR,
    "air_j10": VEHICLE_TYPE_AVIATOR,
    "usair_f15": VEHICLE_TYPE_AVIATOR,
    "ruair_su34": VEHICLE_TYPE_AVIATOR,
    "air_su30mkk": VEHICLE_TYPE_AVIATOR,
    "air_f35b": VEHICLE_TYPE_AVIATOR,
    "usaav_m6": VEHICLE_TYPE_AIRDEFENSE,
    "aav_tunguska": VEHICLE_TYPE_AIRDEFENSE,
    "aav_type95": VEHICLE_TYPE_AIRDEFENSE,
    "usaas_stinger": VEHICLE_TYPE_AIRDEFENSE,
    "igla_djigit": VEHICLE_TYPE_AIRDEFENSE,
    "wasp_defence_front": VEHICLE_TYPE_AIRDEFENSE,
    "wasp_defence_back": VEHICLE_TYPE_AIRDEFENSE,
    "usthe_uh60": VEHICLE_TYPE_HELICOPTER,
    "the_mi17": VEHICLE_TYPE_HELICOPTER,
    "chthe_z8": VEHICLE_TYPE_HELICOPTER,
    "ahe_ah1z": VEHICLE_TYPE_HELICOPTER,
    "ahe_havoc": VEHICLE_TYPE_HELICOPTER,
    "ahe_z10": VEHICLE_TYPE_HELICOPTER,
    "jeep_faav": VEHICLE_TYPE_TRANSPORT,
    "usjep_hmmwv": VEHICLE_TYPE_TRANSPORT,
    "jep_paratrooper": VEHICLE_TYPE_TRANSPORT,
    "jep_mec_paratrooper": VEHICLE_TYPE_TRANSPORT,
    "jep_vodnik": VEHICLE_TYPE_TRANSPORT,
    "jep_nanjing": VEHICLE_TYPE_TRANSPORT,
    "uslcr_lcac": VEHICLE_TYPE_TRANSPORT,
    "boat_rib": VEHICLE_TYPE_TRANSPORT,
    "usart_lw155": VEHICLE_TYPE_ARTILLERY,
    "ars_d30": VEHICLE_TYPE_ARTILLERY,
    "ats_tow": VEHICLE_TYPE_GRNDDEFENSE,
    "ats_hj8": VEHICLE_TYPE_GRNDDEFENSE,
    "hmg_m2hb": VEHICLE_TYPE_GRNDDEFENSE,
    "chhmg_kord": VEHICLE_TYPE_GRNDDEFENSE,
    "mec_bipod": VEHICLE_TYPE_GRNDDEFENSE,
    "us_bipod": VEHICLE_TYPE_GRNDDEFENSE,
    "ch_bipod": VEHICLE_TYPE_GRNDDEFENSE,
    "us_soldier": VEHICLE_TYPE_SOLDIER,
    "us_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "us_light_soldier": VEHICLE_TYPE_SOLDIER,
    "mec_soldier": VEHICLE_TYPE_SOLDIER,
    "mec_light_soldier": VEHICLE_TYPE_SOLDIER,
    "mec_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "ch_soldier": VEHICLE_TYPE_SOLDIER,
    "ch_light_soldier": VEHICLE_TYPE_SOLDIER,
    "ch_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "parachute": VEHICLE_TYPE_PARACHUTE,
    # xpack1 stuff
    "seal_soldier": VEHICLE_TYPE_SOLDIER,
    "seal_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "sas_soldier": VEHICLE_TYPE_SOLDIER,
    "sas_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "spetz_soldier": VEHICLE_TYPE_SOLDIER,
    "spetz_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "mecsf_soldier": VEHICLE_TYPE_SOLDIER,
    "mecsf_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "chinsurgent_soldier": VEHICLE_TYPE_SOLDIER,
    "chinsurgent_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "meinsurgent_soldier": VEHICLE_TYPE_SOLDIER,
    "meinsurgent_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "xpak_bmp3": VEHICLE_TYPE_ARMOR,
    "xpak_forklift": VEHICLE_TYPE_TRANSPORT,
    "xpak_atv": VEHICLE_TYPE_TRANSPORT,
    "xpak_civ1": VEHICLE_TYPE_TRANSPORT,
    "xpak_civ2": VEHICLE_TYPE_TRANSPORT,
    "xpak_jetski": VEHICLE_TYPE_TRANSPORT,
    "xpak_ailraider": VEHICLE_TYPE_TRANSPORT,
    "xpak_apache": VEHICLE_TYPE_HELICOPTER,
    "xpak_hind": VEHICLE_TYPE_HELICOPTER,
    "xpak_hummertow": VEHICLE_TYPE_TRANSPORT,
    # booster pack 1
    "xpak2_vbl": VEHICLE_TYPE_TRANSPORT,
    "xpak2_tnkl2a6": VEHICLE_TYPE_ARMOR,
    "xpak2_tnkc2": VEHICLE_TYPE_ARMOR,
    "xpak2_tiger": VEHICLE_TYPE_HELICOPTER,
    "xpak2_lynx": VEHICLE_TYPE_HELICOPTER,
    "xpak2_eurofighter": VEHICLE_TYPE_AVIATOR,
    "xpak2_harrier": VEHICLE_TYPE_AVIATOR,
    "eu_soldier": VEHICLE_TYPE_SOLDIER,
    "eu_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    # booster pack 2
    "air_a10": VEHICLE_TYPE_AVIATOR,
    "air_su39": VEHICLE_TYPE_AVIATOR,
    "xpak2_fantan": VEHICLE_TYPE_AVIATOR,
    "che_wz11": VEHICLE_TYPE_HELICOPTER,
    "she_ec635": VEHICLE_TYPE_HELICOPTER,
    "she_littlebird": VEHICLE_TYPE_HELICOPTER,
    "xpak2_musclecar": VEHICLE_TYPE_TRANSPORT,
    "xpak2_semi": VEHICLE_TYPE_TRANSPORT,
    # dcon
    "ah64": VEHICLE_TYPE_HELICOPTER,
    "dcon_ac130": VEHICLE_TYPE_AVIATOR,
    "dcon_ah1z": VEHICLE_TYPE_HELICOPTER,
    "dcon_ah6": VEHICLE_TYPE_HELICOPTER,
    "dcon_mh6": VEHICLE_TYPE_HELICOPTER,
    "dcon_oh6": VEHICLE_TYPE_HELICOPTER,
    "dcon_f15": VEHICLE_TYPE_AVIATOR,
    "dcon_f15a": VEHICLE_TYPE_AVIATOR,
    "dcon_f18": VEHICLE_TYPE_AVIATOR,
    "dcon_f18a": VEHICLE_TYPE_AVIATOR,
    "dcon_f35b": VEHICLE_TYPE_AVIATOR,
    "dcon_havoc": VEHICLE_TYPE_HELICOPTER,
    "dcon_mi17": VEHICLE_TYPE_HELICOPTER,
    "dcon_mig29": VEHICLE_TYPE_AVIATOR,
    "dcon_mig29a": VEHICLE_TYPE_AVIATOR,
    "dcon_su34": VEHICLE_TYPE_AVIATOR,
    "dcon_uh60": VEHICLE_TYPE_HELICOPTER,
    "dcon_uh60l": VEHICLE_TYPE_HELICOPTER,
    "hind": VEHICLE_TYPE_HELICOPTER,
    "mirage": VEHICLE_TYPE_AVIATOR,
    "su25": VEHICLE_TYPE_AVIATOR,
    "usair_a10": VEHICLE_TYPE_AVIATOR,
    "9p117": VEHICLE_TYPE_ARTILLERY,
    "dcon_bm21": VEHICLE_TYPE_ARTILLERY,
    "dcon_bmp2": VEHICLE_TYPE_ARMOR,
    "dcon_brdm2_kpv": VEHICLE_TYPE_TRANSPORT,
    "dcon_btr90": VEHICLE_TYPE_ARMOR,
    "dcon_dpv": VEHICLE_TYPE_TRANSPORT,
    "dcon_hmmwv": VEHICLE_TYPE_TRANSPORT,
    "dcon_hmmwv_medic": VEHICLE_TYPE_TRANSPORT,
    "dcon_hmmwv_minigun": VEHICLE_TYPE_TRANSPORT,
    "dcon_hmmwv_mk19": VEHICLE_TYPE_TRANSPORT,
    "dcon_hmmwv_tow": VEHICLE_TYPE_TRANSPORT,
    "dcon_lav25": VEHICLE_TYPE_ARMOR,
    "dcon_m109": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_1": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_2": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_3": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_4": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_5": VEHICLE_TYPE_ARTILLERY,
    "dcon_m109_6": VEHICLE_TYPE_ARTILLERY,
    "dcon_m1a1": VEHICLE_TYPE_ARMOR,
    "dcon_m2a3": VEHICLE_TYPE_ARMOR,
    "dcon_m6": VEHICLE_TYPE_AIRDEFENSE,
    "dcon_mlrs": VEHICLE_TYPE_ARTILLERY,
    "dcon_paratrooper": VEHICLE_TYPE_TRANSPORT,
    "dcon_semi": VEHICLE_TYPE_TRANSPORT,
    "dcon_semi_a": VEHICLE_TYPE_TRANSPORT,
    "dcon_semi_b": VEHICLE_TYPE_TRANSPORT,
    "dcon_t90": VEHICLE_TYPE_ARMOR,
    "dcon_technical": VEHICLE_TYPE_TRANSPORT,
    "dcon_tunguska": VEHICLE_TYPE_AIRDEFENSE,
    "dcon_vodnik": VEHICLE_TYPE_TRANSPORT,
    "dcon_technical": VEHICLE_TYPE_TRANSPORT,
    "dcon_technicalTOW": VEHICLE_TYPE_TRANSPORT,
    # POE2
    "gerair_ef2000": VEHICLE_TYPE_AVIATOR,
    "gerair_tornado": VEHICLE_TYPE_AVIATOR,
    "gerhe_eurotigerarh": VEHICLE_TYPE_HELICOPTER,
    "gerhe_nh90": VEHICLE_TYPE_TRANSPORT,
    "the_mi17": VEHICLE_TYPE_HELICOPTER,
    "ufo": VEHICLE_TYPE_HELICOPTER,
    "ukrair_mig25": VEHICLE_TYPE_AVIATOR,
    "ukrair_su24": VEHICLE_TYPE_AVIATOR,
    "ukrair_su25": VEHICLE_TYPE_AVIATOR,
    "ukrhe_mi24p": VEHICLE_TYPE_HELICOPTER,
    "civsctr": VEHICLE_TYPE_ARMOR,
    "geraav_gepard": VEHICLE_TYPE_AIRDEFENSE,
    "gerapc_boxerGTK": VEHICLE_TYPE_TRANSPORT,
    "gerapc_marder1a5": VEHICLE_TYPE_ARMOR,
    "gerartil_pzh2000": VEHICLE_TYPE_ARTILLERY,
    "gerjeep_dingo": VEHICLE_TYPE_TRANSPORT,
    "gerjeep_wolf": VEHICLE_TYPE_TRANSPORT,
    "gerjeep_wolfsoft": VEHICLE_TYPE_TRANSPORT,
    "gertnk_leopard": VEHICLE_TYPE_ARMOR,
    "snowmobile": VEHICLE_TYPE_TRANSPORT,
    "ukraav_mtlb_sa13_v2": VEHICLE_TYPE_ARMOR,
    "ukraav_shilka": VEHICLE_TYPE_AIRDEFENSE,
    "ukrapc_bmp2": VEHICLE_TYPE_TRANSPORT,
    "ukrapc_mtlb": VEHICLE_TYPE_TRANSPORT,
    "ukrartil_m1974": VEHICLE_TYPE_ARTILLERY,
    "ukrartil_msta": VEHICLE_TYPE_ARTILLERY,
    "ukrjeep_dozer": VEHICLE_TYPE_TRANSPORT,
    "ukrjeep_uaz": VEHICLE_TYPE_TRANSPORT,
    "ukrtnk_oplot": VEHICLE_TYPE_ARMOR,
    "ukrtnk_t55": VEHICLE_TYPE_ARMOR,
    "ger_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "ger_light_soldier": VEHICLE_TYPE_SOLDIER,
    "ukr_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "ukr_light_soldier": VEHICLE_TYPE_SOLDIER,
    "aa_zu23": VEHICLE_TYPE_GRNDDEFENSE,
    "chhmg_kord": VEHICLE_TYPE_GRNDDEFENSE,
    "gerartil_fh70": VEHICLE_TYPE_GRNDDEFENSE,
    "hmg_m2hb": VEHICLE_TYPE_GRNDDEFENSE,
    "mg3_coax": VEHICLE_TYPE_GRNDDEFENSE,
    "ukrartil_msta": VEHICLE_TYPE_ARTILLERY,
    "remote_kord": VEHICLE_TYPE_GRNDDEFENSE,
    "remote_mg3": VEHICLE_TYPE_GRNDDEFENSE,
    # BF2AUS
    "bf2aus_aslavad": VEHICLE_TYPE_AIRDEFENSE,
    "bf2aus_aslav25": VEHICLE_TYPE_ARMOR,
    "bf2aus_aslav-pc": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_atv4x4": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_atv6x6": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_bushmaster": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_civilian2": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_civilian3": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_f111": VEHICLE_TYPE_AVIATOR,
    "bf2aus_golfcart": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_lrpv": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_m1a1": VEHICLE_TYPE_ARMOR,
    "bf2aus_mrh90": VEHICLE_TYPE_HELICOPTER,
    "bf2aus_technical": VEHICLE_TYPE_TRANSPORT,
    "bf2aus_tiger": VEHICLE_TYPE_HELICOPTER,
    # naw
    "iran_light_soldier": VEHICLE_TYPE_SOLDIER,
    "Iraq_light_soldier": VEHICLE_TYPE_SOLDIER,
    "czh_soldier": VEHICLE_TYPE_SOLDIER,
    "kor_light_soldier": VEHICLE_TYPE_SOLDIER,
    "uk_soldier": VEHICLE_TYPE_SOLDIER,
    "jap_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "nor_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "ch_light_soldier": VEHICLE_TYPE_SOLDIER,
    "ger_soldier": VEHICLE_TYPE_SOLDIER,
    "pak_light_soldier": VEHICLE_TYPE_SOLDIER,
    "den_soldier": VEHICLE_TYPE_SOLDIER,
    "syr_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "can_heavy_soldier": VEHICLE_TYPE_SOLDIER,
    "a10": VEHICLE_TYPE_AVIATOR,
    "a10_ap": VEHICLE_TYPE_AVIATOR,
    "ahe_ah1z": VEHICLE_TYPE_HELICOPTER,
    "ahe_helln": VEHICLE_TYPE_HELICOPTER,
    "ahe_naw": VEHICLE_TYPE_HELICOPTER,
    "air_su30nuk": VEHICLE_TYPE_AVIATOR,
    "ch_medthe": VEHICLE_TYPE_HELICOPTER,
    "f22a": VEHICLE_TYPE_AVIATOR,
    "kaw_oh6": VEHICLE_TYPE_HELICOPTER,
    "kaw_oh6i": VEHICLE_TYPE_HELICOPTER,
    "mh6_so": VEHICLE_TYPE_HELICOPTER,
    "mh6_tr": VEHICLE_TYPE_HELICOPTER,
    "naw_apache": VEHICLE_TYPE_HELICOPTER,
    "rah66a": VEHICLE_TYPE_HELICOPTER,
    "sa342a": VEHICLE_TYPE_HELICOPTER,
    "sa342f": VEHICLE_TYPE_HELICOPTER,
    "su25": VEHICLE_TYPE_AVIATOR,
    "su25sc": VEHICLE_TYPE_AVIATOR,
    "the_mi17a": VEHICLE_TYPE_HELICOPTER,
    "us_medthe": VEHICLE_TYPE_HELICOPTER,
    "usair_f15n": VEHICLE_TYPE_AVIATOR,
    "usthe_uh606": VEHICLE_TYPE_HELICOPTER,
    "civ_buggy": VEHICLE_TYPE_TRANSPORT,
    "civ_charger": VEHICLE_TYPE_TRANSPORT,
    "civ_cobra": VEHICLE_TYPE_TRANSPORT,
    "civ_digger": VEHICLE_TYPE_TRANSPORT,
    "civ_mustang": VEHICLE_TYPE_TRANSPORT,
    "civ_police": VEHICLE_TYPE_TRANSPORT,
    "mil_cruiser": VEHICLE_TYPE_TRANSPORT,
    "reb_defender": VEHICLE_TYPE_TRANSPORT,
    "reb_hotRod": VEHICLE_TYPE_TRANSPORT,
    "reb_van_01": VEHICLE_TYPE_TRANSPORT,
    "truck1": VEHICLE_TYPE_TRANSPORT,
    "aa_technical": VEHICLE_TYPE_AIRDEFENSE,
    "usaav_m163": VEHICLE_TYPE_AIRDEFENSE,
    "dirtbike": VEHICLE_TYPE_TRANSPORT,
    "humvee_aaag": VEHICLE_TYPE_ARTILLERY,
    "jeep_technical": VEHICLE_TYPE_TRANSPORT,
    "iraqtrk_ural4320": VEHICLE_TYPE_TRANSPORT,
    "ustrk_m35": VEHICLE_TYPE_TRANSPORT,
    "m270": VEHICLE_TYPE_ARTILLERY,
    "nanjing_amrpr": VEHICLE_TYPE_TRANSPORT,
    "tos1": VEHICLE_TYPE_ARTILLERY,
    "iraqart_bm21": VEHICLE_TYPE_ARTILLERY,
    "iraqart_2s1": VEHICLE_TYPE_ARTILLERY,
    "usart_m109": VEHICLE_TYPE_ARTILLERY,
    "tow_technical": VEHICLE_TYPE_TRANSPORT,
    "usav_brad": VEHICLE_TYPE_ARMOR,
    "usjep_amrpr": VEHICLE_TYPE_TRANSPORT,
    "zero_quad": VEHICLE_TYPE_TRANSPORT,
    "zero_quad125cc": VEHICLE_TYPE_TRANSPORT,
    "zero_quad250cc": VEHICLE_TYPE_TRANSPORT,
    "apc_cobra": VEHICLE_TYPE_TRANSPORT,
    "challenger": VEHICLE_TYPE_TRANSPORT,
    "baja_bug": VEHICLE_TYPE_TRANSPORT,
    "apc_cobraat": VEHICLE_TYPE_TRANSPORT,
    "ssn_688i": VEHICLE_TYPE_TRANSPORT,
    "lss": VEHICLE_TYPE_TRANSPORT,
    "air_a10": VEHICLE_TYPE_AVIATOR,
    "air_su39": VEHICLE_TYPE_AVIATOR,
    "xpak2_fantan": VEHICLE_TYPE_AVIATOR,
    "che_wz11": VEHICLE_TYPE_HELICOPTER,
    "xpak2_tnkl2a6": VEHICLE_TYPE_ARMOR,
    "xpak2_tnkc2": VEHICLE_TYPE_ARMOR,
    "ustnk_m1a1": VEHICLE_TYPE_ARMOR,
    "xpak2_tiger": VEHICLE_TYPE_HELICOPTER,
    "xpak2_eurofighter": VEHICLE_TYPE_AVIATOR,
    "she_ec635": VEHICLE_TYPE_HELICOPTER,
    "she_littlebird": VEHICLE_TYPE_HELICOPTER,
    "xpak2_musclecar": VEHICLE_TYPE_TRANSPORT,
    "xpak2_semi": VEHICLE_TYPE_TRANSPORT,
    "bkc_interceptor": VEHICLE_TYPE_TRANSPORT,
    "bkc_pursuit": VEHICLE_TYPE_TRANSPORT,
    "bkc_defender": VEHICLE_TYPE_TRANSPORT,
    "chinook": VEHICLE_TYPE_HELICOPTER,
    "chinookassault": VEHICLE_TYPE_HELICOPTER,
    "aix_av8b": VEHICLE_TYPE_AVIATOR,
    "aix_be12": VEHICLE_TYPE_AVIATOR,
    "aix_draken": VEHICLE_TYPE_AVIATOR,
    "aix_f117a": VEHICLE_TYPE_AVIATOR,
    "aix_gr7": VEHICLE_TYPE_AVIATOR,
    "aix_su47": VEHICLE_TYPE_AVIATOR,
    "aix_yak38": VEHICLE_TYPE_AVIATOR,
    "aix_su22": VEHICLE_TYPE_AVIATOR,
    "aix_spitfire_v": VEHICLE_TYPE_AVIATOR,
    "aix_spitfire_ix": VEHICLE_TYPE_AVIATOR,
    "aix_phantom_ii": VEHICLE_TYPE_AVIATOR,
    "aix_phantom_fgr2": VEHICLE_TYPE_AVIATOR,
    "aix_p51d": VEHICLE_TYPE_AVIATOR,
    "aix_ju87b": VEHICLE_TYPE_AVIATOR,
    "aix_f14": VEHICLE_TYPE_AVIATOR,
    "aix_bf109e": VEHICLE_TYPE_AVIATOR,
    "aix_a7": VEHICLE_TYPE_AVIATOR,
    "boat_markv": VEHICLE_TYPE_TRANSPORT,
}

weaponTypeMap = {
    "usrif_m16a2": WEAPON_TYPE_ASSAULT,
    "rurif_ak101": WEAPON_TYPE_ASSAULT,
    "rurif_ak47": WEAPON_TYPE_ASSAULT,
    "usrif_sa80": WEAPON_TYPE_ASSAULT,
    "usrif_g3a3": WEAPON_TYPE_ASSAULT,
    "usrif_m203": WEAPON_TYPE_ASSAULT,
    "rurif_gp30": WEAPON_TYPE_ASSAULT,
    "rurif_gp25": WEAPON_TYPE_ASSAULT,
    "usrgl_m203": WEAPON_TYPE_ASSAULTGRN,
    "rurgl_gp30": WEAPON_TYPE_ASSAULTGRN,
    "rurgl_gp25": WEAPON_TYPE_ASSAULTGRN,
    "rurrif_ak74u": WEAPON_TYPE_CARBINE,
    "usrif_m4": WEAPON_TYPE_CARBINE,
    "rurif_ak74u": WEAPON_TYPE_CARBINE,
    "chrif_type95": WEAPON_TYPE_CARBINE,
    "usrif_g36c": WEAPON_TYPE_CARBINE,
    "uslmg_m249saw": WEAPON_TYPE_LMG,
    "rulmg_rpk74": WEAPON_TYPE_LMG,
    "chlmg_type95": WEAPON_TYPE_LMG,
    "rulmg_pkm": WEAPON_TYPE_LMG,
    "usrif_m24": WEAPON_TYPE_SNIPER,
    "rurif_dragunov": WEAPON_TYPE_SNIPER,
    "chsni_type88": WEAPON_TYPE_SNIPER,
    "ussni_m82a1": WEAPON_TYPE_SNIPER,
    "ussni_m95_barret": WEAPON_TYPE_SNIPER,
    "uspis_92fs": WEAPON_TYPE_PISTOL,
    "uspis_92fs_silencer": WEAPON_TYPE_PISTOL,
    "rupis_baghira": WEAPON_TYPE_PISTOL,
    "rupis_baghira_silencer": WEAPON_TYPE_PISTOL,
    "chpis_qsz92": WEAPON_TYPE_PISTOL,
    "chpis_qsz92_silencer": WEAPON_TYPE_PISTOL,
    "usatp_predator": WEAPON_TYPE_ATAA,
    "chat_eryx": WEAPON_TYPE_ATAA,
    "usrif_mp5_a3": WEAPON_TYPE_SMG,
    "rurif_bizon": WEAPON_TYPE_SMG,
    "chrif_type85": WEAPON_TYPE_SMG,
    "usrif_remington11-87": WEAPON_TYPE_SHOTGUN,
    "rusht_saiga12": WEAPON_TYPE_SHOTGUN,
    "chsht_norinco982": WEAPON_TYPE_SHOTGUN,
    "chsht_protecta": WEAPON_TYPE_SHOTGUN,
    "ussht_jackhammer": WEAPON_TYPE_SHOTGUN,
    "kni_knife": WEAPON_TYPE_KNIFE,
    "c4_explosives": WEAPON_TYPE_C4,
    "ushgr_m67": WEAPON_TYPE_HANDGRENADE,
    "usmin_claymore": WEAPON_TYPE_CLAYMORE,
    "defibrillator": WEAPON_TYPE_SHOCKPAD,
    "at_mine": WEAPON_TYPE_ATMINE,
    "simrad": WEAPON_TYPE_TARGETING,
    # xpack1 stuff
    "nshgr_flashbang": WEAPON_TYPE_TACTICAL,
    "sasrif_teargas": WEAPON_TYPE_TACTICAL,
    "insgr_rpg": WEAPON_TYPE_ATAA,
    "nsrif_crossbow": WEAPON_TYPE_ZIPLINE,
    "rurif_oc14": WEAPON_TYPE_ASSAULT,
    "sasrif_fn2000": WEAPON_TYPE_ASSAULT,
    "sasgr_fn2000": WEAPON_TYPE_ASSAULTGRN,
    "sasrif_g36e": WEAPON_TYPE_ASSAULT,
    "sasrif_g36k": WEAPON_TYPE_ASSAULT,
    "sasrif_mg36": WEAPON_TYPE_LMG,
    "sasrif_mp7": WEAPON_TYPE_SMG,
    "spzrif_aps": WEAPON_TYPE_ASSAULT,
    "usrif_fnscarh": WEAPON_TYPE_ASSAULT,
    "usrif_fnscarl": WEAPON_TYPE_CARBINE,
    # xpack1 unlocks
    "insgr_rpg": WEAPON_TYPE_ATAA,
    "rurif_oc14": WEAPON_TYPE_ASSAULT,
    "sasrif_fn2000": WEAPON_TYPE_ASSAULT,
    "sasgr_fn2000": WEAPON_TYPE_ASSAULTGRN,
    "sasrif_g36e": WEAPON_TYPE_ASSAULT,
    "sasrif_g36k": WEAPON_TYPE_ASSAULT,
    "sasrif_mg36": WEAPON_TYPE_LMG,
    "sasrif_mp7": WEAPON_TYPE_SMG,
    "spzrif_aps": WEAPON_TYPE_ASSAULT,
    "usrif_fnscarh": WEAPON_TYPE_ASSAULT,
    "usrif_fnscarl": WEAPON_TYPE_CARBINE,
    # booster pack 1
    "eurif_fnp90": WEAPON_TYPE_SMG,
    "eurif_hk53a3": WEAPON_TYPE_CARBINE,
    "gbrif_benelli_m4": WEAPON_TYPE_SHOTGUN,
    "gbrif_l96a1": WEAPON_TYPE_SNIPER,
    "eurif_famas": WEAPON_TYPE_ASSAULT,
    "gbrif_sa80a2_l85": WEAPON_TYPE_ASSAULT,
    "gbgr_sa80a2_l85": WEAPON_TYPE_ASSAULTGRN,
    "gbrif_hk21": WEAPON_TYPE_LMG,
    # dcon
    "car15": WEAPON_TYPE_CARBINE,
    "vss": WEAPON_TYPE_CARBINE,
    "rpg7": WEAPON_TYPE_ATAA,
    "dcon_smaw": WEAPON_TYPE_ATAA,
    "fim92a": WEAPON_TYPE_ATAA,
    "dcon_stingerhh": WEAPON_TYPE_ATAA,
    "gltd": WEAPON_TYPE_TARGETING,
    # POE2
    "at_mine": WEAPON_TYPE_ATMINE,
    "at_mine2": WEAPON_TYPE_ATMINE,
    "c4_explosives": WEAPON_TYPE_C4,
    "defibrillator": WEAPON_TYPE_SHOCKPAD,
    "gergre_dm61": WEAPON_TYPE_HANDGRENADE,
    "gergrl_ag36": WEAPON_TYPE_ASSAULTGRN,
    "gerkni_km2000": WEAPON_TYPE_KNIFE,
    "gerlmg_mg3": WEAPON_TYPE_LMG,
    "gerlmg_mg36": WEAPON_TYPE_LMG,
    "gerpis_p8": WEAPON_TYPE_PISTOL,
    "gerrif_g36": WEAPON_TYPE_ASSAULT,
    "gerrif_g36c": WEAPON_TYPE_ASSAULT,
    "gerrif_g36k": WEAPON_TYPE_ASSAULT,
    "gerrif_msg90": WEAPON_TYPE_SNIPER,
    "gerroc_bunkerfaust": WEAPON_TYPE_ATAA,
    "gerroc_fliegerfaust2": WEAPON_TYPE_ATAA,
    "gerroc_panzerfaust3": WEAPON_TYPE_ATAA,
    "gerroc_panzerfaust3t": WEAPON_TYPE_ATAA,
    "gersni_g82": WEAPON_TYPE_CARBINE,
    "gergre_smoke": WEAPON_TYPE_TACTICAL,
    "gergre_smoke2": WEAPON_TYPE_TACTICAL,
    "katana": WEAPON_TYPE_KNIFE,
    "ruskni_expknife": WEAPON_TYPE_KNIFE,
    "ukrgre_rdg2": WEAPON_TYPE_ASSAULTGRN,
    "ukrgre_rdg2_2": WEAPON_TYPE_ASSAULTGRN,
    "ukrgre_rgd5": WEAPON_TYPE_ASSAULTGRN,
    "ukrgrl_gp25": WEAPON_TYPE_ASSAULTGRN,
    "ukrlmg_pkm": WEAPON_TYPE_LMG,
    "ukrlmg_rpk74": WEAPON_TYPE_LMG,
    "ukrpis_fort12": WEAPON_TYPE_PISTOL,
    "ukrpis_pb6p9": WEAPON_TYPE_PISTOL,
    "ukrrif_aks74u": WEAPON_TYPE_CARBINE,
    "ukrrif_pp2000": WEAPON_TYPE_SMG,
    "ukrrif_pp2000_2": WEAPON_TYPE_SMG,
    "ukrrif_svd": WEAPON_TYPE_SNIPER,
    "ukrrif_skorpion": WEAPON_TYPE_SNIPER,
    "ukrrif_vepr": WEAPON_TYPE_ASSAULT,
    "ukrrif_vintorez": WEAPON_TYPE_SNIPER,
    "ukrroc_rpgfrag": WEAPON_TYPE_ATAA,
    "ukrroc_rpgheat": WEAPON_TYPE_ATAA,
    "ukrroc_rpgtandem": WEAPON_TYPE_ATAA,
    "ukrroc_rpgthermo": WEAPON_TYPE_ATAA,
    "ukrroc_sa7": WEAPON_TYPE_ATAA,
    "ukrsht_toz194": WEAPON_TYPE_SHOTGUN,
    "ukrsmg_asval": WEAPON_TYPE_ASSAULT,
    "ukrsni_ntw20": WEAPON_TYPE_ASSAULT,
    "usasht_m1014": WEAPON_TYPE_SHOTGUN,
    "usasmg_mp7": WEAPON_TYPE_SMG,
    "usasmg_mp7_2": WEAPON_TYPE_SMG,
    "usasmg_mp7_scoped": WEAPON_TYPE_SMG,
    "usasmg_mp7_silenced": WEAPON_TYPE_SMG,
    "ushgr_m67": WEAPON_TYPE_HANDGRENADE,
    "usmin_claymore": WEAPON_TYPE_CLAYMORE,
    "usmin_claymore2": WEAPON_TYPE_CLAYMORE,
    "usrif_g36c": WEAPON_TYPE_ASSAULT,
    # BF2AUS
    "bf2aus_ak_bayonet": WEAPON_TYPE_KNIFE,
    "bf2aus_binoculars": WEAPON_TYPE_TARGETING,
    "bf2aus_browninghp": WEAPON_TYPE_PISTOL,
    "bf2aus_carl_gustav": WEAPON_TYPE_ATAA,
    "bf2aus_f1": WEAPON_TYPE_HANDGRENADE,
    "bf2aus_f88c": WEAPON_TYPE_ASSAULT,
    "bf2aus_f88gla_gl": WEAPON_TYPE_ASSAULTGRN,
    "bf2aus_f88gla_rif": WEAPON_TYPE_ASSAULT,
    "bf2aus_f88s": WEAPON_TYPE_ASSAULT,
    "bf2aus_m4a1": WEAPON_TYPE_CARBINE,
    "bf2aus_m72law": WEAPON_TYPE_ATAA,
    "bf2aus_rpg18": WEAPON_TYPE_ATAA,
    "bf2aus_rpg7": WEAPON_TYPE_ATAA,
    "bf2aus_sa7": WEAPON_TYPE_ATAA,
    "bf2aus_sr-98": WEAPON_TYPE_SNIPER,
    "bf2aus_stinger": WEAPON_TYPE_ATAA,
    "bf2aus_timed_c4": WEAPON_TYPE_C4,
    "bf2aus_usp": WEAPON_TYPE_PISTOL,
    # naw
    "t2_1887_shotgun": WEAPON_TYPE_SHOTGUN,
    "rambo_3_knife": WEAPON_TYPE_KNIFE,
    "nsrif_crossbow": WEAPON_TYPE_SNIPER,
    "m14lm": WEAPON_TYPE_ATMINE,
    "ap_mine": WEAPON_TYPE_ATMINE,
    "deserteagle": WEAPON_TYPE_PISTOL,
    "dual_deserteagles": WEAPON_TYPE_PISTOL,
    "dual_uzi": WEAPON_TYPE_SMG,
    "iraq_scorpion": WEAPON_TYPE_SMG,
    "galil": WEAPON_TYPE_CARBINE,
    "grail": WEAPON_TYPE_ATAA,
    "ied": WEAPON_TYPE_C4,
    "javelin": WEAPON_TYPE_ATAA,
    "ksvk": WEAPON_TYPE_SNIPER,
    "m72law": WEAPON_TYPE_ATAA,
    "m40a3_silenced": WEAPON_TYPE_SNIPER,
    "m40a3": WEAPON_TYPE_SNIPER,
    "psg1": WEAPON_TYPE_SNIPER,
    "rpg7": WEAPON_TYPE_ATAA,
    "sigp226": WEAPON_TYPE_PISTOL,
    "steyr_aug": WEAPON_TYPE_CARBINE,
    "steyr_aug_m203": WEAPON_TYPE_CARBINE,
    "steyr_aug_m203_gl": WEAPON_TYPE_ASSAULTGRN,
    "steyr_specops": WEAPON_TYPE_CARBINE,
    "stinger": WEAPON_TYPE_ATAA,
    "svds": WEAPON_TYPE_SNIPER,
    "ump45": WEAPON_TYPE_PISTOL,
    "uzi": WEAPON_TYPE_SMG,
    "mk19": WEAPON_TYPE_ASSAULTGRN,
    "oerlikonaa": WEAPON_TYPE_ATAA,
    "iraqat_rpg7": WEAPON_TYPE_ATAA,
    "usat_smaw": WEAPON_TYPE_ATAA,
    "iraqaa_sa7": WEAPON_TYPE_ATAA,
    "usaa_fm92a": WEAPON_TYPE_ATAA,
    "mim23": WEAPON_TYPE_ATAA,
    "sa-3": WEAPON_TYPE_ATAA,
    "rh202_aa": WEAPON_TYPE_ATAA,
    "igla_tech": WEAPON_TYPE_ATAA,
    "civ2_tow": WEAPON_TYPE_ATAA,
    "tos1_missile": WEAPON_TYPE_ATAA,
    "tomahawk_bgm109": WEAPON_TYPE_ATAA,
    "mk48_torpedo": WEAPON_TYPE_ATAA,
    "m270_missile": WEAPON_TYPE_ATAA,
    "hh_stinger": WEAPON_TYPE_ATAA,
    "brad_missile": WEAPON_TYPE_ATAA,
    "b57_nuke": WEAPON_TYPE_ATAA,
    "zigs_hellfire": WEAPON_TYPE_ATAA,
    "minigun": WEAPON_TYPE_SMG,
    "hgr_smoke_1": WEAPON_TYPE_HANDGRENADE,
    "hgr_smoke_2": WEAPON_TYPE_HANDGRENADE,
}


kitTypeMap = {
    "us_at": KIT_TYPE_AT,
    "us_assault": KIT_TYPE_ASSAULT,
    "us_engineer": KIT_TYPE_ENGINEER,
    "us_medic": KIT_TYPE_MEDIC,
    "us_specops": KIT_TYPE_SPECOPS,
    "us_support": KIT_TYPE_SUPPORT,
    "us_sniper": KIT_TYPE_SNIPER,
    "mec_at": KIT_TYPE_AT,
    "mec_assault": KIT_TYPE_ASSAULT,
    "mec_engineer": KIT_TYPE_ENGINEER,
    "mec_medic": KIT_TYPE_MEDIC,
    "mec_specops": KIT_TYPE_SPECOPS,
    "mec_support": KIT_TYPE_SUPPORT,
    "mec_sniper": KIT_TYPE_SNIPER,
    "ch_at": KIT_TYPE_AT,
    "ch_assault": KIT_TYPE_ASSAULT,
    "ch_engineer": KIT_TYPE_ENGINEER,
    "ch_medic": KIT_TYPE_MEDIC,
    "ch_specops": KIT_TYPE_SPECOPS,
    "ch_support": KIT_TYPE_SUPPORT,
    "ch_sniper": KIT_TYPE_SNIPER,
    # xpack1
    "seal_at": KIT_TYPE_AT,
    "seal_assault": KIT_TYPE_ASSAULT,
    "seal_engineer": KIT_TYPE_ENGINEER,
    "seal_medic": KIT_TYPE_MEDIC,
    "seal_specops": KIT_TYPE_SPECOPS,
    "seal_support": KIT_TYPE_SUPPORT,
    "seal_sniper": KIT_TYPE_SNIPER,
    "sas_at": KIT_TYPE_AT,
    "sas_assault": KIT_TYPE_ASSAULT,
    "sas_engineer": KIT_TYPE_ENGINEER,
    "sas_medic": KIT_TYPE_MEDIC,
    "sas_specops": KIT_TYPE_SPECOPS,
    "sas_support": KIT_TYPE_SUPPORT,
    "sas_sniper": KIT_TYPE_SNIPER,
    "spetsnaz_at": KIT_TYPE_AT,
    "spetsnaz_assault": KIT_TYPE_ASSAULT,
    "spetsnaz_engineer": KIT_TYPE_ENGINEER,
    "spetsnaz_medic": KIT_TYPE_MEDIC,
    "spetsnaz_specops": KIT_TYPE_SPECOPS,
    "spetsnaz_support": KIT_TYPE_SUPPORT,
    "spetsnaz_sniper": KIT_TYPE_SNIPER,
    "mecsf_at": KIT_TYPE_AT,
    "mecsf_assault": KIT_TYPE_ASSAULT,
    "mecsf_engineer": KIT_TYPE_ENGINEER,
    "mecsf_medic": KIT_TYPE_MEDIC,
    "mecsf_specops": KIT_TYPE_SPECOPS,
    "mecsf_support": KIT_TYPE_SUPPORT,
    "mecsf_sniper": KIT_TYPE_SNIPER,
    "chinsurgent_at": KIT_TYPE_AT,
    "chinsurgent_assault": KIT_TYPE_ASSAULT,
    "chinsurgent_engineer": KIT_TYPE_ENGINEER,
    "chinsurgent_medic": KIT_TYPE_MEDIC,
    "chinsurgent_specops": KIT_TYPE_SPECOPS,
    "chinsurgent_support": KIT_TYPE_SUPPORT,
    "chinsurgent_sniper": KIT_TYPE_SNIPER,
    "meinsurgent_at": KIT_TYPE_AT,
    "meinsurgent_assault": KIT_TYPE_ASSAULT,
    "meinsurgent_engineer": KIT_TYPE_ENGINEER,
    "meinsurgent_medic": KIT_TYPE_MEDIC,
    "meinsurgent_specops": KIT_TYPE_SPECOPS,
    "meinsurgent_support": KIT_TYPE_SUPPORT,
    "meinsurgent_sniper": KIT_TYPE_SNIPER,
    "mecsf_at_special": KIT_TYPE_AT,
    "mecsf_assault_special": KIT_TYPE_ASSAULT,
    "mecsf_specops_special": KIT_TYPE_SPECOPS,
    "mecsf_sniper_special": KIT_TYPE_SNIPER,
    "sas_at_special": KIT_TYPE_AT,
    "sas_assault_special": KIT_TYPE_ASSAULT,
    "sas_specops_special": KIT_TYPE_SPECOPS,
    "sas_sniper_special": KIT_TYPE_SNIPER,
    # booster pack 1
    "eu_at": KIT_TYPE_AT,
    "eu_assault": KIT_TYPE_ASSAULT,
    "eu_engineer": KIT_TYPE_ENGINEER,
    "eu_medic": KIT_TYPE_MEDIC,
    "eu_specops": KIT_TYPE_SPECOPS,
    "eu_support": KIT_TYPE_SUPPORT,
    "eu_sniper": KIT_TYPE_SNIPER,
    # dcon
    "dcon_cruiserus": KIT_TYPE_SNIPER,
    "us_assault_nopara": KIT_TYPE_ASSAULT,
    "us_at_nopara": KIT_TYPE_AT,
    "us_engineer_nopara": KIT_TYPE_ENGINEER,
    "us_medic_nopara": KIT_TYPE_MEDIC,
    "us_sniper_heavy": KIT_TYPE_SNIPER,
    "us_sniper_heavy_nopara": KIT_TYPE_SNIPER,
    "us_sniper_nopara": KIT_TYPE_SNIPER,
    "us_specops_nopara": KIT_TYPE_SPECOPS,
    "us_support_nopara": KIT_TYPE_SUPPORT,
    "dcon_cruisermc": KIT_TYPE_SNIPER,
    "mec_specops_vss": KIT_TYPE_SPECOPS,
    "mec_at_nosting": KIT_TYPE_AT,
    # POE2
    "ger_assault": KIT_TYPE_ASSAULT,
    "ger_at": KIT_TYPE_AT,
    "ger_engineer": KIT_TYPE_ENGINEER,
    "ger_medic": KIT_TYPE_MEDIC,
    "ger_sniper": KIT_TYPE_SNIPER,
    "ger_specops": KIT_TYPE_SPECOPS,
    "ger_support": KIT_TYPE_SUPPORT,
    "ukr_at": KIT_TYPE_AT,
    "ukr_assault": KIT_TYPE_ASSAULT,
    "ukr_engineer": KIT_TYPE_ENGINEER,
    "ukr_medic": KIT_TYPE_MEDIC,
    "ukr_specops": KIT_TYPE_SPECOPS,
    "ukr_support": KIT_TYPE_SUPPORT,
    "ukr_sniper": KIT_TYPE_SNIPER,
    # BF2AUS
    "ch_at_aa": KIT_TYPE_AT,
    "mec_at_aa": KIT_TYPE_AT,
    "us_at_aa": KIT_TYPE_AT,
    # naw
    "iran_specops": KIT_TYPE_SPECOPS,
    "iraq_sniper": KIT_TYPE_SNIPER,
    "czh_sniper": KIT_TYPE_SNIPER,
    "kor_assault": KIT_TYPE_ASSAULT,
    "uk_assault": KIT_TYPE_ASSAULT,
    "jap_support": KIT_TYPE_SUPPORT,
    "nor_support": KIT_TYPE_SUPPORT,
    "ch_engineer": KIT_TYPE_ENGINEER,
    "ger_engineer": KIT_TYPE_ENGINEER,
    "pak_medic": KIT_TYPE_MEDIC,
    "den_medic": KIT_TYPE_MEDIC,
    "syr_at": KIT_TYPE_AT,
    "can_at": KIT_TYPE_AT,
    "us_support_super": KIT_TYPE_SUPPORT,
    "us_sniper_super": KIT_TYPE_SNIPER,
    "us_engineer_super": KIT_TYPE_ENGINEER,
    "us_antiair": KIT_TYPE_AT,
    "ch_engineer_super": KIT_TYPE_ENGINEER,
    "ch_antiair": KIT_TYPE_AT,
    "ch_support_super": KIT_TYPE_SUPPORT,
    "ch_sniper_super": KIT_TYPE_SNIPER,
}

armyMap = {
    "us": ARMY_USA,
    "mec": ARMY_MEC,
    "ch": ARMY_CHINESE,
    # xpack1
    "seal": ARMY_SEALS,
    "sas": ARMY_SAS,
    "spetz": ARMY_SPETZNAS,
    "mecsf": ARMY_MECSF,
    "chinsurgent": ARMY_REBELS,
    "meinsurgent": ARMY_INSURGENTS,
    # booster pack 1
    "eu": ARMY_EURO,
    "ger": ARMY_GER,
    "ukr": ARMY_UKR,
}

mapMap = {
    # middle eastern theater
    "kubra_dam": "0",
    "mashtuur_city": "1",
    "operation_clean_sweep": "2",
    "zatar_wetlands": "3",
    "strike_at_karkand": "4",
    "sharqi_peninsula": "5",
    "gulf_of_oman": "6",
    "operationsmokescreen": "10",
    "taraba_quarry": "11",
    "road_to_jalalabad": "12",
    # Asian Theater
    "daqing_oilfields": "100",
    "dalian_plant": "101",
    "dragon_valley": "102",
    "fushe_pass": "103",
    "hingan_hills": "104",
    "songhua_stalemate": "105",
    "greatwall": "110",
    # US Theatre
    "midnight_sun": "200",
    "operationroadrage": "201",
    "operationharvest": "202",
    # xpack 1
    "devils_perch": "300",
    "iron_gator": "301",
    "night_flight": "302",
    "warlord": "303",
    "leviathan": "304",
    "mass_destruction": "305",
    "surge": "306",
    "ghost_town": "307",
    # Special maps
    "wake_island_2007": "601",
    # dcon
    "dcon_73_eastings": "701",
    "dcon_desert_shield": "702",
    "dcon_el_alamein": "703",
    "dcon_gazala": "704",
    "dcon_inshallah_valley": "705",
    "dcon_lostvillage": "706",
    "dcon_weapon_bunkers": "707",
    "outskirts_of_mosul": "708",
    # PR
    "airport": "801",
    "al_fallujah_region": "802",
    "albasrah": "803",
    "ejod_desert_6": "804",
    "goods_station": "805",
    "helmand_province": "806",
    "hills_of_hamgyong": "807",
    "inishail_forest": "808",
    "jabal": "809",
    "mao_valley": "810",
    "muttrah_city": "811",
    "operation_compton": "812",
    "operation_ghost_train": "813",
    "operation_greasy_mullet": "814",
    "operation_phoenix": "815",
    "qwai1": "816",
    "raid_on_moskiye": "817",
    "road_to_kyongan_ni": "818",
    "steel_thunder": "819",
    "street": "820",
    "sunset_city": "821",
    # AusForces
    "al_asad_airfield": "901",
    "battle_for_termez": "902",
    "kubaysah_cement_factory": "903",
    "sahl_al_abbah": "904",
    # POE2 maps
    "battle_of_sambir": "1001",
    "carpathian_mountains": "1002",
    "dnipro_sunrise": "1003",
    "dnister_river_valley": "1004",
    "fallen": "1005",
    "first_snow": "1006",
    "guardian": "1007",
    "highway_to_hell": "1008",
    "lutsk": "1009",
    "orel": "1010",
    "rivne": "1011",
    "rolling_thunder": "1012",
    "zhytomyr": "1013",
    "spies_like_us": "1014",
    "city_of_the_dead": "1015",
    "day_of_damnation": "1016",
    "deliverance": "1017",
    "hell_awaits": "1018",
    "night_of_the_damned": "1019",
    "no_mans_land": "1020",
    "berezne": "1021",
    "operationacorn": "1022",
    "red_dawn": "1023",
    "stormfront": "1024",
    "woodland": "1025",
    # naw
    "a_bad_surprise": "897",
    "adh_oasis_revisited": "801",
    "al_khafji_docks": "880",
    "back_to_the_suribachi": "896",
    "basrahs_edge_bfds": "802",
    "berlin": "882",
    "bl_bridge2b": "884",
    "cat_island": "839",
    "christmas_hill": "838",
    "dalian_2": "822",
    "daqing_oilfields": "824",
    "dragon_valley": "823",
    "eagles_nest": "885",
    "el_alamein_bfds_sp": "840",
    "end_of_the_line": "841",
    "forest_railway": "825",
    "frostbite": "811",
    "frostbite_night": "812",
    "fuShe_pass": "826",
    "gazala_bfds_v2": "804",
    "greatWall": "110",
    "gulf_of_oman": "888",
    "heaven_and_hell": "805",
    "highway_tampa": "827",
    "invasion_of_the_coral_sea": "808",
    "invasion_of_the_philippines": "806",
    "iraq_oilfields": "807",
    "iwo_jima": "809",
    "jibbel_city": "810",
    "kasserine_pass": "889",
    "kubra_dam": "828",
    "last_stand_snipers": "893",
    "mashtuur_city": "829",
    "midnight_sun": "200",
    "midway": "813",
    "none_but_the_brave": "815",
    "operation_black_hawk_down": "891",
    "operation_blue_pearl": "871",
    "operation_clean_sweep": "876",
    "operationharvest": "202",
    "operation_gatecrasher": "203",
    "operationroadrage": "201",
    "operationsmokescreen": "10",
    "philippine_sea": "821",
    "pripiyat": "865",
    "prologue": "816",
    "road_to_jalalabad": "867",
    "sharqi_peninsula": "830",
    "songhua_stalemate": "831",
    "stalingrad": "879",
    "strike_at_karkand": "833",
    "strike_at_karkand_2": "817",
    "sunset_in_tunisia": "863",
    "taraba_quarry": "11",
    "terminus": "892",
    "tobruk": "846",
    "urban_raid": "849",
    "village_lost": "818",
    "vulcan_island": "875",
    "wake_island_2007": "834",
    "warbirds_ii": "850",
    "waterfront": "819",
    "waylaid": "820",
    "zatar_wetlands": "835",
}
UNKNOWN_MAP = 99

gameModeMap = {
    "gpm_cq": 0,
    "gpm_sl": 1,
    "gpm_coop": 2,
    "gpm_ctf": 3,
    "gpm_obj": 4,
    "gpm_dom": 5,
}
UNKNOWN_GAMEMODE = 99


def getVehicleType(templateName):
    try:
        vehicleType = vehicleTypeMap[string.lower(templateName)]
    except KeyError:
        return VEHICLE_TYPE_UNKNOWN

    return vehicleType


def getWeaponType(templateName):
    try:
        weaponType = weaponTypeMap[string.lower(templateName)]
    except KeyError:
        return WEAPON_TYPE_UNKNOWN

    return weaponType


def getKitType(templateName):
    try:
        kitType = kitTypeMap[string.lower(templateName)]
    except KeyError:
        return KIT_TYPE_UNKNOWN

    return kitType


def getArmy(templateName):
    try:
        army = armyMap[string.lower(templateName)]
    except KeyError:
        return ARMY_UNKNOWN

    return army


def getMapId(mapName):
    try:
        mapId = mapMap[string.lower(mapName)]
    except KeyError:
        return UNKNOWN_MAP

    return mapId


def getGameModeId(gameMode):
    try:
        gameModeId = gameModeMap[string.lower(gameMode)]
    except KeyError:
        return UNKNOWN_GAMEMODE

    return gameModeId


def getRootParent(obj):
    parent = obj.getParent()

    if parent == None:
        return obj

    return getRootParent(parent)


if g_debug:
    print "Stat constants loaded"
