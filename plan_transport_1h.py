#-------------------------------------------------------------------------------
# Name:        plan transport 1h
# Purpose:
#
# Author:      barbier lucas
#
# Created:     02/05/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random as rd
from Carac_trains import *
from acceleration_train import *
from donnees_lignes import *


def Ajout_train(plan, lignesOK):
    '''

    '''
    if all(lignesOK):
        return plan
    else :
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        while lignesOK[ind_ligne] :
            ind_ligne = rd.randint(0, len(lignesOK)-1)
        ligne_etudiee = plan[0][ind_ligne]
        if ligne_etudiee in [TGV_MâconLochéTGV_Lyon, TGV_MâconLochéTGV_Sud, TGV_Sud_Lyon]:
            train_utilise = tgv
        elif ligne_etudiee[1] == False :
            train_utilise = Ter_autorail
        else :
            train_utilise = rd.choice([Ter_2n, Ter_regiolis])
        for _ in range(100):
            h_depart = rd.randint(0,59)
            plan[1][ind_ligne] = h_depart
            plan[2][ind_ligne] = "gares desservies"
            plan[3][ind_ligne] = train_utilise
            if verif_plan_1h(plan) :
                lignesOK[ind_ligne] = True
                return Ajout_train(plan, lignesOK)
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        while not(lignesOK[ind_ligne]) :
            ind_ligne = rd.randint(0, len(lignesOK)-1)
        plan[1][ind_ligne] = 0
        plan[2][ind_ligne] = ""
        plan[3][ind_ligne] = 0
        lignesOK[ind_ligne] = False
        return Ajout_train(plan, lignesOK)

def verif_plan_1h(plan, troncons_verif):
    """

    """
    for t in troncons_verif:
        occupation = Pile()
        for m in range(60):