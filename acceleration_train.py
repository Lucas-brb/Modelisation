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
import matplotlib.pyplot as plt
import time
from donnees_lignes import *
import math

"""Le code suivant va permettre de calculer l'accélération d'un train en fonction de sa vitesse actuelle.
Pour ce faire nous allons renseigner les données contenues dans Excel et les implémenter dans python.
Voici comment les matrices sont représentées :

Matrice_vitesse_effort = M_v_e = [[palier_1 , effort_1] , ... , [palier_n , effort_n]]
train = [masse(t), RAV_A, RAV_B, RAV_C, v_max, Matrice_vitesse_effort]"""

def partie_positive(x) :
    if x > 0:
        return x
    return 0

def acceleration(v,train) :
    '''
    Permet de donner l'accélération d'un type de train en fonction de sa vitesse actuelle.
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
    f = 0.5 # le freinage de tous les trains
    if v >= train[4] :
        return (0,0.5) # on n'accélère pas au dessus de la vitesse limite du train
    else :
        while v >= M_v_e[i,0] : # on cherche dans quel intervalle la vitesse actuelle se situe
            i += 1
    a = (M_v_e[i-1,1] - RAV)/(train[0]*1000) # application du PFD
    return a,f


def temps_distance_acc(v_actuelle, v_consigne, train) :
    '''
    Permet de donner la durée et la distance nécessaires pour passer de la vitesse actuelle à la vitesse consigne pour un type de train.
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
        temps = i
    return temps,l/1000


def d_min(v_actuelle, v_lim1, v_lim2, train):
    '''
    Donne la distance minimale requise pour passer de la vitesse actuelle à la vitesse limite 2 en passant par la vitesse limite 1.
    Cette fonction a pour but d'être utilisée afin de savoir si il est utile d'accélérer jusqu'à la limite de vitesse avant de freiner pour arriver au prochain troncon.
    Entrées :
        v_actuelle = la vitesse actuelle du train (en km/h)
        v_lim1 = la vitesse limite sur le troncon dans lequel est le train actuellement (km/h)
        v_lim2 = la vitesse limite sur le prochain troncon (km/h)
        train = le type de train utilisé pour ce calcul
    Sortie :
        d_min = la distance minimale pour passer par v1 avant de passer à v2 (km)
    Remarque : on considère que v_actuelle <= v_lim1 car on respecte les limitaions de vitesse
    '''
    v_lim1 = min(v_lim1, train[4])
    v_lim2 = min(v_lim2, train[4])
    v_actuelle_m = v_actuelle/3.6
    v_lim1_m = v_lim1/3.6
    v_lim2_m = v_lim2/3.6
    a,f = acceleration(v_actuelle,train)
    if v_lim1 > v_lim2 :
        d_min = (v_lim1_m**2 - v_lim2_m**2)/(2*f) + temps_distance_acc(v_actuelle, v_lim1, train)[1]*1000
        # la distance pour accélérer de v_actuelle à v_lim1 puis pour freiner de v_lim1 à v_lim2
        return d_min/1000
    else:
        raise ValueError('v_lim2 > v_lim1')


