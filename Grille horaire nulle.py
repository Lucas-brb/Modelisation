#grille horaire

#D=#résultat de la fonction qui retourne toutes les données (faite par Lucas)
##
import numpy as np

gares = ['Lyon', 'Roanne', 'Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain', 'Villefranche', 'Mâcon', 'Bourg-en-Bresse', 'Villars', 'Sathenay', 'Givors', 'Rive de Gier', 'Saint Chamond', 'Saint Etienne', 'Feurs', 'Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly', 'Annecy', 'Chambéry', 'Montmélian', 'Grenoble université', 'Grenoble', 'Moirans', 'Voiron', 'Rives', 'Saint André', 'Tour du Pin', 'Bourgoin', "Isle d'Abeau", 'Vénissieux', 'Chasse sur Rhône', 'Vienne','Saint Rambert', 'Tain', 'Valence', 'Valence TGV', 'Romans', 'Mâcon-Loché-TGV','Crest']

gares2=["lyon","roanne","tarare"]
'''data = [['' for _ in range(10)] for l in range(45)]
data[0][0]='Gares' '''

f'''or i in range(0,44):
    data[i+1][0]=gares[i]
print(data)'''

##
'''Ligne= D[0][#liste de toutes les lignes] =
gares_d=[#gares desservies]

for j in heures :
    data[1,j] = j
    for i in range(np.shape(gares)) :
        if gares[i] in gares_d :
            data[i,1]= j+transition_troncon(Ligne[i-1][2], Ligne[i][2], Ligne[i+1][2], Ligne[i][3],train)[0]
        else :
            data[i,1]='''

import matplotlib.pyplot as plt

fig, ax =plt.subplots(1,1)
tableau = [['' for _ in range(2)] for l in range(np.shape(gares2)[0])]
for i in range (1,np.shape(gares2)[0]-1):
    tableau[i][0]=data[i][0]
column_labels=["Gares", "Heure de départ"]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data,colLabels=column_labels,loc="center")

plt.show()



'''fig, ax =plt.subplots(1,1)
data=[["Lyon","8h"],
      ["Feurs","12h"],
      ["Saint-Etienne",""]]
column_labels=["Gares", "Heure de départ"]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data,colLabels=column_labels,loc="center")

plt.show()'''