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


def Ajout_train(lignes, lignesOK, trains):
    '''

    '''
    ind_ligne = rd.randint(0, len(lignes)-1)
    while lignesOK[ind_ligne] :
        ind_ligne = rd.randint(0, len(lignes)-1)
    h_depart = rd.randint(0,59)