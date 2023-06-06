def Liste_Gares_Heures(ligne): #ligne sous la forme 'Roanne-Lyon'
    troncons_l=troncons_lignes[ligne][0]
    sens_parcours=troncons_lignes[ligne][1]
    Gares=[]
    Heures=[]
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
                    Gares.append(troncons_l[i][0])
                else:
                    indices.append(i)
            elif sens_parcours[i] == False:
                if troncons_l[i][1] in gares:
                    Gares.append(troncons_l[i][1])
                    Gares.append(troncons_l[i][1])
                else:
                    indices.append(i)
        if i == len(troncons_l)-1: #est-ce le terminus
            if sens_parcours[i] == True:
                Gares.append(troncons_l[len(troncons_l)-1][1])
            elif sens_parcours[i] == False:
                Gares.append(troncons_l[len(troncons_l)-1][0])

    #création de la liste des heures de passage à ces gares
    indice_plan = plan[0].index(ligne)
    for x in plan[2][indice_plan]:
        Heures.append(x)

    #on retire les heures correspond aux points qui ne sont pas des gares desservies
    Heures = [Heures[i] for i in range(len(Heures)) if not(i in indices)]

    #on met les heures sous le format '9h05'
    for k in range (0, len(Heures)) :
        Heures[k]=min_to_format(Heures[k])

    return Gares, Heures