#données des trajets


gares = ['Lyon', 'Roanne', 'Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain', 'Villefranche', 'Mâcon', 'Bourg-en-Bresse', 'Villars', 'Sathonay', 'Givors', 'Rive de Gier', 'Saint Chamond', 'Saint Etienne', 'Feurs', 'Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly', 'Annecy', 'Chambéry', 'Montmélian', 'Grenoble université', 'Grenoble', 'Moirans', 'Voiron', 'Rives', 'Saint André', 'Tour du Pin', 'Bourgoin', "Isle d'Abeau", 'Vénissieux', 'Chasse sur Rhône', 'Vienne','Saint Rambert', 'Tain', 'Valence', 'Valence TGV', 'Romans', 'Mâcon-Loché-TGV','Crest']

chgmt_vitesse=['Oullins', 'Saint Just Saint Rambert', 'fin tronçon imposé nord', 'fin tronçon imposé sud']

bifurcations=['Lyon Saint Clair', 'Pont de Veyle', 'Saint-Quentin-Fallavier','Quincieux','Lyon nord']

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
l9=[bifurcations[0],gares[0],40,4,1,4]

l10=[gares[1],gares[16],95,42,0,2]
l11=[gares[16], chgmt_vitesse[1], 140,32,0,2]
l12=[chgmt_vitesse[1], gares[15],100,14,0,2]

l13=[gares[0],chgmt_nb_voies[0],40,2.5,1,4]
l14=[chgmt_nb_voies[0],chgmt_vitesse[0],90,5.5,1,2]
l15=[chgmt_vitesse[0],gares[12],115,16,1,2]
l16=[gares[12],gares[13],125,16,1,2]
l17=[gares[13],gares[14],125,10,1,2]
l18=[gares[14],gares[15],125,12,1,2]

l19=[bifurcations[3], gares[6],160, 1.6, 1, 4]
l20=[bifurcations[3],gares[7],160,15,1,2]
l21=[gares[7],gares[8],160,38,1,2]

l22=[gares[0], chgmt_vitesse[3],40,4,1,4]
l22bis=[chgmt_vitesse[3],gares[35],150,16,1,4]
l23=[gares[35],gares[36],120,10,1,2]
l24=[gares[36],gares[37],140,33,1,2]
l25=[gares[37],gares[38],140,27,1,2]
l26=[gares[38],gares[39],140,18,1,2]

l27=[gares[0],chgmt_vitesse[3],40,4,1,4]
l27bis=[chgmt_vitesse[3],gares[34],90,3,1,4]
l28=[gares[34],chgmt_nb_voies[1],160,4,1,3]
l28bis=[chgmt_nb_voies[1],bifurcations[2],160,12,1,2]
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

l58=[gares[42],bifurcations[4],300,60,1,2]
l59=[bifurcations[4],bifurcations[2],300,40,1,2]
l60=[bifurcations[2],gares[43],300,110,1,2]

l61=[bifurcations[4],gares[11],300,7,1,2]

_troncons_verif = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l22bis, l23, l24, l25, l26, l27, l27bis, l28, l28bis, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, l61]

#Récapitulatif des lignes et de leurs tronçons
#utilisation de la fonction python 'all' pour vérifier si tous les tronçons sont électrifiés, i.e si la ligne est electrifiée
# j'aurais besoin que vous me mettiez l'orientation des tronçons sur les lignes genre
# si la ligne est ligne_ville1_ville2 = [l1,l2,l3] il faudrait me mettre
# ligne_ville1_ville2 = [[l1,l2,l3], [True, True, False]] si l1 et l2 sont parcourus dans le sens direct, et l3 dans le sens indirect
Ligne_Roanne_Lyon = [[l1,l2,l3,l4,l5,l6,l7,l8,l9], [True, True, True, True, True, True, True, True, True], [all([l1[4],l2[4],l3[4],l4[4],l5[4],l6[4],l7[4],l8[4],l9[4]])]]

Ligne_Roanne_SaintEtienne = [[l10,l11,l12], [True, True, True], all([l10[4],l11[4],l12[4]])]

Ligne_Lyon_SaintEtienne=[[l13,l14,l15,l16,l17,l18], [True, True, True, True, True, True], all([l13[4],l14[4],l15[4],l16[4],l17[4],l18[4]])]

Ligne_Lyon_Macon=[[l9,l8,l7,l19,l20,l21], [False, False, False, False, True, True], all([l9[4],l8[4],l7[4],l19[4],l20[4],l21[4]])]

Ligne_Lyon_Valence=[[l22,l22bis,l23,l24,l25,l26], [True, True, True, True, True, True], all([l22[4],l22bis[4],l23[4],l24[4],l25[4],l26[4]])]

