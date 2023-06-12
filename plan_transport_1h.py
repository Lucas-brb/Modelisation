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

"""
plan = [
[liste des lignes]
[liste distance par ligne]
[liste des heures]
[liste gares desservies]
[liste trains utilisés]
]
"""

lignes_ter1 = ['Lyon-Chambery', 'Chambery-Annecy', 'Grenoble-Chambery', 'Lyon-Macon', 'Lyon-Valence', 'Lyon-Grenoble', 'Valence-Grenoble', 'Chambery-Lyon', 'Annecy-Chambéry', 'Chambéry-Grenoble', 'Macon_Lyon', 'Valence-Lyon', 'Grenoble-Lyon', 'Grenoble-Valence']
lignes_ter2 = ['Lyon-Saint-Etienne', 'Roanne-Saint-Etienne', 'Lyon-Bourg-en-Bresse', 'Bourg-en-Bresse-Macon', 'Roanne-Lyon', 'Lyon-Annecy', 'StE-Lyon', 'StE-Roanne', 'Bourg-en-Bresse-Lyon', 'Macon-Bourg-en-Bresse','Lyon-Roanne', 'Annecy-Lyon']
tgv_normal = ['TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille']
tgv_pointe = tgv_normal*2


heures_pointe = [7, 8, 9, 12, 13, 14, 17, 18, 19]
min_pointe = [_ for _ in range(7*60, 9*60)] + [_ for _ in range(12*60, 14*60)] + [_ for _ in range(17*60, 18*60)]
indices_heures = []
indices_heures_initial = 0
plan = []
for _ in range(6, 21):
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

