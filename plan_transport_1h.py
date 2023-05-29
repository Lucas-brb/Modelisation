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

plan = [list(troncons_lignes.keys())]
plan.append([0 for i in range(len(plan[0]))])
plan.append([-1 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
lignesOK = [False for i in range(len(plan[0]))]

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
        nom_ligne = plan[0][ind_ligne]
        ligne_etudiee = troncons_lignes[nom_ligne]
        if troncons_lignes[ligne_etudiee][0] in [TGV_MâconLochéTGV_Lyon[0], TGV_MâconLochéTGV_Sud[0], TGV_Sud_Lyon[0]]:
            train_utilise = tgv
        elif ligne_etudiee[2] == False :
            train_utilise = Ter_autorail
        else :
            train_utilise = rd.choice([Ter_2n, Ter_regiolis])
        for _ in range(100):
            h_depart = rd.randint(0,59)
            heures, distances = temps_parcours_ligne(troncons_lignes[ligne_etudiee][0],train_utilise,h_depart,'gares desservies')
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
    h_entree, h_sortie = [],[]
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1:
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne
                t_entree, t_sortie = entree_sortie_troncon(plan[1][ligne], plan[2][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
                h_entree.append(t_entree)
                h_sortie.append(t_sortie)
                heures_passage.append([t_entree, t_sortie, troncons_lignes[plan[0][ligne]][1][ind_t]])
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))
    #heures_passage = np.array(heures_passage)
    #heures_passage[heures_passage[:,0].argsort()] # on trie le tableau par heure d'entrée croissante
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)):
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
                if len(Occupation) != 0:
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
    h_entree, h_sortie = [], []
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1:
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne
                t_entree, t_sortie = entree_sortie_troncon(plan[1][ligne], plan[2][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
                h_entree.append(t_entree)
                h_sortie.append(t_sortie)
                heures_passage.append([t_entree, t_sortie, troncons_lignes[plan[0][ligne]][1][ind_t]])
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))
    #heures_passage = np.array(heures_passage)
    #heures_passage[heures_passage[:,0].argsort()] # on trie le tableau par heure d'entrée croissante
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)):
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
                elif ind_train in Occupation2 :
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
    h_entree, h_sortie = [], []
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1:
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne
                t_entree, t_sortie = entree_sortie_troncon(plan[1][ligne], plan[2][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
                h_entree.append(t_entree)
                h_sortie.append(t_sortie)
                heures_passage.append([t_entree, t_sortie, troncons_lignes[plan[0][ligne]][1][ind_t]])
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))
    #heures_passage = np.array(heures_passage)
    #heures_passage[heures_passage[:,0].argsort()] # on trie le tableau par heure d'entrée croissante
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)):
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
                elif len(Occupation3) != 0:
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
    h_entree, h_sortie = [], []
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1:
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne
                t_entree, t_sortie = entree_sortie_troncon(plan[1][ligne], plan[2][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
                h_entree.append(t_entree)
                h_sortie.append(t_sortie)
                heures_passage.append([t_entree, t_sortie, troncons_lignes[plan[0][ligne]][1][ind_t]])
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))
    #heures_passage = np.array(heures_passage)
    #heures_passage[heures_passage[:,0].argsort()] # on trie le tableau par heure d'entrée croissante
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)):
            if heures_passage[ind_train][0] == t:
                if heures_passage[ind_train][2] :
                    if len(Occupation1) == 0:
                        Occupation1.append(ind_train)
                    # si les trains ne sont pas assez espacés à l'entrée et à la sortie
                    elif heures_passage[ind_train][1] - heures_passage[Occupation1[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation1[-1]][0] < 4:
                        if len(Occupation2) == 0:
                            Occupation2.append(ind_train)
                        # si les trains ne sont pas assez espacés sur la 2è voie
                        elif heures_passage[ind_train][1] - heures_passage[Occupation2[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation2[-1]][0] < 4:
                            return False
                        else :
                            Occupation2.append(ind_train)
                    else : # si les trains sont assez espacés
                        Occupation1.append(ind_train)
                else :
                    if len(Occupation3) == 0:
                        Occupation3.append(ind_train)
                    elif heures_passage[ind_train][1] - heures_passage[Occupation3[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1]][0] < 4:
                        if len(Occupation4) == 0:
                            Occupation4.append(ind_train)
                        # si les trains ne sont pas assez espacés
                        elif heures_passage[ind_train][1] - heures_passage[Occupation3[-1]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation3[-1]][0] < 4:
                            return False
                        else :
                            Occupation4.append(ind_train)
                    else :
                        Occupation3.append(ind_train)
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
                elif ind_train in Occupation3:
                    if Occupation3[0] != ind_train:
                        return False
                    else :
                        del Occupation3[0]
                elif ind_train in Occupation4 :
                    if Occupation4[0] != ind_train:
                        return False
                    else :
                        del Occupation4[0]
    return True

def verif_plan_1h(plan):
    """
    """
    h_arrivee = [heures[-1] for heures in plan[2] if heures != -1]
    h_max = int(max(h_arrivee))
    _troncons_verif = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l22bis, l23, l24, l25, l26, l27, l27bis, l28, l28bis, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, l61]
    for t in _troncons_verif:
        if t[-1] == 1:
            if not(verif_troncon_1voie(plan, t, h_max)):
                return False
        elif t[-1] == 2:
            if not(verif_troncon_2voies(plan, t, h_max)):
                return False
        elif t[-1] == 3:
            if not(verif_troncon_3voies(plan, t, h_max)):
                return False
        else :
            if not(verif_troncon_4voies(plan, t, h_max)):
                return False
    return True