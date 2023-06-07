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

lignes_ter1 = ['Roanne-Lyon', 'Roanne-Saint-Etienne', 'Lyon-Saint-Etienne', 'Lyon-Macon', 'Lyon-Valence', 'Lyon-Grenoble', 'Valence-Grenoble', 'Lyon-Roanne', 'StE-Roanne', 'StE-Lyon', 'Macon_Lyon', 'Valence-Lyon', 'Grenoble-Lyon', 'Grenoble-Valence']
lignes_ter2 = ['Grenoble-Chambery', 'Chambery-Annecy', 'Lyon-Bourg-en-Bresse', 'Bourg-en-Bresse-Macon', 'Lyon-Chambery', 'Lyon-Annecy', 'Chambéry-Grenoble', 'Annecy-Chambéry', 'Bourg-en-Bresse-Lyon', 'Macon-Bourg-en-Bresse', 'Chambery-Lyon', 'Annecy-Lyon']
tgv_normal = ['TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']
tgv_pointe = tgv_normal*2

heures_pointe = [7, 8, 9, 12, 13, 14, 17, 18, 19]
indices_heures = []
indices_heures_initial = 0
plan = []
for _ in range(6, 23):
    if _ % 2 == 0:
        if _ in heures_pointe:
            desserte_heure = lignes_ter1 + tgv_pointe
        else:
            desserte_heure = lignes_ter1 + tgv_normal
    else :
        if _ in heures_pointe:
            desserte_heure = lignes_ter2 + tgv_pointe
        else:
            desserte_heure = lignes_ter2 + tgv_normal
    plan += desserte_heure
    indices_heures.append([indices_heures_initial, indices_heures_initial + len(desserte_heure)])
    indices_heures_initial += len(desserte_heure)
plan = [plan]

