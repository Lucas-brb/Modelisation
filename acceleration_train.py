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
from Carac_trains import * # on importe tous les trains et leurs carctéristiques

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
    return (a,d)

def temps_acceleration(v_actuelle,v_consigne,train):
    if v_consigne <= v_actuelle :
        temps = (v_actuelle - v_consigne)/acceleration(v_actuelle , train)[1]
    else :
        temps = 0
    return temps

print(temps_acceleration(10,0,tgv))