from plan_fonctionnel import *
from donnees_lignes import *
from acceleration_train import *

def Liste_Gares_Heures(ligne,plan): #ligne sous la forme 'Roanne-Lyon'
    troncons_l=troncons_lignes[ligne][0]
    sens_parcours=troncons_lignes[ligne][1]
    Gares=[]
    indices=[]

    #création de la liste des gares desservies
    for i in range (0, len(troncons_l)):
        if i == 0 : #est-ce le départ
            if sens_parcours[i] == True:
                if troncons_l[i][0] in gares:
                    Gares.append(troncons_l[i][0])
                else:
                    indices.append(i)
            elif sens_parcours[i] == False:
                if troncons_l[i][1] in gares:
                    Gares.append(troncons_l[i][1])
                else:
                    indices.append(i)
        else : #s'arrête-t-on à cette gare sur la ligne
            if sens_parcours[i] == True:
                if troncons_l[i][0] in gares:
                    Gares.append(troncons_l[i][0])
                    #Gares.append(troncons_l[i][0])
                else:
                    indices.append(i)
            elif sens_parcours[i] == False:
                if troncons_l[i][1] in gares:
                    Gares.append(troncons_l[i][1])
                    #Gares.append(troncons_l[i][1])
                else:
                    indices.append(i)
        if i == len(troncons_l)-1: #est-ce le terminus
            if sens_parcours[i] == True:
                Gares.append(troncons_l[len(troncons_l)-1][1])
            elif sens_parcours[i] == False:
                Gares.append(troncons_l[len(troncons_l)-1][0])

    #création de la liste des heures de passage à ces gares
    indice_plan = []
    for j in range(0, len(plan[0])):
        if plan[0][j]==ligne:
            indice_plan.append(j)
    Heures=[[] for _ in range (len(indice_plan))]
    Distances=[[] for _ in range (len(indice_plan))]
    for k in range (len(indice_plan)):
        for l in range (0, len(plan[2][indice_plan[k]])-1):
            Heures[k].append(plan[2][indice_plan[k]][l+1])
            Distances[k].append(plan[1][indice_plan[k]][l+1])
            for h in range (1,len(Heures[k])-1):
                if Distances[k][h+1]==Distances[k][h] :
                    Heures[k][h]=Heures[k][h+1]
            Heur = []
            occurrences = {}
            for chiffre in Heures[k]:
                if chiffre not in occurrences:
                    occurrences[chiffre] = True
                    Heur.append(chiffre)
                Heures[k]=Heur #on transforme la liste des heures où il y avait des heures d'arrivée et de départ aux gares intermediaires en liste des heures où les trains ne font que passer par ces gares sans s'y arrêter

    #on retire les heures correspond aux points qui ne sont pas des gares desservies
    for k in range (len(indice_plan)):
        Heures[k] = [Heures[k][i] for i in range(len(Heures[k])) if not(i in indices)]

    #on met les heures sous le format '9h05'
    for k in range  (len(indice_plan)):
        for m in range (0, len(Heures[k])) :
            Heures[k][m]=min_to_format(Heures[k][m])

    return Gares, Heures

def Liste_Gares_Heures_v2(ligne, plan):
    """
    """
    ind_ligne = []
    for j in range(len(plan[0])):
        if plan[0][j] == ligne:
            ind_ligne.append(j)
    Heures = [[min_to_format(plan[2][_][0])] for _ in ind_ligne]
    Noeuds = [[plan[5][_][0]] for _ in ind_ligne]
    a_supprimer = [[] for _ in ind_ligne]
    for p in range(len(ind_ligne)):
        for k in range(1, len(plan[5][ind_ligne[p]])):
            if plan[5][ind_ligne[p]][k] in gares:
                if plan[5][ind_ligne[p]][k] == Noeuds[p][-1]:
                    Heures[p][-1] = Heures[p][-1] + ' - ' + min_to_format(plan[2][ind_ligne[p]][k])
                else:
                    Heures[p].append(min_to_format(plan[2][ind_ligne[p]][k]))
                    Noeuds[p].append(plan[5][ind_ligne[p]][k])
    return Noeuds[-1], Heures