def transition_troncon(v_actuelle, v_troncon1, v_troncon2, l_troncon, train) :
    '''
    Calcule le temps mis par le train pour parcourir le troncon.
    Entrées :
        v_actuelle = la vitesse actuelle du train (km/h)
        v_troncon1 = la vitesse du troncon dans lequel le train est (km/h)
        v_troncon2 = la vitesse du prochain troncon (km/h)
        l_troncon = la longueur du troncon (km)
        train = le type de train qui parcourt ce troncon
    Sorties :
        temps = le temps mis par le train pour parcourir le troncon
        v_sortie = la vitesse de sortie du troncon 1
    Remarque : la question de "l'éco-conduite" n'est pas prise en compte ici, on essaie d'aller le plus vite possible
    '''
    v_troncon1 = min(v_troncon1, train[4])
    v_troncon2 = min(v_troncon2, train[4])
    v_actuelle_m = v_actuelle/3.6
    v_troncon1_m = v_troncon1/3.6
    v_troncon2_m = v_troncon2/3.6
    a,f = acceleration(v_actuelle, train)
    if v_troncon1 > v_troncon2 :
        d_m = d_min(v_actuelle, v_troncon1, v_troncon2, train)
        if l_troncon >= d_m : # la vitesse limite est atteignable car la longueur du troncon est plus grande que d_min calculé précedemment
            temps = (v_troncon1_m - v_troncon2_m)/f # le temps qu'il faut pour freiner de la v_troncon1 à v_troncon2
            ta, la = temps_distance_acc(v_actuelle, v_troncon1, train)
            temps += ta # temps pour accélérer de v_actuelle jusqu'à v_troncon1
            temps += (l_troncon*1000 - la*1000 - (v_troncon1_m**2 - v_troncon2_m**2)/f)/v_troncon1_m # le temps passé à v_troncon1
            v_sortie= v_troncon2
        else :
            # on ne peut pas attteindre la vitesse limite donc on cherche à quelle vitesse on peut aller au maximum
            v_max_atteinte = v_actuelle
            t_acc, d_acc = temps_distance_acc(v_actuelle, v_max_atteinte, train)
            d_parcourue = partie_positive((v_max_atteinte**2 - v_troncon2_m**2)/2*f) + d_acc*1000
            # distance d'accélération de v_actuelle à v_max_atteinte puis freinage de v_max_atteinte à v_troncon2 (si c'est positif donc si v_max_atteinte > v_troncon2)
            while d_parcourue < l_troncon*1000 and v_max_atteinte <= train[4]-1:
                # itérations pour ttrouver la vitesse maximale atteinte
                v_max_atteinte += 1
                t_acc, d_acc = temps_distance_acc(v_actuelle, v_max_atteinte, train)
                d_parcourue = ((v_max_atteinte/3.6)**2 - v_troncon2_m**2)/2*f + d_acc*1000 # en mètre
                temps = t_acc + partie_positive((v_max_atteinte/3.6 - v_troncon2_m)/f)
                v_sortie = min(v_troncon2, v_max_atteinte)
    else :
        if temps_distance_acc(v_actuelle, v_troncon1, train)[1] > l_troncon :
            # on ne peut pas atteindre v_tronçon1 donc on cherche la vitesse maximale atteignable
            v_max_atteinte = v_actuelle # v_max_atteinte en km/h
            t_acc, d_acc = temps_distance_acc(v_actuelle, v_max_atteinte, train)
            d_parcourue = d_acc*1000 # en mètre
            while d_parcourue < l_troncon*1000 :
                v_max_atteinte += 1 # en km/h
                t_acc, d_acc = temps_distance_acc(v_actuelle, v_max_atteinte, train)
                if v_max_atteinte > v_troncon2:
                    d_parcourue = d_acc + ((v_max_atteinte/3.6)**2 - v_troncon2_m**2)/(2*0.5)
                else:
                    d_parcourue = d_acc*1000 # en mètre
            temps = t_acc
            v_sortie = v_max_atteinte
        else :
            # on peut atteindre v_troncon1
            t_acc, d_acc = temps_distance_acc(v_actuelle, v_troncon1, train)
            temps = t_acc + (l_troncon - d_acc)*1000/v_troncon1_m
            v_sortie = v_troncon1
    return temps, v_sortie