plan.append([0 for i in range(len(plan[0]))])
plan.append([-1 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
plan.append([0 for i in range(len(plan[0]))])
liste_lignesOK = [False for i in range(len(plan[0]))]


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

def Ajout_train(plan, lignesOK, indices_heures, min_pointe):
    '''
    Permet d'ajouter un train à un plan de transport.
    Entrees :
        plan = le plan de transport actuel
        lignesOK = la liste des lignes qui sont déjà incluses dans le plan de transport
        (les indices avec le plan correspondent)
    Sortie :
        plan = le plan de transport fini
    Remarque : cette fonction est une fonction récursive.
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
            #heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
            #gares_desservies = gares_desservables[nom_ligne]

            # on va tester sur toutes les minutes de la journée s'il est possible de faire démarrer le train à cette heure
            for i in range(len(indices_heures)):
                if ind_ligne_test in range(indices_heures[i][0], indices_heures[i][1]):
                    h_d_min , h_d_max = 60*(i+6), 60*(i+7)

            # on calcule le temps mis par le train pour parcourir sa ligne
            #print(h_d_min, h_d_max)
            if h_d_min in min_pointe and not(nom_ligne in ['TGV Lille-Grenoble', 'TGV Grenoble-Lille']):
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, "", ligne_etudiee[1])
                gares_desservies = []
            else:
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
                gares_desservies = gares_desservables[nom_ligne]
            for h_depart in range(h_d_min, h_d_max):
                heures_n = [h + h_depart for h in heures]
                plan_copie[1][ind_ligne_test] = distances
                plan_copie[2][ind_ligne_test] = heures_n
                plan_copie[3][ind_ligne_test] = gares_desservies
                plan_copie[4][ind_ligne_test] = nom_train_utilise
                plan_copie[5][ind_ligne_test] = noeuds_desservis
                if verif_plan(plan_copie): # si on peut faire partir le train sur la ligne considérée à l'heure voulue
                    heures_possibles[ind_ligne].append(h_depart)
            trains.append(nom_train_utilise)

        # si un des trains ne peut pas partir avec ce plan de transport, on est bloqués
        if any(len(x) == 0 for x in heures_possibles) :
            for p in range(len(heures_possibles)):
                if len(heures_possibles[p]) == 0:
                    break
            print(p)
            '''ind_ligne_bug = ind_lignes_nOK[p]
            if not(plan[0][ind_ligne_bug] in ['TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille'] :
                for h in range(len(plan)):
                    del plan[h][ind_ligne_bug]
                del lignesOK [ind_ligne_bug]'''
            for n in range(len(indices_heures)):
                if p in range(indices_heures[n][0], indices_heures[n][1]):
                    break
            ind_ligne = rd.randint(indices_heures[n][0], indices_heures[n][1])

            # on retire un élément au hasard du plan
            if not(all(not(x) for x in lignesOK)):
                while not(lignesOK[ind_ligne]) :
                    ind_ligne = rd.randint(indices_heures[n][0], indices_heures[n][1])
                plan[1][ind_ligne] = -1
                plan[2][ind_ligne] = -1
                plan[3][ind_ligne] = ""
                plan[4][ind_ligne] = ""
                plan[5][ind_ligne] = 0
                lignesOK[ind_ligne] = False
        else : # si on n'est pas bloqués
            index = plus_petite_longueur(heures_possibles) # on récupère le liste des indices des listes de plus petite longueur dans heures_possibles
            i = rd.choice(index)
            ind_ligne = ind_lignes_nOK[i]
            nom_ligne = plan[0][ind_ligne]
            ligne_etudiee = troncons_lignes[nom_ligne]
            nom_train_utilise = trains[i]
            train_utilise = noms_trains[nom_train_utilise]
            h_depart = heures_possibles[i][0]
            if h_d_min in min_pointe and not(nom_ligne in ['TGV Lille-Grenoble', 'TGV Grenoble-Lille']):
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, "", ligne_etudiee[1])
                gares_desservies = []
            else:
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, gares_desservables[nom_ligne], ligne_etudiee[1])
                gares_desservies = gares_desservables[nom_ligne]
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures
            plan[3][ind_ligne] = gares_desservies
            plan[4][ind_ligne] = nom_train_utilise
            plan[5][ind_ligne] = noeuds_desservis
            lignesOK[ind_ligne] = True
        return Ajout_train(plan, lignesOK, indices_heures, min_pointe)
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

def Ajout_train_v2(plan, nb_desserte_ter, indices_heures, min_pointe):
    '''
    Permet d'ajouter un train à un plan de transport.
    Entrees :
        plan = le plan de transport actuel
        lignesOK = la liste des lignes qui sont déjà incluses dans le plan de transport
        (les indices avec le plan correspondent)
    Sortie :
        plan = le plan de transport fini
    Remarque : cette fonction est une fonction récursive.
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
            #heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
            #gares_desservies = gares_desservables[nom_ligne]

            # on va tester sur toutes les minutes de la journée s'il est possible de faire démarrer le train à cette heure
            for i in range(len(indices_heures)):
                if ind_ligne_test in range(indices_heures[i][0], indices_heures[i][1]):
                    h_d_min , h_d_max = 60*(i+6), 60*(i+7)

            # on calcule le temps mis par le train pour parcourir sa ligne
            #print(h_d_min, h_d_max)
            if h_d_min in min_pointe and not(nom_ligne in ['TGV Lille-Grenoble', 'TGV Grenoble-Lille']):
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, "", ligne_etudiee[1])
                gares_desservies = []
            else:
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, 0, gares_desservables[nom_ligne], ligne_etudiee[1])
                gares_desservies = gares_desservables[nom_ligne]
            for h_depart in range(h_d_min, h_d_max):
                heures_n = [h + h_depart for h in heures]
                plan_copie[1][ind_ligne_test] = distances
                plan_copie[2][ind_ligne_test] = heures_n
                plan_copie[3][ind_ligne_test] = gares_desservies
                plan_copie[4][ind_ligne_test] = nom_train_utilise
                plan_copie[5][ind_ligne_test] = noeuds_desservis
                if verif_plan(plan_copie): # si on peut faire partir le train sur la ligne considérée à l'heure voulue
                    heures_possibles[ind_ligne].append(h_depart)
            trains.append(nom_train_utilise)

        # si un des trains ne peut pas partir avec ce plan de transport, on est bloqués
        if any(len(x) == 0 for x in heures_possibles) :
            for p in range(len(heures_possibles)):
                if len(heures_possibles[p]) == 0:
                    break
            print(p)
            '''ind_ligne_bug = ind_lignes_nOK[p]
            if not(plan[0][ind_ligne_bug] in ['TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille'] :
                for h in range(len(plan)):
                    del plan[h][ind_ligne_bug]
                del lignesOK [ind_ligne_bug]'''
            for n in range(len(indices_heures)):
                print(indices_heures[n][0], indices_heures[n][1])
                if p in range(indices_heures[n][0], indices_heures[n][1]):
                    break
            ind_ligne = rd.randint(indices_heures[n][0], indices_heures[n][1])

            # on retire un élément au hasard du plan
            if not(all(not(x) for x in lignesOK)):
                while not(lignesOK[ind_ligne]) :
                    ind_ligne = rd.randint(indices_heures[n][0], indices_heures[n][1])
                plan[1][ind_ligne] = -1
                plan[2][ind_ligne] = -1
                plan[3][ind_ligne] = ""
                plan[4][ind_ligne] = ""
                plan[5][ind_ligne] = 0
                lignesOK[ind_ligne] = False
        else : # si on n'est pas bloqués
            index = plus_petite_longueur(heures_possibles) # on récupère le liste des indices des listes de plus petite longueur dans heures_possibles
            i = rd.choice(index)
            ind_ligne = ind_lignes_nOK[i]
            nom_ligne = plan[0][ind_ligne]
            ligne_etudiee = troncons_lignes[nom_ligne]
            nom_train_utilise = trains[i]
            train_utilise = noms_trains[nom_train_utilise]
            h_depart = heures_possibles[i][0]
            if h_d_min in min_pointe and not(nom_ligne in ['TGV Lille-Grenoble', 'TGV Grenoble-Lille']):
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, "", ligne_etudiee[1])
                gares_desservies = []
            else:
                heures, distances, noeuds_desservis = temps_parcours_ligne(ligne_etudiee[0], train_utilise, h_depart, gares_desservables[nom_ligne], ligne_etudiee[1])
                gares_desservies = gares_desservables[nom_ligne]
            plan[1][ind_ligne] = distances
            plan[2][ind_ligne] = heures
            plan[3][ind_ligne] = gares_desservies
            plan[4][ind_ligne] = nom_train_utilise
            plan[5][ind_ligne] = noeuds_desservis
            lignesOK[ind_ligne] = True
        return Ajout_train(plan, lignesOK, indices_heures, min_pointe)

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
            if heures_passage[ind_train][1] == t: # si un train sort à la minute t
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
            if heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1:
                    del Occupation1[Occupation1.index(ind_train)]
                elif ind_train in Occupation2 :
                    del Occupation2[Occupation2.index(ind_train)]
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
            if heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1 :
                    del Occupation1[Occupation1.index(ind_train)]
                elif ind_train in Occupation2 :
                    del Occupation2[Occupation2.index(ind_train)]
                elif len(Occupation3) != 0:
                    if Occupation3[0][0] == ind_train :
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
            if ind_train == 13:
                pass
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
            if heures_passage[ind_train][1] == t: # un train sort à la minute t
                if ind_train in Occupation1:
                    del Occupation1[Occupation1.index(ind_train)]
                elif ind_train in Occupation2:
                    del Occupation2[Occupation2.index(ind_train)]
                elif ind_train in Occupation3:
                    del Occupation3[Occupation3.index(ind_train)]
                elif ind_train in Occupation4 :
                    del Occupation4[Occupation4.index(ind_train)]
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
    if sens_parcours[0] : # si le tronçon est parcouru dans le sens positif
        noeuds_l = [troncons_l[0][0]]
    else :
        noeuds_l = [troncons_l[0][1]]
    dist_gares_ligne = [0]
    for i in range(len(troncons_l)):
        kmt += troncons_l[i][3] # on ajoute la distance du tronçon qui sépare nos deux noeuds
        if sens_parcours[i] :
            noeuds_l.append(troncons_l[i][1])
        else :
            noeuds_l.append(troncons_l[i][0])
        dist_gares_ligne.append(kmt)
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
        a_supprimer = []
        for ind_train in range(len(heures_passage)):
            if heures_passage[ind_train][0] == t :
                if len(Occupation) < capacite:
                    Occupation.append(ind_train)
                else :
                    return False
            if heures_passage[ind_train][1] == t:
                if ind_train in Occupation:
                    a_supprimer.append(ind_train)
        for elt in a_supprimer:
            del Occupation[Occupation.index(elt)]
    return True

def tgv_bien_places(plan, liste_tgv):
    tous_tgv = [[] for b in range(len(liste_tgv))]
    for i_ligne in range(len(plan[0])):
        if plan[2][i_ligne] != -1:
            if plan[0][i_ligne] in liste_tgv:
                i_tgv = liste_tgv.index(plan[0][i_ligne])
                tous_tgv[i_tgv].append(plan[2][i_ligne][0])
    for elt in tous_tgv :
        for j in range(len(elt)-1):
            if abs(elt[j] - elt[j+1]) <= 20:
                return False
    return True

def verif_plan(plan):
    """
    Verifie si un plan de transport est bon
    Entree :
        plan = le plan de transport qu'on veut vérifier
    Sortie :
        un booléen : True si le plan est bon, False sinon
    """
    if not(tgv_bien_places(plan, tgv_normal)):
        return False
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