#données des trajets


gares = ['Lyon', 'Roanne', 'Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain', 'Villefranche', 'Mâcon', 'Bourg-en-Bresse', 'Villars', 'Sathenay', 'Givors', 'Rive de Gier', 'Saint Chamond', 'Saint Etienne', 'Feurs', 'Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly', 'Annecy', 'Chambéry', 'Montmélian', 'Grenoble université', 'Grenoble', 'Moirans', 'Voiron', 'Rives', 'Saint André', 'Tour du Pin', 'Bourgoin', "Isle d'Abeau", 'Vénissieux', 'Chasse sur Rhône', 'Vienne','Saint Rambert', 'Tain', 'Valence', 'Valence TGV', 'Romans']

chgmt_vitesse=['Oullins', 'Saint Just Saint Rambert', 'tronçon imposé']


bifurcations=['Lyon Saint Clair', 'Pont de Veyle', 'Saint-Quentin-Fallavier','Quincieux']

chgmt_nb_voies=['Perrache']

'''lien1 = l1 = [Point de départ, point d'arrivée, vitesse (km/h), distance (km), électricité (1) ou non (0), nombres de voies]'''

l1= [gares[1], gares[2], 105, 25,0,2]
l2=[gares[2], gares[3], 105, 15, 0, 2]
l3=[gares[3],gares[4],105,18,0,2]
l4=[gares[4],gares[5],105,8,0,2]
l5=[gares[5],bifurcations[3],140,10.4,0,2]
l6=[bifurcations[3], gares[6],140, 1.6, 1, 4]
l7=[gares[6], chgmt_vitesse[2], 140, 11, 1,4]
l8=[chgmt_vitesse[2], bifurcations[0],40,3,1,4]
l9=[bifurcations[0],gares[0],90,4,1,4]

l10=[gares[1],gares[16],95,42,0,2]
l11=[gares[16], chgmt_vitesse[1], 140,32,0,2]
l12=[chgmt_vitesse[1], gares[15],100,14,0,2]

l13=[gares[0],chgmt_nb_voies[0],90,2.5,1,4]
l14=[chgmt_nb_voies[0],chgmt_vitesse[0],90,5.5,1,2]
l15=[chgmt_vitesse[0],gares[12],115,16,1,2]
l16=[gares[12],gares[13],125,16,1,2]
l17=[gares[13],gares[14],125,10,1,2]
l18=[gares[14],gares[15],125,12,1,2]

l19=[bifurcations[3], gares[6],160, 1.6, 1, 4]
l20=[bifurcation[3],gares[7],160,15,1,2]
l21=[gares[7],gares[8],160,38,1,2]

Ligne_Roanne_Lyon = [l1, l2, l3, l4,l5,l6,l7,l8,l9]
Ligne_Roanne_SaintEtienne =[l10,l11,l12]
Ligne_Lyon_SaintEtienne=[l13,l14,l15,l16,l17,l18]
Ligne_Lyon_Mâcon=[l9,l8,l7,l19,l20,l21]



