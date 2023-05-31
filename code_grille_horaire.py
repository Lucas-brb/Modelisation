import matplotlib.pyplot as plt

# Données du tableau
def Grille_horaire(ligne, train, min_depart, gares_desservies):
    desserte = ligne[0]
    Gares=[]
    HeureDépart = []
    for i in range (0, len(desserte)):
        if desserte[i][0] in gares:
            Gares.append(desserte[i][0])
            HeureDépart.append(temps_parcours_ligne(desserte, train, min_depart, gares_desservies)[0][i])
    HeureDépart.append(temps_parcours_ligne(desserte, train, min_depart, gares_desservies)[0][len(desserte)])
    Gares.append(desserte[len(desserte)-1][1])
# Transposer les données
    table_data = [Gares, HeureDépart]
    table_data_transposed = list(map(list, zip(*table_data)))

# Création du graphique
    fig, ax = plt.subplots()

# Création du tableau
    table = ax.table(cellText=table_data_transposed, colLabels=['Gares', 'Heure de départ'], loc='center')

# Style du tableau
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)

# Suppression des axes du graphique
    ax.axis('off')

# Affichage du graphique
    plt.show()


Liste_lignes=[Ligne_BourgEnBresse_Macon, Ligne_Chambery_Annecy, Ligne_Grenoble_Chambery, Ligne_Lyon_BourgEnBresse, Ligne_Lyon_Chambery, Ligne_Lyon_Grenoble, Ligne_Lyon_Macon, Ligne_Lyon_SaintEtienne, Ligne_Lyon_Valence, Ligne_Roanne_Lyon, Ligne_Roanne_SaintEtienne, Ligne_Valence_Grenoble]


