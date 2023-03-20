#-------------------------------------------------------------------------------
# Name:        Carac_trains
# Purpose:
#
# Author:      barbier lucas
#
# Created:     17/03/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

"""Matrice_vitesse_effort_train = M_v_e = [[palier_1 , effort_1] , ... , [palier_n , effort_n]]
train = [masse(t), RAV_A, RAV_B, RAV_C, v_max, Matrice_vitesse_effort , nbe_passagers]"""

# TGV
M_v_e_tgv = np.array([[0 , 220000] , [20 , 220000] , [40 , 217500] , [60 , 214000] , [70 , 203000] , [75 , 195000] , [80 , 177000] , [84, 170000] , [100 , 170000] , [120 , 169000] , [140 , 165500] , [160 , 161000] , [175 , 156000] , [180 , 153000] , [200 , 141000] , [220 , 128000] , [240 , 118000] , [260 , 108000] , [280 , 101000] , [300 , 94500] , [320, 90000]])
tgv = [424 , 6.368 , 0.0755 , 0.001262 , 320 , M_v_e_tgv , 510]

# TER 2N
M_v_e_2n = np.array([[0 , 370400] , [10 , 370400] , [20 , 370400] , [30 , 352000] , [40 , 306000] , [50 , 244800] , [60 , 204000] , [70 , 174860] , [80 , 153290] , [90 , 126960] , [100 , 107260] , [110 , 92090] , [120 , 80120] , [130 , 70490] , [140 , 62610] , [150 , 56070] , [160 , 50570]])
Ter_2n = [357.5 , 8.028 , 0.1 , 0.001854 , 160 , M_v_e_2n , 570]

# TER Regiolis
M_v_e_reg = np.array([[0 , 299200],
[5 , 299200],
[10 ,299200],
[20 ,299200],
[30 ,299200],
[38 ,299200],
[40 ,299200],
[42 ,299200],
[50 ,248830],
[60 ,207360],
[70 ,177740],
[80 ,155520],
[90 ,138240],
[100 ,124420],
[110 ,113110],
[120 ,103680],
[130 ,95700],
[140 ,88870],
[150 ,82940],
[160 ,77760]])
Ter_regiolis = [294 , 9.931 , 0.1 , 0.002528 , 160 , M_v_e_reg , 228]

# TER Autorail
M_v_e_auto = np.array([[0,51900],
[10,50000],
[20,41500],
[25,40000],
[30,36000],
[33,34000],
[36,32000],
[40,30300],
[44,28000],
[48,26000],
[53,24000],
[58,22000],
[60,21200],
[63,20000],
[70,18000],
[77,16000],
[86,14000],
[93,13100],
[100,12000],
[110,12200],
[120,12000],
[130,11000],
[140,10600]])
Ter_autorail = [53.7 , 13.2 , 0.086 , 0.0041 , 140 , M_v_e_auto , 61]