#plan = [list(troncons_lignes.keys())]
#plan = [['Roanne-Lyon', 'Roanne-Saint-Etienne', 'Lyon-Saint-Etienne', 'Lyon-Macon', 'Lyon-Valence', 'Lyon-Grenoble', 'TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'Lyon-Roanne', 'StE-Roanne', 'StE-Lyon', 'Macon_Lyon', 'Valence-Lyon', 'Grenoble-Lyon', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']]
plan.append([0 for i in range(len(plan[0]))])
plan.append([-1 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
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
    Permet d'ajouter un train à un plan de transport.
    Entrees :
        plan = le plan de transport actuel
        lignesOK = la liste des lignes qui sont déjà incluses dans le plan de transport
        (les indices avec le plan correspondent)
    Sortie :
        plan = le plan de transport fini
    Remarque : cette fonctnio est une fonction récursive.
    '''
    if all(lignesOK):
        return plan
    else :

        # on prend l'indice des lignes qui ne sont pas encore intégrées
        ind_lignes_nOK = [i for i in range(len(lignesOK)) if not(lignesOK[i])]
        print(len(ind_lignes_nOK))

        # initialisation
        heures_possibles = [[] for _ in range(len(ind_lignes_nOK))]
        trains = []

        for ind_ligne in range(len(ind_lignes_nOK)) : # ind_ligne = indice dans ind_ligne_nOK
            plan_copie = copy.deepcopy(plan) # on n'interfère pas avec le vrai plan de transport
            ind_ligne_test = ind_lignes_nOK[ind_ligne] # ind_ligne_test = indice de la ligne dans le plan de transport en entrée
            nom_ligne = plan[0][ind_ligne_test] # str
            ligne_etudiee = troncons_lignes[nom_ligne] # on prend la liste et l'orientation des tronçons qui constituent la ligne considérée.

            # si c'est un desserte TGV
            if nom_ligne in ['TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']:
                nom_train_utilise = 'TGV'

            # si la ligne n'est pas électrifiée
            elif ligne_etudiee[2] == False :
                nom_train_utilise = 'Autorail'
            else : # sinon, on prend au hasard entre les deux autres types de matériel
                nom_train_utilise = rd.choice(['2N', 'Regiolis'])

            # recuperation des caractéristiques techniques du train
            train_utilise = noms_trains[nom_train_utilise]

            # on calcule le temps mis par le train pour parcourir sa ligne
            heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])

            # on va tester sur toutes les minutes de la journée s'il est possible de faire démarrer le train à cette heure
            for h_depart in range(6*60, 22*60):
                heures_n = [h + h_depart for h in heures]
                plan_copie[1][ind_ligne_test] = distances
                plan_copie[2][ind_ligne_test] = heures_n
                plan_copie[3][ind_ligne_test] = gares_desservables[nom_ligne]
                plan_copie[4][ind_ligne_test] = nom_train_utilise
                plan_copie[5][ind_ligne_test] = noeuds_desservis
                if verif_plan(plan_copie): # si on peut faire partir le train sur la ligne considérée à l'heure voulue
                    heures_possibles[ind_ligne].append(h_depart)
            trains.append(nom_train_utilise)

        # si un des trains ne peut pas partir avec ce plan de transport, on est bloqués
        if any(len(x) == 0 for x in heures_possibles) :
            ind_ligne = rd.randint(0, len(lignesOK)-1)

            # on retire un élément au hasard du plan
            if not(all(not(x) for x in lignesOK)):
                while not(lignesOK[ind_ligne]) :
                    ind_ligne = rd.randint(0, len(lignesOK)-1)
                plan[1][ind_ligne] = -1
                plan[2][ind_ligne] = -1
                plan[3][ind_ligne] = ""
                plan[4][ind_ligne] = ""
                plan[5][ind_ligne] = 0
                lignesOK[ind_ligne] = False
        else : # si l'on n'est pas bloqués
            index = plus_petite_longueur(heures_possibles) # on récupère le liste des indices des listes de plus petite longueur dans heures_possibles
            i = rd.choice(index)
            ind_ligne = ind_lignes_nOK[i]
            nom_ligne = plan[0][ind_ligne]
            ligne_etudiee = troncons_lignes[nom_ligne]
            nom_train_utilise = trains[i]
            train_utilise = noms_trains[nom_train_utilise]
            h_depart = heures_possibles[i][0]
            heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, gares_desservables[nom_ligne], ligne_etudiee[1])
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures
            plan[3][ind_ligne] = gares_desservables[nom_ligne]
            plan[4][ind_ligne] = nom_train_utilise
            plan[5][ind_ligne] = noeuds_desservis
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
    Une fonction qui permet de vérifier si un tronçon à une voie n'est pas surchargé.
    Entrees :
        plan = le plan à vérifier
        troncon_verif = le tronçon sur lequel notre étude va porter
    Sorties :
        un booléen, True si non surchargé et False sinon
    """

    # initialisation
    Occupation = []
    heures_passage = []
    h_entree, h_sortie = [],[]

    # on récupère les données des lignes qui contiennent ce tronçon
    for ligne in range(len(plan[0])):
        if plan[2][ligne] != -1: # si la ligne a été ajoutée dans le plan
            if troncon_verif in troncons_lignes[plan[0][ligne]][0]: # on prend la liste des trançons qui se situe dans le dico troncons_lignes
                ind_t = troncons_lignes[plan[0][ligne]][0].index(troncon_verif) # on recherche l'indice du tronçon dans la ligne

                # recuperation des dates d'entrée et de sortie du tronçon avec la fonction entree_sortie_troncon
                t_entree, t_sortie = entree_sortie_troncon(plan[2][ligne], plan[1][ligne], troncons_lignes[plan[0][ligne]][0])[1][ind_t]
                h_entree.append(t_entree)
                h_sortie.append(t_sortie)
                heures_passage.append([t_entree, t_sortie, troncons_lignes[plan[0][ligne]][1][ind_t]])

    # si le tronçon n'est parcouru par aucune des lignes ajoutées dans plan
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))

    # on va regarder l'occupation du tronçon à tous les instants
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)): # indice dans la liste heures_passage
            if heures_passage[ind_train][0] == t:
                if len(Occupation) == 0: # si aucun train n'est déjà présent sur le tronçon
                    Occupation.append([ind_train, heures_passage[ind_train][2]])
                else :
                    if Occupation[-1][1] == heures_passage[ind_train][2]: # si les deux trains sur le tronçon vont bien dans le même sens

                        # si les trains ne sont pas assez espacés
                        # Occupation[[-1][0]][1] = l'heure de sortie du tronçon du dernier train étant rentré sur le tronçon
                        # Occupation[[-1][0]][0] = l'heure d'entrée dans le tronçon du dernier train étant rentré
                        if heures_passage[ind_train][1] - heures_passage[Occupation[-1][0]][1] < 4 or heures_passage[ind_train][0] - heures_passage[Occupation[-1][0]][0] < 4:
                            return False
                        else :
                            Occupation.append([ind_train, heures_passage[ind_train][2]])
                    else :
                        return False
            elif heures_passage[ind_train][1] == t: # si un train sort à la minute t
                if len(Occupation) != 0:

                    # ce n'est pas le premier train qui est rentré qui ressort :  il y a rattrapage !
                    if ind_train != Occupation[0][0]:
                        return False
                    else :
                        del Occupation[0] # on supprime le train du tronçon
    return True

def verif_troncon_2voies(plan, troncon_verif):
    """
        Une fonction qui permet de vérifier si un tronçon à 2 voies n'est pas surchargé.
    Entrees :
        plan = le plan à vérifier
        troncon_verif = le tronçon sur lequel notre étude va porter
    Sorties :
        un booléen, True si non surchargé et False sinon
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
    Une fonction qui permet de vérifier si un tronçon à 3 voies n'est pas surchargé.
    Entrees :
        plan = le plan à vérifier
        troncon_verif = le tronçon sur lequel notre étude va porter
    Sorties :
        un booléen, True si non surchargé et False sinon
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
    Une fonction qui permet de vérifier si un tronçon à 4 voies n'est pas surchargé.
    Entrees :
        plan = le plan à vérifier
        troncon_verif = le tronçon sur lequel notre étude va porter
    Sorties :
        un booléen, True si non surchargé et False sinon
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

def dist_noeuds_ligne(troncons_l, sens_parcours):
    """
    Donne la liste des noeuds ordonnées dans le sens de parcours de la ligne, ainsi que les distances depuis l'origine correspondantes
    Entrees :
        troncons_l = la liste des tronçons de la ligne
        sens_parcours = une liste de la même taille que le liste des tronçons qui nous donne le sens de parcours de chaque tronçon
    Sorties :
        dist_gares_ligne = la liste des distances depuis l'origine de chaque noeud
        noeuds_l = la liste des noeuds de la ligne dans l'ordre du sens de parcours de la ligne
    """
    kmt = 0
    if sens_parcours[0] :
        noeuds_l = [troncons_l[0][0]]
    else :
        noeuds_l = [troncons_l[0][1]]
    dist_gares_ligne = [0]
    for i in range(len(troncons_l)):
        kmt += troncons_l[i][3]
        if sens_parcours[i] :
            dist_gares_ligne.append(kmt)
            noeuds_l.append(troncons_l[i][1])
        else :
            dist_gares_ligne.append(kmt)
            noeuds_l.append(troncons_l[i][0])
    return dist_gares_ligne, noeuds_l

def verif_noeud(plan, noeud_verif):
    """
    Une fonction qui permet de vérifier si un noeud n'est pas surchargé
    Entrees :
        plan = le plan de transport que l'on veut vérifier
        noeud_verif = le noeud concerné par la vérification
    Sortie :
        un booléen, True s'il n'est pas surchargé, False sinon
    """
    Occupation = []
    heures_passage = []
    h_entree, h_sortie = [], []
    capacite = capa_noeuds[noeud_verif]
    for i_ligne in range(len(plan[0])):
        if plan[2][i_ligne] != -1:
            troncons, sens_troncons = troncons_lignes[plan[0][i_ligne]][0:2]
            if noeud_verif in plan[5][i_ligne]:
                ind_noeud = plan[5][i_ligne].index(noeud_verif)
                if ind_noeud < len(plan[5][i_ligne]) - 1 and plan[5][i_ligne][ind_noeud + 1] == noeud_verif:
                    t_entree, t_sortie = plan[2][i_ligne][ind_noeud : ind_noeud + 2]
                else :
                    t_entree, t_sortie = plan[2][i_ligne][ind_noeud], plan[2][i_ligne][ind_noeud] + 1
                heures_passage.append([t_entree, t_sortie])
    if h_entree == [] :
        return True
    h_min = int(min(h_entree))
    h_max = int(max(h_sortie))
    for t in range(h_min, h_max+1):
        for ind_train in range(len(heures_passage)):
            if heures_passage[ind_train][0] == t :
                if len(Occupation) < capacite:
                    Occupation.append(ind_train)
                else :
                    return False
            elif heures_passage[ind_train][1] == t:
                if ind_train in Occupation:
                    del Occupation[Occupation.index(ind_train)]
    return True

def bien_places(plan, ind_h):
    for i_ligne in range(len(plan[0])):
        if plan[2][i_ligne] != -1:
            for i in range(len(ind_h)):
                if i_ligne in range(ind_h[i][0], ind_h[i][1]):
                    h_min , h_max = 60*(i+6), 60*(i+7)
            if plan[0][i_ligne] in ['TGV Creusot-Lyon', 'TGV Lille-Grenoble', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']:
                if not(plan[2][i_ligne][0] in range(h_min, h_max)):
                    return False
            else :
                if not(plan[2][i_ligne][0] in range(h_min - 10, h_max - 10)):
                    return False
    return True

def verif_plan(plan):
    """
    """
    _troncons_verif = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l20, l21, l22, l22bis, l23, l24, l25, l26, l27, l27bis, l28, l28bis, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, l61]
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
    for noeud_v in list(capa_noeuds.keys()):
        if not(verif_noeud(plan, noeud_v)):
            return False
    return True