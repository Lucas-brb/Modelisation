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
        label_l = plan[0][ind_ligne]
        if plan[0][ind_ligne] == ligne : # si c'est la même ligne parcourue dans le même sens

            # on ajoute la liste des heures et distances dans la variable d'affichage
            aff.append([plan[2][ind_ligne], plan[1][ind_ligne], label_l, couleurs_lignes[ligne]])

        elif troncons_lignes[plan[0][ind_ligne]][0] == list(reversed(troncons[0])) : # si c'est la même ligne dans l'autre sens

            # on prend la distance totale pour pouvoir afficher dans le bon sens
            dist_tot = plan[1][ind_ligne][-1]
            km_parcourus = []

            # on prend les km dans le sens décroissant
            for dist in plan[1][ind_ligne] :
                km_parcourus.append(dist_tot - dist)
            aff.append([plan[2][ind_ligne], km_parcourus, label_l, couleurs_lignes[ligne]])
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
                        '''
                        aff.append([[heure_e, heure_s], dist_cor_troncons[ind_t_commun], label_l, couleurs_lignes[plan[0][ind_ligne]]])
                        '''
                    else: # si il n'est pas parcouru dans le même sens

                        # on inverse les distances

                        aff_temp0 = [heure_e, heure_s] + aff_temp0
                        aff_temp1 = [dist_cor_troncons[ind_t_commun][1], dist_cor_troncons[ind_t_commun][0]] + aff_temp1
                        '''
                        aff.append([[heure_e, heure_s], list(reversed(dist_cor_troncons[ind_t_commun])), label_l, couleurs_lignes[plan[0][ind_ligne]]])
                        '''
            if len(aff_temp0) != 0:
                aff.append([aff_temp0, aff_temp1, label_l, couleurs_lignes[plan[0][ind_ligne]]])
    axes = plt.axes()
    for t in aff :
        plt.plot(t[0], t[1], label = t[2], color = t[3])
    plt.axhline(y = 0 , linestyle = '--', color = 'grey', linewidth = 0.5)
    for w in dist_cor_troncons:
        plt.axhline(y = w[1], linestyle = '--', color = 'grey', linewidth = 0.5)
    distances, gares = dist_noeuds_ligne(troncons[0], troncons[1])
    axes.set_yticks(distances)
    axes.set_yticklabels(gares)
    axes.set_xticks([(k+6)*60 for k in range(18)])
    axes.set_xticklabels(['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'])
    plt.xticks(rotation = 90)
    plt.show()
    plt.grid(visible = True, color = 'grey', linewidth = 0.1, linestyle = '--')
    plt.close()