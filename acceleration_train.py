#-------------------------------------------------------------------------------
# Name:        Vitesse_train
# Purpose:
#
# Author:      barbi
#
# Created:     14/03/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
"""Le code suivant va permettre de calculer l'accélération d'un train en fonction de sa vitesse actuelle.
Pour ce faire nous allons renseigner les données contenues dans Excel et les implémenter dans python.
Voici comment les matrices sont représentées :

Matrice_vitesse_effort = M_v_e = [[palier_1 , effort_1] , ... , [palier_n , effort_n]]
train = [masse(t), RAV_A, RAV_B, RAV_C, v_max, Matrice_vitesse_effort]"""


def acceleration(v,train) : #donne l'accélération du train en fonction de la vitesse
    i = 0
    M_v_e = train[5] # on prend la matrice des efforts en fonction de la vitesse (donnée dans le fichier excel)
    RAV = train[0]*(train[1] + train[2]*v + train[3]*v**2)
    nbe_paliers = np.shape(M_v_e)[0]
    d = 0.5 #la décélération de tous les trains
    if v >= train[4] :
        return (0,0.5) #on n'accélère pas au dessus de la vitesse limite du train
    else :
        while v >= M_v_e[i,0] : #on cherche dans quel intervalle la vitesse actuelle se situe
            i += 1
    a = (M_v_e[i-1,1] - RAV)/(train[0]*1000) # application du PFD
    print(M_v_e[i-1,1] , RAV , M_v_e[i-1,1] - RAV)
    return (a,d)
M_v_e_tgv = np.array([[0 , 220000] , [20 , 220000] , [40 , 217500] , [60 , 214000] , [70 , 203000] , [75 , 195000] , [80 , 177000] , [84, 170000] , [100 , 170000] , [120 , 169000] , [140 , 165500] , [160 , 161000] , [175 , 156000] , [180 , 153000] , [200 , 141000] , [220 , 128000] , [240 , 118000] , [260 , 108000] , [280 , 101000] , [300 , 94500] , [320, 90000]])
tgv = [424 , 6.368 , 0.0755 , 0.001262 , 320 , M_v_e_tgv ]
print(acceleration(0 , tgv))
