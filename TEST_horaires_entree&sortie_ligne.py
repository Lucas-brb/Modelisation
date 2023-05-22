def entree_sortie_troncon(heures, distances, ligne):
    '''Connaitre les heures d'entrée et de sortie de chaque tronçon pour une ligne donnée
    Entrées:
    ligne = [troncon 1, troncon 2,..., troncon n]
    distances = [0, d1, d2, d2, d3,..., dn], on met 2 fois la même distance s'il y a une gare car le train ne bouge pas
    heures = [0, heure 1, heure 2, heure 2 +2min, heure 3,..., heure n], lorsque le train passe par une gare il y a une pause de 2min

    Sorties :
    '''
    horaires =[]
    for k in range(0,len(distances)-1) :
        if distances[k] != distances[k+1]:
            horaires.append([heures[k], heures[k+1]])
        else :
            pass
    L=[ligne,horaires]
    return L

#test
heures=[0,5,10,13,15,32,34,40,42,51]
distances=[0,2.5, 7.5,23.5,23.5,39.5,39.5,49.5,49.5,61.5]
Ligne_Lyon_SaintEtienne=[[l13,l14,l15,l16,l17,l18], [True, True, True, True, True, True], all([l13[4],l14[4],l15[4],l16[4],l17[4],l18[4]])]

print(entree_sortie_troncon(heures,distances,Ligne_Lyon_SaintEtienne[0]))