Ligne_Lyon_Grenoble=[[l27,l27bis,l28,l28bis,l29,l30,l31,l32,l33,l34,l35,l36], [True, True, True, True, True, True, True, True, True, True, True, True], all([l27[4],l27bis[4],l28[4],l28bis[4],l29[4],l30[4],l31[4],l32[4],l33[4],l34[4],l35[4],l36[4]])]

Ligne_Valence_Grenoble=[[l37,l38,l39,l40,l41,l42,l36], [True, True, True, True, True, True, True], all([l37[4],l38[4],l39[4],l40[4],l41[4],l42[4],l36[4]])]
Ligne_Grenoble_Chambery=[[l43,l44,l45], [True, True, True], all([l43[4],l44[4],l45[4]])]

Ligne_Chambery_Annecy=[[l46,l47,l48], [True, True, True], all([l46[4],l47[4],l48[4]])]

Ligne_Lyon_BourgEnBresse=[[l9,l49,l50,l51], [False, True, True, True], all([l9[4],l49[4],l50[4],l51[4]])]

Ligne_BourgEnBresse_Macon=[[l52,l53], [True, True], all([l52[4],l53[4]])]

Ligne_Lyon_Chambery=[[l9,l54,l55,l56,l57,l46], [False, True, True, True, True, False], all([l9[4],l54[4],l55[4],l56[4],l57[4],l46[4]])]



TGV_Creusot_Lyon=[[l49,l9], [False, True], all([l49[4],l9[4]])]

TGV_Lyon_Marseille=[[l27,l27bis,l28,l28bis],[True, True, True, True], all([l27[4], l27bis[4],l28[4],l28bis[4]])]

TGV_Lyon_Montpellier=[[l27,l27bis,l28,l28bis],[True, True, True, True], all([l27[4], l27bis[4],l28[4],l28bis[4]])]

TGV_Lille_Grenoble= [[l49,l9,l27,l27bis,l28,l28bis,l29,l30,l31,l32,l33,l34,l35,l36],[False, True, True, True, True, True, True, True, True, True, True, True, True, True],all([l49[4],l9[4],l27[4], l27bis[4],l28[4],l28bis[4],l29[4],l30[4],l31[4],l32[4],l33[4],l34[4],l35[4],l36[4]])]






troncons_lignes = {'Roanne-Lyon' : Ligne_Roanne_Lyon, 'Roanne-Saint-Etienne' : Ligne_Roanne_SaintEtienne, 'Lyon-Saint-Etienne' : Ligne_Lyon_SaintEtienne, 'Lyon-Macon' : Ligne_Lyon_Macon, 'Lyon-Valence' : Ligne_Lyon_Valence, 'Lyon-Grenoble' : Ligne_Lyon_Grenoble, 'Valence-Grenoble' : Ligne_Valence_Grenoble, 'Grenoble-Chambery' : Ligne_Grenoble_Chambery, 'Chambery-Annecy' : Ligne_Chambery_Annecy, 'Lyon-Bourg-en-Bresse' : Ligne_Lyon_BourgEnBresse, 'Bourg-en-Bresse-Macon' : Ligne_BourgEnBresse_Macon, 'Lyon-Chambery' : Ligne_Lyon_Chambery, 'TGV Creusot-Lyon' : TGV_Creusot_Lyon, 'TGV Lyon-Marseille' : TGV_Lyon_Marseille,'TGV Lyon-Montpellier' : TGV_Lyon_Montpellier,'TGV Lille-Grenoble':TGV_Lille_Grenoble,
'Lyon-Roanne' : [list(reversed(Ligne_Roanne_Lyon[0])), [not(_) for _ in Ligne_Roanne_Lyon[1]], Ligne_Roanne_Lyon[2]], 'StE-Roanne' : [list(reversed(Ligne_Roanne_SaintEtienne[0])), [not(_) for _ in Ligne_Roanne_SaintEtienne[1]], Ligne_Roanne_SaintEtienne[2]], 'StE-Lyon' : [list(reversed(Ligne_Lyon_SaintEtienne[0])), [not(_) for _ in Ligne_Lyon_SaintEtienne[1]], Ligne_Lyon_SaintEtienne[2]], 'Macon_Lyon' : [list(reversed(Ligne_Lyon_Macon[0])) , [not(_) for _ in Ligne_Lyon_Macon[1]], Ligne_Lyon_Macon[2]],'Valence-Lyon':[list(reversed(Ligne_Lyon_Valence[0])),[not(_) for _ in Ligne_Lyon_Valence[1]],Ligne_Lyon_Valence[2]],'Grenoble-Lyon':[list(reversed(Ligne_Lyon_Grenoble[0])),[not(_) for _ in Ligne_Lyon_Grenoble[1]],Ligne_Lyon_Grenoble[2]],'Grenoble-Valence':[list(reversed(Ligne_Valence_Grenoble[0])),[not(_) for _ in Ligne_Valence_Grenoble[1]],Ligne_Valence_Grenoble[2]], 'Chambéry-Grenoble':[list(reversed(Ligne_Grenoble_Chambery[0])),[not(_) for _ in Ligne_Grenoble_Chambery],Ligne_Grenoble_Chambery[2]],'Annecy-Chambéry':[list(reversed(Ligne_Chambery_Annecy[0])),[not(_) for _ in Ligne_Chambery_Annecy[1]],Ligne_Chambery_Annecy[2]], 'Bourg-en-Bresse-Lyon':[list(reversed(Ligne_Lyon_BourgEnBresse[0])),[not(_) for _ in Ligne_Lyon_BourgEnBresse[1]],Ligne_Lyon_BourgEnBresse[2]],'Macon-Bourg-en-Bresse':[list(reversed(Ligne_BourgEnBresse_Macon[0])),[not(_) for _ in Ligne_BourgEnBresse_Macon[1]],Ligne_BourgEnBresse_Macon[2]],'Chambery-Lyon':[list(reversed(Ligne_Lyon_Chambery[0])),[not(_) for _ in Ligne_Lyon_Chambery[1]],Ligne_Lyon_Chambery[2]],'TGV Lyon-Creusot':[list(reversed(TGV_Creusot_Lyon[0])),[not(_) for _ in TGV_Creusot_Lyon[1]],TGV_Creusot_Lyon[2]],'TGV Marseille-Lyon':[list(reversed(TGV_Marseille_Lyon[0])),[not(_) for _ in TGV_Marseille_Lyon[1]],TGV_Marseille_Lyon[2]],'TGV Montpellier-Lyon':[list(reversed(TGV_Lyon_Montpellier[0])),[not(_) for _ in TGV_Lyon_Montpellier[1]],TGV_Lyon_Montpellier[2]], 'TGV Grenoble-Lille':[list(reversed(TGV_Lille_Grenoble[0])),[not(_) for _ in TGV_Lille_Grenoble[1]], TGV_Lille_Grenoble[2]]} # a suivre

#Pour avoir toutes les lignes (dans les 2 sens), dans les lignes on inverse l'ordre des 'liens', pour le 2e terme de la ligne on change les True en False (et False en True) et le dernier terme n'est pas modifié








#gares déservies pour chaque ligne
#Sous forme de dictionnaire :
#mon_dico={'villedépart_villefin': 'gare_1, gare_2,...', 'ligne2':'gare1, gare2,...',...}

gares_deservables = {'Roanne_Lyon':[gares[2], gares[3], gares[4], gares[5], gares[6]], 'Roanne_StEtienne':[gares[16]],'Lyon_StEtienne':[gares[12],gares[13],gares[14]],'Lyon_Macon':[gares[6],gares[7]],'Lyon_Valence':[gares[35],gares[36],gares[37],gares[38]],'Lyon_Grenoble':[gares[34],gares[33],gares[32],gares[31],gares[30],gares[29],gares[28],gares[27]],'Valence_Grenoble':[gares[40],gares[41],gares[27]],'Grenoble_Chambery':[gares[25],gares[24]],'Chambery_Annecy':[gares[20],gares[21]],'Lyon_BourgEnBresse':[gares[11],gares[10]],'BourgEnBresse_Macon':[' '],'Lyon_Chambery':[gares[17],gares[18],gares[19],gares[20]],'Creusot_Lyon':[' '],'Lyon_Marseille':[' '], 'Lyon-Montpellier':[' '],'Lille_Grenoble':[gares[0]]}


#Nombre de voies par gare
nb_voies_gares = {'Lyon':11,'Roanne':3, 'Amplepuis':2, 'Tarare':2, 'Arbesle':4, 'Lozanne':4, 'Saint Germain':4, 'Villefranche':5, 'Mâcon':6, 'Bourg-en-Bresse':7, 'Villars':3, 'Sathonay':4, 'Givors':5, 'Rive de Gier':2, 'Saint Chamond':2, 'Saint Etienne':6, 'Feurs':2, 'Montluel':3, 'Ambérieu':6, 'Culoz':5, 'Aix-les-bains':5, 'Rumilly':2, 'Annecy':5, 'Chambéry':6, 'Montmélian':4, 'Grenoble université':4, 'Grenoble':7, 'Moirans':4, 'Voiron':2, 'Rives':3, 'Saint André':4, 'Tour du Pin':2, 'Bourgoin':3, "Isle d'Abeau":2, 'Vénissieux':3, 'Chasse sur Rhône':4, 'Vienne':5,'Saint Rambert':5, 'Tain':2, 'Valence':7, 'Valence TGV':7, 'Romans':2}
