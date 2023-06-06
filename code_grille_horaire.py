import matplotlib.pyplot as plt

#dans la grille horaire, pour les gares desservies hors départ de terminus, on retrouve deux fois le nom de la gare avec deux heures correspondantes : la première quand le train arrive dans cette gare, la deuxième quand le train part de cette gare, soit 2 min après être arrivé

# Données du tableau
def Grille_horaire(ligne):
    Gares = Liste_Gares_Heures(ligne)[0]
    HeureDépart = Liste_Gares_Heures(ligne)[1]
# Transposer les données
    table_data = [Gares, HeureDépart]
    table_data_transposed = list(map(list, zip(*table_data)))

# Création du graphique
    fig, ax = plt.subplots()

# Création du tableau
    table = ax.table(cellText=table_data_transposed, colLabels=['Gares', 'Heure de passage'], loc='center')

# Style du tableau
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)

# Suppression des axes du graphique
    ax.axis('off')

# Affichage du graphique
    plt.show()


Liste_lignes=[Ligne_BourgEnBresse_Macon, Ligne_Chambery_Annecy, Ligne_Grenoble_Chambery, Ligne_Lyon_BourgEnBresse, Ligne_Lyon_Chambery, Ligne_Lyon_Grenoble, Ligne_Lyon_Macon, Ligne_Lyon_SaintEtienne, Ligne_Lyon_Valence, Ligne_Roanne_Lyon, Ligne_Roanne_SaintEtienne, Ligne_Valence_Grenoble,Ligne_Lyon_Annecy]


