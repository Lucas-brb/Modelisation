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

Ajout_train(plan,lignesOK)

def g_e_t(ligne, plan):
    plt.close()
    troncons  = troncons_lignes[ligne]
    km = 0
    dist_cor_troncons = []
    for t in troncons[0]:
        dist_cor_troncons.append([km, km + t[3]])
        km += t[3]
    aff = []
    for ind_ligne in range(len(plan[0])) :
        if plan[0][ind_ligne] == ligne :
            aff.append([plan[2][ind_ligne], plan[1][ind_ligne]])
        elif troncons_lignes[plan[0][ind_ligne]][0] == list(reversed(troncons[0])) :
            dist_tot = plan[1][ind_ligne][-1]
            km_parcourus = []
            for dist in plan[1][ind_ligne] :
                km_parcourus.append(dist_tot - dist)
            aff.append([plan[2][ind_ligne], km_parcourus])
        else :
            troncons_communs = [commun for commun in troncons[0] if commun in troncons_lignes[plan[0][ind_ligne]][0]]
            # a continuer
    for t in aff :
        plt.plot(t[0], t[1])
    plt.show()

g_e_t(plan[0][0],plan)
"""
axes = plt.axes()
plt.plot(heures, distances)
gares = ['Roanne', 'Feurs', 'Saint Just Saint Rambert', 'Saint Etienne']
heures = ['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
axes.set_yticks([0, 42, 74, 88])
axes.set_xticks([k*60 for k in range(18)])
axes.set_yticklabels(gares)
axes.set_xticklabels(heures)
plt.xlim(0,17*60)
plt.xticks(rotation = 90)
plt.show()
time.sleep(1)
plt.close()
g_e_t(plan[0][0],plan)
"""