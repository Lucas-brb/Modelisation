#grille horaire

D=#résultat de la fonction qui retourne toutes les données (faite par Lucas)
##
import numpy as np

gares = ['Lyon', 'Roanne', 'Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain', 'Villefranche', 'Mâcon', 'Bourg-en-Bresse', 'Villars', 'Sathenay', 'Givors', 'Rive de Gier', 'Saint Chamond', 'Saint Etienne', 'Feurs', 'Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly', 'Annecy', 'Chambéry', 'Montmélian', 'Grenoble université', 'Grenoble', 'Moirans', 'Voiron', 'Rives', 'Saint André', 'Tour du Pin', 'Bourgoin', "Isle d'Abeau", 'Vénissieux', 'Chasse sur Rhône', 'Vienne','Saint Rambert', 'Tain', 'Valence', 'Valence TGV', 'Romans', 'Mâcon-Loché-TGV','Crest']


ex_tab = [['' for _ in range(10)] for l in range(45)]
ex_tab[0][0]='Gares'

for i in range(0,44):
    ex_tab[i+1][0]=gares[i]
print(ex_tab)

##
Ligne= D[0][#liste de toutes les lignes] =
gares_d=[#gares desservies]

for j in heures :
    ex_tab[1,j] = j
    for i in gares_d :
        ex_tab[i,1]= j+transition_troncon(Ligne[i-1,2], Ligne[i,2], Ligne[i+1,2], Ligne[i,3],train)[0]
