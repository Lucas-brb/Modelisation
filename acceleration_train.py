#-------------------------------------------------------------------------------
# Name:        acceleration_train
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
import matplotlib.pyplot as plt

"""Le code suivant va permettre de calculer l'accélération d'un train en fonction de sa vitesse actuelle.
Pour ce faire nous allons renseigner les données contenues dans Excel et les implémenter dans python.
Voici comment les matrices sont représentées :

Matrice_vitesse_effort = M_v_e = [[palier_1 , effort_1] , ... , [palier_n , effort_n]]
train = [masse(t), RAV_A, RAV_B, RAV_C, v_max, Matrice_vitesse_effort]"""


def acceleration(v,train) :
    '''
    Permet de donner l'accélération d'un type de train en fonction de sa vitesse actuelle
    Entrées :
        v = vitesse actuelle du train en km/h
        train = le type de train et ses caractéristiques
    Sortie :
        un tuple (a,f) avec a l'accélération en m/s² et le freinage en m/s²
    '''
    i = 0
    M_v_e = train[5] # on prend la matrice des efforts en fonction de la vitesse (donnée dans le fichier excel)
    RAV = train[0]*(train[1] + train[2]*v + train[3]*v**2)
    nbe_paliers = np.shape(M_v_e)[0]
    f = 0.5 #le freinage de tous les trains
    if v >= train[4] :
        return (0,0.5) #on n'accélère pas au dessus de la vitesse limite du train
    else :
        while v >= M_v_e[i,0] : #on cherche dans quel intervalle la vitesse actuelle se situe
            i += 1
    a = (M_v_e[i-1,1] - RAV)/(train[0]*1000) # application du PFD
    return a,f


def temps_acceleration(v_actuelle, v_consigne, train) :
    '''
    Permet de donner le temps pour passer de la vitesse actuelle à la vitesse consigne pour un type de train
    Entrées :
        v_actuelle = la vitesse actuelle du train en km/h
        v_consigne = la vitesse qu'on veut lui donner en km/h
        train = le type de train dont on veut modifier la vitesse
    Sorties :
        temps = le temps mis pour passer de v_actuelle à v_consigne en s
        l = la distance de transition d'une vitesse à l'autre
    '''
    v_actuelle_m = v_actuelle/3.6
    v_consigne_m = v_consigne/3.6 # on travaille avec des vitesses en m.s pour faciliter les calculs
    a, f = acceleration(v_actuelle , train)
    T = [0]
    Vitesses = [v_actuelle_m]
    if v_actuelle_m >= v_consigne_m :
        temps = (v_actuelle_m - v_consigne_m)/f # freinage constant
        l = (v_actuelle_m**2 - v_consigne_m**2)/(2*f)
    elif v_consigne > train[4] :
        raise ValueError('Vitesse supérieure à la vitesse maximale du train')
    else :
        i = 0
        l = 0
        while v_actuelle_m < v_consigne_m:
            i += 0.01 # on échantillonne sur 1/100ème de seconde
            l += v_actuelle_m*0.01 # on calcule la distance parcourue avec la méthode des triangles
            v_actuelle_m += a*0.01 # méthode des rectangles
            v_actuelle = v_actuelle_m*3.6
            a,f = acceleration(v_actuelle , train) # actualisation de l'accélération
            T.append(i)
            Vitesses.append(v_actuelle_m)
        temps = i
        #plt.plot(t, vitesses)
        #plt.show()
    return temps,l/1000


def d_min(v_actuelle, v_lim1, v_lim2, train):
    '''
    Donne la distance minimale requise pour passer de la vitesse actuelle à la vitesse limite 2 en passant par la vitesse limite 1.
    Cette fonction a pour but de savoir si il est utile d'accélérer jusqu'à la limite de vitesse avant de freiner pour arriver au prochain tronçon.
    Entrées :
        v_actuelle = la vitesse actuelle du train (en km/h)
        v_lim1 = la vitesse limite sur le tronçon dans lequel est le train actuellement (km/h)
        v_lim2 = la vitesse limite sur le prochain tronçon (km/h)
        train = le type de train utilisé pour ce calcul
    Sortie :
        d_min = la distance minimale pour passer par v1 avant de passer à v2 (km)
    Remarque : on considère que v_actuelle <= v_lim1 car on a respecté la limitation de vitesse dans le tronçon
    '''
    v_actuelle_m = v_actuelle/3.6
    v_lim1_m = v_lim1/3.6
    v_lim2_m = v_lim2/3.6
    a,f = acceleration(v_actuelle,train)
    if v_lim1 > v_lim2 :
        d_min = (v_lim1_m**2 - v_lim2_m**2)/(2*f) # on condidère qu'on atteint la vitesse max, donc on initialise d_min à la longueur qu'il faut pour passer de v_lim1 à v_lim2
        while v_actuelle < v_lim1:
            d_min += v_actuelle_m*0.01
            v_actuelle_m += a*0.01
            v_actuelle = v_actuelle_m*3.6
            a,f = acceleration(v_actuelle , train) # actualisation de l'accélération
        return d_min/1000
    else:
        raise ValueError('v_lim2 > v_lim1')


def transition_tronçon(v_actuelle, v_tronçon1, v_tronçon2, l_tronçon, train) :
    '''
    Calcule le temps mis par le train pour parcourir le tronçon.
    Entrées :
        v_actuelle = la vitesse actuelle du train (km/h)
        v_tronçon1 = la vitesse du tronçon dans lequel le train est (km/h)
        v_tronçon2 = la vitesse du prochain tronçon (km/h)
        l_tronçon = la longueur du tronçon (km)
        train = le type de train qui parcourt ce tronçon
    Sorties :
        temps = le temps mis par le train pour parcourir le tronçon
        v_max_atteinte =
    Remarque : la question de l'éco-conduite n'est pas prise en compte ici, on essaie d'aller le plus vite possible
    '''
    v_actuelle_m = v_actuelle/3.6
    v_tronçon1_m = v_tronçon1/3.6
    v_tronçon2_m = v_tronçon2/3.6
    a,f = acceleration(v_actuelle, train)
    if v_tronçon1 > v_tronçon2 :
        d_m = d_min(v_actuelle, v_tronçon1, v_tronçon2, train)
        if l_tronçon >= d_m : # la vitesse maximale est atteignable
            temps = (v_tronçon1_m - v_tronçon2_m)/f #le temps qu'il faut pour freiner
            ta, la = temps_acceleration(v_actuelle, v_tronçon1, train)
            temps += ta # temps pour accélérer jusqu'à la vitesse limite
            temps += (l_tronçon*1000 - la*1000 - (v_tronçon1_m**2 - v_tronçon2_m**2)/f)/v_tronçon1_m # le temps passé à la vitesse limite
            v_max_atteinte = v_tronçon1
        else :
            v_max_atteinte = v_actuelle
            t_acc, d_acc = temps_acceleration(v_actuelle, v_max_atteinte, train)
            d_parcourue = (v_max_atteinte**2 - v_tronçon2_m**2)/f + d_acc*1000 # en mètre
            while d_parcourue < l_tronçon*1000 :
                v_max_atteinte += 1
                t_acc, d_acc = temps_acceleration(v_actuelle, v_max_atteinte, train)
                d_parcourue = ((v_max_atteinte/3.6)**2 - v_tronçon2_m**2)/f + d_acc*1000 # en mètre
            if v_max_atteinte >= v_tronçon2:
                temps = t_acc + (v_max_atteinte/3.6 - v_tronçon2_m)/f
            else :
                temps = t_acc
    else :
        if temps_acceleration(v_actuelle, v_tronçon2, train)[1] > l_tronçon :
            v_max_atteinte = v_actuelle
            t_acc, d_acc = temps_acceleration(v_actuelle, v_max_atteinte, train)
            d_parcourue = d_acc*1000 # en mètre
            while d_parcourue < l_tronçon*1000 :
                v_max_atteinte += 1
                t_acc, d_acc = temps_acceleration(v_actuelle, v_max_atteinte, train)
                if v_max_atteinte > v_tronçon2:
                    d_parcourue = d_acc + ((v_max_atteinte/3.6)**2 - v_tronçon2_m**2)/(2*0.5)
                else:
                    d_parcourue = + d_acc*1000 # en mètre
            temps = t_acc
        else :
            t_acc, d_acc = temps_acceleration(v_actuelle, v_tronçon1, train)
            temps = t_acc + (l_tronçon - d_acc)*1000/v_tronçon1_m
            v_max_atteinte = v_tronçon1
    return temps, v_max_atteinte

#print(transition_tronçon(0, 130, 0, 10, Ter_2n))