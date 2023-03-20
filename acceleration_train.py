#-------------------------------------------------------------------------------
# Name:        Vitesse_train
# Purpose:
#
# Author:      barbier lucas
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


def acceleration(v,train) :
    ''' Permet de donner l'accélération d'un type de train en fonction de sa vitesse actuelle
    Entrées : v = vitesse actuelle du train en km/h ; train = le type de train et ses caractéristiques
    Sortie : un tuple (a,d) avec a l'accélération en m/s² et d la décélération en m/s²
    '''
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
    ''' Permet de donner le temps pour passer de la vitesse actuelle à la vitesse consigne pour un type de train
    Entrées : v_actuelle = la vitesse actuelle du train en km/h ; v_consigne = la vitesse qu'on veut lui donner en km/h ; train = le type de train dont on veut modifier la vitesse
    Sortie : temps = le temps mis pour passer de v_actuelle à v_consigne en s
    '''
    if v_actuelle >= v_consigne :
        temps = (v_actuelle - v_consigne)*3.6/acceleration(v_actuelle , train)[1]
    elif v_consigne > train[4] :
        raise ValueError('Vitesse supérieure à la vitesse maximale du train')
    else :
        i = 0
        while v_actuelle < v_consigne:
            i += 0.1
            v_actuelle += acceleration(v_actuelle , train)[0]*0.1*3.6
        temps = i
    return temps

print(temps_acceleration(140,140,tgv))