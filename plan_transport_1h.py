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


def Ajout_train(lignes, lignesOK):
    '''

    '''
    if not(all(lignesOK)):
        ind_ligne = rd.randint(0, len(lignes)-1)
        while lignesOK[ind_ligne] :
            ind_ligne = rd.randint(0, len(lignes)-1)
        ligne_etudiee = lignes[ind_ligne]
        if ligne_etudiee in [TGV_MâconLochéTGV_Lyon, TGV_MâconLochéTGV_Sud, TGV_Sud_Lyon]:
            train_utilise = tgv
        elif ligne_etudiee[1] == False :
            train_utilise = Ter_autorail
        else :
            train_utilise = rd.choice([Ter_2n, Ter_regiolis])
        for _ in range(100):
            h_depart = rd.randint(0,59)
            if verif_plan :
                break