def min_to_format(min):
    return str(round(min//60,0)) + " h " + str(round(min%60,0))

def temps_parcours_ligne(ligne, train, min_depart, gares_desservies, sens_troncons):
    '''
    Calclue le temps de parcour d'une ligne pour un type de train.
    Entrées :
        ligne : la ligne considérée
        train : le type de train considéré
        min_depart : la minute de départ du train
        gares_desservies : liste des gares desservies sur la ligne
    Sortie :
        heures : la liste des temps d'arrivée à chaque noeud qui constitue la ligne (en mn)
        distances : la distance totale parcourue entre les noeuds (en km)
    Remarque : si on a un arrêt en gare, on duplique le noeud et on rajoute 2mn
    '''
    noeuds = []
    temps_parcours = min_depart
    d_cumulee = 0
    if ligne[0] == l49 :
        v_sortie = 140
        heures = [temps_parcours]
        distances = [d_cumulee]
    elif ligne[0] == l28bis:
        v_sortie = 160
        heures = [temps_parcours]
        distances = [d_cumulee]
    else :
        v_sortie = 0
        heures = [temps_parcours - 10, temps_parcours]
        distances = [d_cumulee]*2
        if sens_troncons[0]:
            noeuds.append(ligne[0][0])
        else :
            noeuds.append(ligne[0][1])

    if sens_troncons[0]:
        noeuds.append(ligne[0][0])
    else :
        noeuds.append(ligne[0][1])
    for i in range(len(ligne)): # Pour chaque tronçon de la ligne
        ti = ligne[i] # Tronçon i
        if i != len(ligne)-1: # Si ce n'est pas le dernier tronçon
            if (sens_troncons[i] and ti[1] in gares_desservies) or (not(sens_troncons[i]) and ti[0] in gares_desservies): # Si une gare est desservie

                # Passage du tronçon
                temps_s, v_sortie = transition_troncon(v_sortie, ti[2], 0, ti[3], train)
                d_cumulee += ti[3]
                temps_parcours += temps_s/60

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

                # Arrêt en gare
                if (sens_troncons[i] and ti[1] == 'Lyon') or (not(sens_troncons[i]) and ti[0] == 'Lyon'):
                    temps_parcours += 6 # min
                else :
                    temps_parcours += 2 # min

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

                if sens_troncons[i]:
                    noeuds.append(ti[1])
                    noeuds.append(ti[1])
                else :
                    noeuds.append(ti[0])
                    noeuds.append(ti[0])

            else: # Si aucune gare n'est desservie

                ti1 = ligne[i+1] # on va avoir besoin de la vitesse limite suivante

                # Passage du tronçon
                temps_s, v_sortie = transition_troncon(v_sortie, ti[2], ti1[2], ti[3], train)
                temps_parcours += temps_s/60
                d_cumulee += ti[3]

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

                if sens_troncons[i]:
                    noeuds.append(ti[1])
                else :
                    noeuds.append(ti[0])

        else : # Pour le dernier tronçon

            if ligne[i] == l49 or ligne[0] == l28bis : # si on sort des lignes ter vers les lgv par le nord ou le sud
                temps_s, v_sortie = transition_troncon(v_sortie, ti[2], 200, ti[3], train)

                if sens_troncons[i]:
                    noeuds.append(ti[1])
                else :
                    noeuds.append(ti[0])

                # Passage du dernier tronçon
                temps_parcours += temps_s/60
                d_cumulee += ti[3]

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

            else : # si ce n'est pas une desserte tgv dans le sens de la ligne tgv
                temps_s, v_sortie = transition_troncon(v_sortie, ti[2], 0, ti[3], train)

                # Passage du dernier tronçon
                temps_parcours += temps_s/60
                d_cumulee += ti[3]

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

                temps_parcours += 10 # min

                # Maj des données
                heures.append(math.ceil(temps_parcours))
                distances.append(d_cumulee)

                if sens_troncons[i]:
                    noeuds.append(ti[1])
                    noeuds.append(ti[1])
                else :
                    noeuds.append(ti[0])
                    noeuds.append(ti[0])

    return heures, distances, noeuds

def min_format(min):
    """
     X min => X//60 h X%60
    """
    return str(int(min//60)) + " h " + str(int(min%60))

def entree_sortie_troncon(heures, l_distances, ligne):
    '''Connaitre les heures d'entrée et de sortie de chaque tronçon pour une ligne donnée
    Entrées:
    ligne = [troncon 1, troncon 2,..., troncon n]
    distances = [0, d1, d2, d2, d3,..., dn], on met 2 fois la même distance s'il y a une gare car le train ne bouge pas
    heures = [0, heure 1, heure 2, heure 2 +2min, heure 3,..., heure n], lorsque le train passe par une gare il y a une pause de 2min

    Sorties :
    '''
    horaires =[]
    for k in range(0,len(l_distances)-1) :
        if l_distances[k] != l_distances[k+1]:
            horaires.append([heures[k], heures[k+1]])
    L=[ligne,horaires]
    return L