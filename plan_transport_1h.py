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
import copy

plan = [list(troncons_lignes.keys())]
#plan = [['Roanne-Lyon', 'Roanne-Saint-Etienne', 'Lyon-Saint-Etienne', 'Lyon-Macon', 'Lyon-Valence', 'Lyon-Grenoble', 'TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'Lyon-Roanne', 'StE-Roanne', 'StE-Lyon', 'Macon_Lyon', 'Valence-Lyon', 'Grenoble-Lyon', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']]
plan.append([0 for i in range(len(plan[0]))])
plan.append([-1 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
lignesOK = [False for i in range(len(plan[0]))]


def plus_petite_longueur(l):
    """
    """
    longueurs = []
    index = []
    for elt in l :
        longueurs.append(len(elt))
    long_min = min(longueurs)
    for _ in range(len(l)):
        if longueurs[_] == long_min:
            index.append(_)
    return index

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
    print(lignesOK)
    if all(lignesOK):
        return plan
    else :

        # on prend l'indice des lignes qui ne sont pas encore intégrées
        ind_lignes_nOK = [i for i in range(len(lignesOK)) if not(lignesOK[i])]

        # initialisation
        heures_possibles = [[] for _ in range(len(ind_lignes_nOK))]
        trains = []

        for ind_ligne in range(len(ind_lignes_nOK)) : # ind_ligne = indice dans ind_ligne_nOK
            plan_copie = copy.deepcopy(plan) # on n'interfère pas avec le vrai plan de transport
            ind_ligne_test = ind_lignes_nOK[ind_ligne] # ind_ligne_test = indice de la ligne dans le vrai plan de transport
            nom_ligne = plan[0][ind_ligne_test]
            ligne_etudiee = troncons_lignes[nom_ligne]
            if ligne_etudiee[0] in [TGV_Creusot_Lyon[0], TGV_Lyon_Marseille[0], TGV_Lyon_Montpellier[0], TGV_Lille_Grenoble[0]]:
                nom_train_utilise = 'TGV'
            elif ligne_etudiee[2] == False :
                nom_train_utilise = 'Autorail'
            else :
                nom_train_utilise = rd.choice(['2N', 'Regiolis'])
            train_utilise = noms_trains[nom_train_utilise]
            heures, distances = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
            for h_depart in range(60):
                heures_n = [h + h_depart for h in heures]
                plan_copie[1][ind_ligne_test] = distances
                plan_copie[2][ind_ligne_test] = heures_n
                plan_copie[3][ind_ligne_test] = '' # gares_desservables[nom_ligne]
                plan_copie[4][ind_ligne_test] = nom_train_utilise
                if verif_plan(plan_copie): # si on peut faire partir le train sur la ligne considérée à l'heure voulue
                    heures_possibles[ind_ligne].append(h_depart)
            trains.append(train_utilise)
        if any(len(x) == 0 for x in heures_possibles) : # un des trains ne peut pas partir avec ce plan de transport, bloqué
            ind_ligne = rd.randint(0, len(lignesOK)-1)
            if not(all(not(x) for x in lignesOK)):
                while not(lignesOK[ind_ligne]) :
                    ind_ligne = rd.randint(0, len(lignesOK)-1)
                plan[1][ind_ligne] = -1
                plan[2][ind_ligne] = -1
                plan[3][ind_ligne] = ""
                plan[4][ind_ligne] = ""
                lignesOK[ind_ligne] = False
        else :
            index = plus_petite_longueur(heures_possibles)
            i = rd.choice(index)
            ind_ligne = ind_lignes_nOK[i]
            nom_ligne = plan[0][ind_ligne]
            ligne_etudiee = troncons_lignes[nom_ligne]
            train_utilise = trains[i]
            h_depart = heures_possibles[i][0]
            heures, distances = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, gares_desservables[nom_ligne], ligne_etudiee[1])
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures
            plan[3][ind_ligne] = '' # gares_desservables[nom_ligne]
            plan[4][ind_ligne] = nom_train_utilise
            lignesOK[ind_ligne] = True
        return Ajout_train(plan, lignesOK)
        '''
        nb_iteration = len([1 for i in lignesOK if not(i)])
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        while lignesOK[ind_ligne] :
            ind_ligne = rd.randint(0, len(lignesOK)-1)
        nom_ligne = plan[0][ind_ligne]
        ligne_etudiee = troncons_lignes[nom_ligne]
        if ligne_etudiee[0] in [TGV_Creusot_Lyon[0], TGV_Lyon_Marseille[0], TGV_Lyon_Montpellier[0], TGV_Lille_Grenoble[0]]:
            train_utilise = tgv
        elif ligne_etudiee[2] == False :
            train_utilise = Ter_autorail
        else :
            train_utilise = rd.choice([Ter_2n, Ter_regiolis])
        heures, distances = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
        '''
        '''
        for _ in range(round(1000/(nb_iteration))):
            h_depart = rd.randint(0,59)
            heures_n = [h + h_depart for h in heures]
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures_n
            plan[3][ind_ligne] = '' # gares_desservables[nom_ligne]
            plan[4][ind_ligne] = train_utilise
            if verif_plan_1h(plan) :
                lignesOK[ind_ligne] = True
                return Ajout_train(plan, lignesOK)
            # ça n'a pas marché, on réinitialise
            plan[1][ind_ligne] = -1
            plan[2][ind_ligne] = -1
            plan[3][ind_ligne] = ""
            plan[4][ind_ligne] = 0
            lignesOK[ind_ligne] = False
        ind_ligne = rd.randint(0, len(lignesOK)-1)
        if not(all(not(x) for x in lignesOK)):
            while not(lignesOK[ind_ligne]) :
                ind_ligne = rd.randint(0, len(lignesOK)-1)
            plan[1][ind_ligne] = -1
            plan[2][ind_ligne] = -1
            plan[3][ind_ligne] = ""
            plan[4][ind_ligne] = 0
            lignesOK[ind_ligne] = False
        return Ajout_train(plan, lignesOK)
    '''

def verif_troncon_1voie(plan, troncon_verif):
    """
    """
    Occupation = []
    heures_passage = []
    h_entree, h_sortie = [],[]
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1:
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne
                t_entree, t_sortie = entree_sortie_troncon(plan[2][ligne], plan[1][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
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

def verif_troncon_2voies(plan, troncon_verif):
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
                t_entree, t_sortie = entree_sortie_troncon(plan[2][ligne], plan[1][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
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

def verif_troncon_3voies(plan, troncon_verif):
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
                t_entree, t_sortie = entree_sortie_troncon(plan[2][ligne], plan[1][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
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

def verif_troncon_4voies(plan, troncon_verif):
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
                t_entree, t_sortie = entree_sortie_troncon(plan[2][ligne], plan[1][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
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
                if heures_passage[ind_train][2] : # on parcourt le tronçon dans le sens positif
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

def verif_noeud(plan, noeud_verif, h_max):
    Occupation = []

def verif_plan(plan):
    """
    """
    _troncons_verif = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l22bis, l23, l24, l25, l26, l27, l27bis, l28, l28bis, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, l61]
    for t in _troncons_verif:
        if t[-1] == 1:
            if not(verif_troncon_1voie(plan, t)):
                return False
        elif t[-1] == 2:
            if not(verif_troncon_2voies(plan, t)):
                return False
        elif t[-1] == 3:
            if not(verif_troncon_3voies(plan, t)):
                return False
        else :
            if not(verif_troncon_4voies(plan, t)):
                return False
    return True