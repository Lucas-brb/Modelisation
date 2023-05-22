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
from donnees_lignes import *
from acceleration_train import *

"""
plan = [
[liste des lignes]
[liste distance par ligne]
[liste des heures]
[liste gares desservies]
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
                        if heures_passage[ind_train][1] - heures_passage[Occupation[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation[-1][0]][0] < 4:
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

def verif_troncon_2voies(plan, troncon_verif, h_max):
    """
    """
    Occupation1 = []
    Occupation2 = []
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
                if heures_passage[ind_train][2] :
                    if len(Occupation1) == 0:
                        Occupation1.append(ind_train)
                    # si les trains sont assez espacés à l'entrée et à la sortie
                    elif heures_passage[ind_train][1] - heures_passage[Occupation1[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation1[-1]][0] < 4:
                        return False
                    else :
                        Occupation1.append(ind_train)
                else :
                    if len(Occupation2) == 0:
                        Occupation2.append(ind_train)
                    elif heures_passage[ind_train][1] - heures_passage[Occupation2[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation2[-1]][0] < 4:
                        return False
                    else :
                        Occupation2.append(ind_train)
            elif heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1:
                    if Occupation1[0] != ind_train:
                        return False
                    else :
                        del Occupation1[0]
                else :
                    if Occupation2[0] != ind_train:
                        return False
                    else :
                        del Occupation2[0]
    return True

def verif_troncon_3voies(plan, troncon_verif, h_max):
    """
    """
    Occupation1 = []
    Occupation2 = []
    Occupation3 = []
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
                if heures_passage[ind_train][2] :
                    if len(Occupation1) == 0:
                        Occupation1.append(ind_train)
                    # si les trains ne sont pas assez espacés à l'entrée et à la sortie
                    elif heures_passage[ind_train][1] - heures_passage[Occupation1[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation1[-1]][0] < 4:
                        if len(Occupation3) == 0:
                            Occupation3.append([ind_train, heures_passage[ind_train][2]])
                        elif Occupation3[-1][1] == heures_passage[ind_train][2]: # les deux trains sur le tronçon vont bien dans le même sens
                        # si les trains ne sont pas assez espacés
                            if heures_passage[ind_train][1] - heures_passage[Occupation3[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1][0]][0] < 4:
                                return False
                            else :
                                Occupation3.append([ind_train, heures_passage[ind_train][2]])
                    else : # si les trains sont assez espacés
                        Occupation1.append(ind_train)
                else :
                    if len(Occupation2) == 0:
                        Occupation2.append(ind_train)
                    elif heures_passage[ind_train][1] - heures_passage[Occupation2[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation2[-1]][0] < 4:
                        if len(Occupation3) == 0:
                            Occupation3.append([ind_train, heures_passage[ind_train][2]])
                        elif Occupation3[-1][1] == heures_passage[ind_train][2]: # les deux trains sur le tronçon vont bien dans le même sens
                        # si les trains ne sont pas assez espacés
                            if heures_passage[ind_train][1] - heures_passage[Occupation3[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1][0]][0] < 4:
                                return False
                            else :
                                Occupation3.append([ind_train, heures_passage[ind_train][2]])
                    else :
                        Occupation2.append(ind_train)
            elif heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1:
                    if Occupation1[0] != ind_train:
                        return False
                    else :
                        del Occupation1[0]
                elif ind_train in Occupation2:
                    if Occupation2[0] != ind_train:
                        return False
                    else :
                        del Occupation2[0]
                else :
                    if Occupation3[0][0] != ind_train:
                        return False
                    else :
                        del Occupation3[0]
    return True

def verif_troncon_4voies(plan, troncon_verif, h_max):
    """
    """
    Occupation1 = []
    Occupation2 = []
    Occupation3 = []
    Occupation4 = []
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
                if heures_passage[ind_train][2] :
                    if len(Occupation1) == 0:
                        Occupation1.append(ind_train)
                    # si les trains ne sont pas assez espacés à l'entrée et à la sortie
                    elif heures_passage[ind_train][1] - heures_passage[Occupation1[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation1[-1]][0] < 4:
                        if len(Occupation3) == 0:
                            Occupation3.append([ind_train, heures_passage[ind_train][2]])
                        elif Occupation3[-1][1] == heures_passage[ind_train][2]: # les deux trains sur le tronçon vont bien dans le même sens
                        # si les trains ne sont pas assez espacés
                            if heures_passage[ind_train][1] - heures_passage[Occupation3[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1][0]][0] < 4:
                                return False
                            else :
                                Occupation3.append([ind_train, heures_passage[ind_train][2]])
                    else : # si les trains sont assez espacés
                        Occupation1.append(ind_train)
                else :
                    if len(Occupation2) == 0:
                        Occupation2.append(ind_train)
                    elif heures_passage[ind_train][1] - heures_passage[Occupation2[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation2[-1]][0] < 4:
                        if len(Occupation3) == 0:
                            Occupation3.append([ind_train, heures_passage[ind_train][2]])
                        elif Occupation3[-1][1] == heures_passage[ind_train][2]: # les deux trains sur le tronçon vont bien dans le même sens
                        # si les trains ne sont pas assez espacés
                            if heures_passage[ind_train][1] - heures_passage[Occupation3[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1][0]][0] < 4:
                                return False
                            else :
                                Occupation3.append([ind_train, heures_passage[ind_train][2]])
                    else :
                        Occupation2.append(ind_train)
            elif heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1:
                    if Occupation1[0] != ind_train:
                        return False
                    else :
                        del Occupation1[0]
                elif ind_train in Occupation2:
                    if Occupation2[0] != ind_train:
                        return False
                    else :
                        del Occupation2[0]
                else :
                    if Occupation3[0][0] != ind_train:
                        return False
                    else :
                        del Occupation3[0]
    return True

def verif_plan_1h(plan):
    """
    """
    h_arrivee = [heures[-1] for heures in plan[2] if heures != -1]
    h_max = max(h_arrivee)
    for t in _troncons_verif:
        if t[-1] == 1:
            if not(verif_troncon_1voie(plan, t, h_max)):
                return False
        elif t[-1] == 2:
            if not(verif_troncon_2voies(plan, t, h_max)):
                return False
    return True