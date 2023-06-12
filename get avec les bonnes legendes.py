#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      barbier lucas
#
# Created:     31/05/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from donnees_lignes import *
from plan_transport_1h import *
from Carac_trains import *
from plan_fonctionnel import *

def g_e_t(ligne, plan):
    """
    Donne le GET d'une ligne ou portion de ligne
    Entrees :
        ligne = la ligne considérée
        plan = le plan de transport dont on veut tracer le GET
    Sortie :
        représentation visuelle du GET
    """
    plt.close()
    troncons  = troncons_lignes[ligne]
    km = 0
    dist_cor_troncons = []
    for t in troncons[0]:
        dist_cor_troncons.append([km, km + t[3]])
        km += t[3]
    aff = [] # on crée la liste de tous les trajets à afficher sur le get
    # on cherche dans toutes les lignes lesquelles correspondent à celle qu'on considère (quelque soit le sens) ou celles qui ont des tronçons en commun avec la ligne considérée
    for ind_ligne in range(len(plan[0])) :
        if plan[0][ind_ligne] == ligne : # si c'est la même ligne parcourue dans le même sens

            # on ajoute la liste des heures et distances dans la variable d'affichage
            aff.append([plan[2][ind_ligne], plan[1][ind_ligne], couleurs_lignes[ligne]])

        elif troncons_lignes[plan[0][ind_ligne]][0] == list(reversed(troncons[0])) : # si c'est la même ligne dans l'autre sens

            # on prend la distance totale pour pouvoir afficher dans le bon sens
            dist_tot = plan[1][ind_ligne][-1]
            km_parcourus = []

            # on prend les km dans le sens décroissant
            for dist in plan[1][ind_ligne] :
                km_parcourus.append(dist_tot - dist)
            aff.append([plan[2][ind_ligne], km_parcourus, couleurs_lignes[ligne]])
        else :
            # si la ligne est différente, on cherche si elle a des tronçons en commun avec celle dont on veut tracer le get
            aff_temp0 = []
            aff_temp1 = []
            for ind_t_commun in range(len(troncons[0])) : # on parcours les tronçons de la ligne du get
                if troncons[0][ind_t_commun] in troncons_lignes[plan[0][ind_ligne]][0]: # si le tronçon est aussi dans la liste des tronçons de la ligne considérée

                    # recuperation de l'indice du tronçon dans la ligne considérée
                    i_t_ligneetuidee = troncons_lignes[plan[0][ind_ligne]][0].index(troncons[0][ind_t_commun])

                    # on prend le tronçon commun
                    troncon_commun = troncons_lignes[plan[0][ind_ligne]][0][i_t_ligneetuidee]

                    #on prend les heures d'entrée et sortie de ce tronçon sur cette ligne
                    heure_e, heure_s = entree_sortie_troncon(plan[2][ind_ligne], plan[1][ind_ligne], plan[0][ind_ligne])[1][i_t_ligneetuidee]

                    if troncons_lignes[plan[0][ind_ligne]][1][i_t_ligneetuidee] == troncons[1][ind_t_commun]: # si le tronçon est parcouru dans le même sens que le tronçon de la ligne get

                        # on ajoute les heures et les distances dans le même sens

                        aff_temp0.append(heure_e)
                        aff_temp0.append(heure_s)
                        aff_temp1.append(dist_cor_troncons[ind_t_commun][0])
                        aff_temp1.append(dist_cor_troncons[ind_t_commun][1])

                    else: # si il n'est pas parcouru dans le même sens

                        # on inverse les distances

                        aff_temp0 = [heure_e, heure_s] + aff_temp0
                        aff_temp1 = [dist_cor_troncons[ind_t_commun][1], dist_cor_troncons[ind_t_commun][0]] + aff_temp1

            if len(aff_temp0) != 0:
                aff.append([aff_temp0, aff_temp1, couleurs_lignes[plan[0][ind_ligne]]])
    axes = plt.axes()
    for t in aff :
        plt.plot(t[0], t[1], color = t[2], linewidth = 0.85)
    plt.axhline(y = 0 , linestyle = '--', color = 'grey', linewidth = 0.5)
    for w in dist_cor_troncons:
        plt.axhline(y = w[1], linestyle = '--', color = 'grey', linewidth = 0.5)
    for _ in range(6*60,24*60,2):
        plt.axvline(x = _, linestyle = '--', color = 'grey', linewidth = 0.4)
    distances, gares = dist_noeuds_ligne(troncons[0], troncons[1])
    axes.set_yticks(distances)
    axes.set_yticklabels(gares)
    axes.set_xticks([k*60 for k in range(6,23)])
    axes.set_xticklabels(['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00'])
    plt.xticks(rotation = 90)
    lignes_legende = ['Lyon-Roanne', 'Roanne-Saint-Etienne', 'Lyon-Saint-Etienne', 'Lyon-Mâcon', 'Lyon-Valence', 'Lyon-Grenoble', 'Valence-Grenoble', 'Grenoble-Chambéry', 'Chambéry-Annecy', 'Lyon-Bourg-En-Bresse', 'Mâcon-Bourg-En-Bresse','Lyon-Chambéry', 'Lyon-Annecy', 'TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble']
    colors = ['red', 'green', 'purple', 'springgreen', 'cyan', 'deepskyblue', 'blueviolet', 'gold', 'magenta', 'hotpink', 'navy', 'teal', 'sienna', 'orange', 'olive', 'black', 'blue']


    # Parcourir les étiquettes et les couleurs et les ajouter à la légende
    handles_l = []
    for label, color in zip(lignes_legende, colors):
        line, = axes.plot([], [], label = label, color = color)
        handles_l.append(line)

    # Obtenir la légende
    plt.legend(handles = handles_l, loc = 'upper left', bbox_to_anchor = (1, 1), numpoints = len(lignes_legende))
    plt.subplots_adjust(right = 0.7)

    plt.title("GET %s" % ligne)
    plt.xlabel("Heures")
    plt.ylabel("Noeuds")
    # plt.xlim(18*60,22*60)
    plt.show()
    plt.close()

g_e_t('Annecy-Chambéry', plan_final)
g_e_t('Lyon-Grenoble', plan_final)
g_e_t('Lyon-nord', plan_final)
g_e_t('Lyon-sud', plan_final)