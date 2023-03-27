#données des trajets


gares = ['Lyon', 'Roanne', 'Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain', 'Villefranche', 'Mâcon', 'Bourg-en-Bresse', 'Villars', 'Sathenay', 'Givors', 'Rive de Gier', 'Saint Chamond', 'Saint Etienne', 'Feurs', 'Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly', 'Annecy', 'Chambéry', 'Montmélian', 'Grenoble université', 'Grenoble', 'Moirans', 'Voiron', 'Rives', 'Saint André', 'Tour du Pin', 'Bourgoin', "Isle d'Abeau", 'Vénissieux', 'Chasse sur Rhône', 'Vienne','Saint Rambert', 'Tain-Tournon', 'Valence', 'Valence TGV', 'Romans']

chgmt_vitesse=['Oullins', 'Saint Just Saint Rambert', 'tronçon imposé']


bifurcations=['Lyon Saint Clair', 'Pont de Veyle', 'Saint-Quentin-Fallavier','Quincieux']

chgmt_nb_voies=['Perrache', 'Saint Priest','Saint Hilaire ouest','Saint Hilaire est','Saint Marcelin']

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

l22=[gares[0],gares[35], 150,20,1,4]
l23=[gares[35],gares[36], 120,10,1,2]
l24=[gares[36],gares[37],140,33,1,2]
l25=[gares[37],gares[38],140,27,1,2]
l26=[gares[38],gares[39],140,18,1,2]

l27=[gares[0],gares[34],90,7,1,4]
l28=[gares[34],chngmt_nb_voies[1],160,4,1,3]
l28=[chgmt_nb_voies[1],bifurcations[2],160,12,1,2]
l29=[bifurcations[2],gares[33],160,14,1,2]
l30=[gares[33],gares[32],160,6,1,2]
l31=[gares[32],gares[31],160,15,1,2]
l32=[gares[31],gares[30],160,7,1,2]
l33=[gares[30],gares[29],140,26,1,2]
l34=[gares[29],gares[28],140,10,1,2]
l35=[gares[28],gares[27],140,6,1,2]
l36=[gares[27],gares[26],140,20,1,2]

l37=[gares[39],gares[40],140,11,1,2]
l38=[gares[40],gares[41],140,10,1,2]
l39=[gares[41],chgmt_nb_voies[2],140,14,1,1]
l40=[chgmt_nb_voies[2],chgmt_nb_voies[3],140,5,1,2]
l41=[chgmt_nb_voies[3],chgmt_nb_voies[4],140,3.4,1,1]
l42=[chgmt_nb_voies[4],gares[27],140,25,1,2]

l43=[gares[26],gares[25],140,6,1,2]
l44=[gares[25],gares[24],140,46,1,2]
l45=[gares[24],gares[23],160,15,1,2]

l46=[gares[23],gares[20],110,14,1,2]
l47=[gares[20],gares[21],115,20,1,2]
l48=[gares[21],gares[22],115,18,1,2]

l49=[bifurcations[0],gares[11],140,4,1,2]
l50=[gares[11],gares[10],140,25,0,2]
l51=[gares[10],gares[9],140,27,0,1]

l52=[gares[9],bifurcations[1],160,34,1,2]
l53=[bifurcations[1],gares[8],160,8,1,2]

l54=[bifurcations[0],gares[17],160,17,1,2]
l55=[gares[17],gares[18],160,28,1,2]
l56=[gares[18],gares[19],115,51,1,2]
l57=[gares[19],gares[20],130,26,1,2]





Ligne_Roanne_Lyon = [l1, l2, l3, l4,l5,l6,l7,l8,l9]
Ligne_Roanne_SaintEtienne =[l10,l11,l12]
Ligne_Lyon_SaintEtienne=[l13,l14,l15,l16,l17,l18]
Ligne_Lyon_Macon=[l9,l8,l7,l19,l20,l21]
Ligne_Lyon_Valence=[l22,l23,l24,l25,l26]
Ligne_Lyon_Grenoble=[l27,l28,l29,l30,l31,l32,l33,l34,l35,l36]
Ligne_Valence_Grenoble=[l37,l38,l39,l40,l41,l42,l36]
Ligne_Grenoble_Chambery=[l43,l44,l45]
Ligne_Chambery_Annecy=[l46,l47,l48]
Ligne_Lyon_BourgEnBresse=[l9,l49,l50,l51]
Ligne_BourgEnBress_Macon=[l52,l53]
Ligne_Lyon_Chambery=[l9,l54,l55,l56,l57,l46]
Ligne_TGV=[] #je sais pas quoi/comment mettre les pts de départ et d'arrivée




