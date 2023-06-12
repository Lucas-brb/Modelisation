import matplotlib.pyplot as plt

#dans la grille horaire, pour les gares desservies hors départ de terminus, on retrouve deux fois le nom de la gare avec deux heures correspondantes : la première quand le train arrive dans cette gare, la deuxième quand le train part de cette gare, soit 2 min après être arrivé

# Données du tableau
def Grille_horaire(ligne,plan):
    Gares = Liste_Gares_Heures(ligne,plan)[0]
    HeureDépart = Liste_Gares_Heures(ligne,plan)[1]

# Transposer les données
    table_data = [Gares] + [HeureDépart[i] for i in range (len(HeureDépart))]
    table_data_transposed = list(map(list, zip(*table_data)))

# Création du graphique
    fig, ax = plt.subplots()

# Création du tableau
    table = ax.table(cellText=table_data_transposed, colLabels=['Gares', 'Horaire', 'Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire','Horaire'], loc='center')

# On met les lignes d'heures de pointe en rouge -- Si la ligne est rouge, alors le train ne s'arrête qu'à la première gare et au terminus
    liste_heures = []

    for heure in [7,8,12,13,14,17,18,19]:
        for minute in range (0, 60):
            heure_complet = f'{heure} h {minute}'
            liste_heures.append(heure_complet)
# Style du tableau
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)

# Suppression des axes du graphique
    ax.axis('off')

# Affichage du graphique
    plt.show()


