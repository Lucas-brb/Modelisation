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

"""
plan = [
[liste des lignes]
[liste distance par ligne]
[liste des heures]
[liste gares dseesrvied]
[liste trains utilisés]
]
"""
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
            heures, distances = temps_parcours_ligne(ligne_etudiee,train_utilise,h_depart,'gares desservies')
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures
            plan[3][ind_ligne] = "gares desservies"
            plan[4][ind_ligne] = train_utilise
            if verif_plan_1h(plan) :
                lignesOK[ind_ligne] = True
                return Ajout_train(plan, lignesOK)
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        while not(lignesOK[ind_ligne]) :
            ind_ligne = rd.randint(0, len(lignesOK)-1)
        plan[1][ind_ligne] = -1
        plan[2][ind_ligne] = -1
        plan[3][ind_ligne] = ""
        plan[4][ind_ligne] = 0
        lignesOK[ind_ligne] = False
        return Ajout_train(plan, lignesOK)

def verif_troncon_1voie(plan, troncon_verif, h_max):
    """
    """
    Occupation = []
    heures_passage = []
    for ligne in range(len(plan[0])):
        if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
            ind_t = troncons_lignes[plan[0][ligne]][0] # on recherche l'indice du tronçon dans la ligne
            heures_passage.append(entree_sortie_troncon(plan[1][ligne], plan[2][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t] + [troncons_lignes[plan[0][ligne]][1]])
            heures_passage = np.array(heures_passage)
            heures_passage[heures_passage[:,0].argsort()] # on trie le tableau par heure d'entrée croissante
    for t in range(h_max+1):
        for ind_train in range(len(heures_passage[:,0])):
            if heures_passage[ind_train][0] == t:
                if len(Occupation) == 0:
                    Occupation.append([ind_train, heures_passage[ind_train][2]])
                else :
                    if Occupation[-1][1] == heures_passage[ind_train][2]: # les deux trains sur le tronçon vont bien dans le même sens
                        # si les trains ne sont pas assez espacés
                        if heures_passage[ind_train][1] - heures_passage[Occupation[0]][1] < 2 or heures_passage[ind_train][0] - heures_passage[Occupation[0]][0] < 2:
                            return False
                        else :
                            Occupation.append([ind_train, heures_passage[ind_train][2]])
                    else :
                        return False
            elif heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train != Occupation[0][0]: # ce n'est pas le premier train qui est rentré qui ressort : rattrapage
                    return False
                else :
                    del Occupation[0] # le train est sorti du tronçon
    return True

def verif_plan_1h(plan, troncons_verif):
    """
    """
    h_arrivee = [heures[-1] for heures in plan[2] if heures != -1]
    h_max = max(h_arrivee)
    for t in troncons_verif: