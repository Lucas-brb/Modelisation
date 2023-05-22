import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#Ligne 1 : Lyon-Valence
#Ligne 2 : Lyon-Grenoble
#Ligne 3 : Valence-Grenoble
#Ligne 4 : Grenoble-Chambéry
#Ligne 5 : Lyon-Chambéry
#Ligne 6 : Lyon-Annecy
#Ligne 7 : Chambéry-Annecy
#Ligne 8 : Lyon-Bourg En Bresse
#Ligne 9 : Lyon-Mâcon
#Ligne 10 : Bourg En Bresse-Mâcon
#Ligne 11 : Lyon-Saint Etienne
#Ligne 12 : Saint Etienne-Roanne
#Ligne 13 : Lyon-Roanne

fig = plt.figure(figsize=(21,8))
ax = fig.add_subplot(111)
data=[["Lyon","1","2","","","5","6","","8","9","","11","","13"],
      ["Chasse s/ Rhône","1","","","","","","","","","","","",""],
      ["Saint-Etienne","1","","","","","","","","","","","",""],
      ["Vienne","1","","","","","","","","","","","",""],
      ["Saint-Rambert","1","","","","","","","","","","","",""],
      ["Tain","1","","","","","","","","","","","",""],
      ["Valence Ville","1","","3","","","","","","","","","",""],
      ["Valence TGV","","","3","","","","","","","","","",""],
      ["Vénissieux","","2","","","","","","","","","","",""],
      ["Isle d Abeau","","2","","","","","","","","","","",""],
      ["Bourgoin","","2","","","","","","","","","","",""],
      ["La Tour du Pin","","2","","","","","","","","","","",""],
      ["Saint André","","2","","","","","","","","","","",""],
      ["Rives","","2","","","","","","","","","","",""],
      ["Voiron","","2","","","","","","","","","","",""],
      ["Moirans","","2","3","","","","","","","","","",""],
      ["Grenoble","","2","3","4","","","","","","","","",""],
      ["Grenoble Univ","","","","4","","","","","","","","",""],
      ["Montmélian","","","","4","","","","","","","","",""],
      ["Montluer","","","","","5","6","","","","","","",""],
      ["Ambérieu","","","","","5","6","","","","","","",""],
      ["Culoz","","","","","5","6","","","","","","",""],
      ["Aix-les-Bains","","","","","5","6","7","","","","","",""],
      ["Chambéry","","","","4","5","","7","","","","","",""],
      ["Rumilly","","","","","","6","7","","","","","",""],
      ["Annecy","","","","","","6","7","","","","","",""],
      ["Sathonay","","","","","","","","8","","","","",""],
      ["Villars","","","","","","","","8","","","","",""],
      ["Bourg-En-Bresse","","","","","","","","8","","10","","",""],
      ["Saint Germain","","","","","","","","","9","","","",""],
      ["Mâcon","","","","","","","","","9","10","","",""],
      ["Givors","","","","","","","","","","","11","",""],
      ["Rive de Gier","","","","","","","","","","","11","",""],
      ["Saint Chamond","","","","","","","","","","","11","",""],
      ["Saint Etienne","","","","","","","","","","","11","12",""],
      ["Feurs","","","","","","","","","","","","12",""],
      ["Lozanne","","","","","","","","","","","","","13"],
      ["Arbesle","","","","","","","","","","","","","13"],
      ["Tarare","","","","","","","","","","","","","13"],
      ["Amplepuis","","","","","","","","","","","","","13"],
      ["Roanne","","","","","","","","","","","","12","13"]
      ]
column_labels=["Gares", "Départ ligne 1", "Départ ligne 2", "Départ ligne 3","Départ ligne 4","Départ ligne 5","Départ ligne 6","Départ ligne 7","Départ ligne 8","Départ ligne 9","Départ ligne 10","Départ ligne 11","Départ ligne 12","Départ ligne 13"]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data,colLabels=column_labels,loc="center")
plt.show()