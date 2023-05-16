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
            plan[1][ind_ligne] = temps_parcours_ligne(ligne_etudiee,train_utilise,h_depart,'gares desservies')[0]
            plan[2][ind_ligne] = "gares desservies"
            plan[3][ind_ligne] = train_utilise
            if verif_plan_1h(plan) :
                lignesOK[ind_ligne] = True
                return Ajout_train(plan, lignesOK)
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        while not(lignesOK[ind_ligne]) :
            ind_ligne = rd.randint(0, len(lignesOK)-1)
        plan[1][ind_ligne] = -1
        plan[2][ind_ligne] = ""
        plan[3][ind_ligne] = 0
        lignesOK[ind_ligne] = False
        return Ajout_train(plan, lignesOK)

def verif_troncon_1voie(plan, troncon_verif, h_max):
    """
    """
    Occupation = File()
    lignes_regardees_pos = []
    lignes_regardees_neg = []
    for ligne in range(len(plan[0])):
        if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
            if troncons_lignes[plan[0][ligne]][1] == True:
                lignes_regardees_pos.append(ligne)
            else :
                lignes_regardees_neg.append(ligne)
    for t in range(h_max+1):


def verif_plan_1h(plan, troncons_verif):
    """
    """
    h_arrivee = [heures[-1] for heures in plan[1] if heures != -1]
    h_max = max(h_arrivee)
    for t in troncons_verif: