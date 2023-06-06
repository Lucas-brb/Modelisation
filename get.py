#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      barbier lucas
#
# Created:     31/05/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from donnees_lignes import *
from plan_transport_1h import *
from Carac_trains import *

Ajout_train(plan,lignesOK)
#plan = [['Roanne-Lyon', 'Roanne-Saint-Etienne', 'Lyon-Saint-Etienne', 'Lyon-Macon', 'Lyon-Valence', 'Lyon-Grenoble', 'Valence-Grenoble', 'Grenoble-Chambery', 'Chambery-Annecy', 'Lyon-Bourg-en-Bresse', 'Bourg-en-Bresse-Macon', 'Lyon-Chambery', 'TGV Creusot-Lyon', 'TGV Lyon-Marseille', 'TGV Lyon-Montpellier', 'TGV Lille-Grenoble', 'Lyon-Roanne', 'StE-Roanne', 'StE-Lyon', 'Macon_Lyon', 'Valence-Lyon', 'Grenoble-Lyon', 'Grenoble-Valence', 'Chambéry-Grenoble', 'Annecy-Chambéry', 'Bourg-en-Bresse-Lyon', 'Macon-Bourg-en-Bresse', 'Chambery-Lyon', 'TGV Lyon-Creusot', 'TGV Marseille-Lyon', 'TGV Montpellier-Lyon', 'TGV Grenoble-Lille'], [[0, 25, 25, 40, 40, 58, 58, 66, 66, 76.4, 78.0, 78.0, 89.0, 92.0, 96.0], [0, 42, 42, 74, 88], [0, 2.5, 8.0, 24.0, 24.0, 40.0, 40.0, 50.0, 50.0, 62.0], [0, 4, 7, 18, 18, 19.6, 34.6, 34.6, 72.6], [0, 4, 20, 20, 30, 30, 63, 63, 90, 90, 108], [0, 4, 7, 7, 11, 23, 37, 37, 43, 43, 58, 58, 65, 65, 91, 91, 101, 101, 107, 107, 127], [0, 11, 11, 21, 21, 35, 40, 43.4, 68.4, 68.4, 88.4], [0, 6, 6, 52, 52, 67], [0, 14, 14, 34, 34, 52], [0, 4, 8, 8, 33, 33, 60], [0, 34, 42], [0, 4, 21, 21, 49, 49, 100, 100, 126, 126, 140], [0, 4, 8], [0, 4, 7, 11, 23], [0, 4, 7, 11, 23], [0, 4, 8, 8, 12, 15, 19, 31, 45, 51, 66, 73, 99, 109, 115, 135], [0, 4, 7, 18, 18, 19.6, 30.0, 30.0, 38.0, 38.0, 56.0, 56.0, 71.0, 71.0, 96.0], [0, 14, 46, 46, 88], [0, 12, 12, 22, 22, 38, 38, 54, 59.5, 62.0], [0, 38, 53, 53, 54.6, 54.6, 65.6, 68.6, 72.6], [0, 18, 18, 45, 45, 78, 78, 88, 88, 104, 108], [0, 20, 20, 26, 26, 36, 36, 62, 62, 69, 69, 84, 84, 90, 90, 104, 116, 120, 120, 123, 127], [0, 20, 20, 45, 48.4, 53.4, 67.4, 67.4, 77.4, 77.4, 88.4], [0, 15, 15, 61, 61, 67], [0, 18, 18, 38, 38, 52], [0, 27, 52, 52, 56, 60], [0, 8, 42], [0, 14, 14, 40, 40, 91, 91, 119, 119, 136, 140], [0, 4, 8], [0, 12, 16, 19, 23], [0, 12, 16, 19, 23], [0, 20, 26, 36, 62, 69, 84, 90, 104, 116, 120, 123, 127, 127, 131, 135]], [[0, 14.567007268121483, 16.567007268121483, 25.41972882195725, 27.41972882195725, 37.986736090078736, 39.986736090078736, 44.83945764391451, 46.83945764391451, 51.74542058833694, 52.431134874051224, 54.431134874051224, 59.32969041106625, 63.82969041106625, 69.82969041106625], [0, 26.90437972948718, 28.90437972948718, 43.17033913910086, 51.57033913910086], [0, 3.842146696078001, 7.5915310444773, 15.970415530933144, 17.970415530933145, 26.020134451017192, 28.020134451017192, 33.189853371101236, 35.189853371101236, 41.31957229118528], [0, 6.090607591731187, 10.590607591731187, 15.691079166225041, 17.69107916622504, 18.889912499558374, 24.665258301673624, 26.665258301673624, 41.66166121079343], [0, 6.090607591731187, 12.968184616785129, 14.968184616785129, 20.363752675101786, 22.363752675101786, 37.049398576502696, 39.049398576502696, 51.16361590647504, 53.16361590647504, 61.42069037930452], [4, 10.090607591731187, 12.191790626807823, 14.191790626807823, 16.438790626808196, 20.949202008889518, 26.199202008889518, 28.199202008889518, 32.34835015703766, 34.34835015703766, 40.719753066157466, 42.719753066157466, 46.8689012143056, 48.8689012143056, 60.55454711570651, 62.55454711570651, 67.38305015996457, 69.38305015996457, 72.4972674899369, 74.4972674899369, 83.61148481990924], [0, 5.257074472829483, 7.257074472829483, 12.08557751708754, 14.08557751708754, 20.628366275631308, 22.77122341848845, 24.228366275631306, 34.942651989917024, 36.942651989917024, 46.056869319889365], [0, 3.1142173299723406, 5.114217329972341, 25.371291802801824, 27.371291802801824, 33.74269471192163], [5, 12.9380864776751, 14.9380864776751, 25.69610990109245, 27.69610990109245, 37.410655063640235], [4, 10.10682650177269, 13.573011686958294, 15.573011686958294, 27.103521361122244, 29.103521361122244, 41.49117389242905], [0, 13.496402909119809, 16.49640290911981], [9, 15.090607591731187, 22.052108726221675, 24.052108726221675, 35.298511635341484, 37.298511635341484, 64.27249866234285, 66.27249866234285, 78.73597919381983, 80.73597919381983, 88.7095325428265], [0, 1.4497354497354498, 7.449735449735449], [4, 10.18122707853152, 12.313628798978666, 14.006402743318613, 18.506402743318613], [0, 6.181227078531521, 8.313628798978666, 10.006402743318613, 14.506402743318613], [5, 6.449735449735449, 12.44973544973545, 18.44973544973545, 24.63096252826697, 26.763364248714115, 28.456138193054063, 32.95613819305406, 38.20613819305406, 40.45613819305406, 46.08113819305406, 48.54410115601702, 59.68695829887417, 63.97267258458845, 66.54410115601702, 75.11552972744559], [0, 6.090607591731187, 10.590607591731187, 15.691079166225041, 17.69107916622504, 18.889912499558374, 23.379897410485597, 25.379897410485597, 30.262421291569172, 32.26242129156917, 42.859230886938455, 44.859230886938455, 53.741754768022034, 55.741754768022034, 70.33856436339133], [0, 8.815237415509364, 22.710628944433502, 24.710628944433502, 51.615008673920684], [0, 6.129718920084046, 8.129718920084045, 13.29943784016809, 15.29943784016809, 23.349156760252136, 25.349156760252136, 33.8390642416405, 37.29996959143474, 41.04996959143474], [0, 14.996402909119809, 20.62140290911981, 22.62140290911981, 24.78573624245308, 26.78573624245308, 31.778260450732297, 36.2782604507323, 42.2782604507323], [0, 8.257074472829483, 10.257074472829483, 22.371291802801824, 24.371291802801824, 39.05693770420274, 41.05693770420274, 46.452505762519394, 48.452505762519394, 55.216840184970486, 61.216840184970486], [5, 14.02024865870815, 16.020248658708148, 19.040497317416296, 21.040497317416296, 25.77503169041016, 27.77503169041016, 39.366708920546884, 41.366708920546884, 44.56631724373214, 46.56631724373214, 52.7659255669174, 54.7659255669174, 57.59053389010266, 59.59053389010266, 65.41514221328792, 69.91514221328792, 71.41514221328792, 73.41514221328792, 75.43548952217705, 81.43548952217705], [0, 9.114217329972341, 11.114217329972341, 22.371291802801828, 23.828434659944683, 25.971291802801826, 31.971291802801826, 33.97129180280183, 38.799794847059886, 40.799794847059886, 46.05686931988937], [0, 6.3714029091198086, 8.371402909119809, 28.628477381949292, 30.628477381949292, 33.74269471192163], [0, 9.756595722653538, 11.756595722653538, 22.556669706176642, 24.556669706176642, 32.530223055183306], [0, 12.387652531306808, 23.10193824559252, 25.10193824559252, 28.381827134481654, 34.381827134481654], [0, 3.57460832318526, 16.32460832318526], [0, 7.973553349006666, 9.973553349006666, 22.437033880483636, 24.437033880483636, 51.411020907485, 53.411020907485, 64.65742381660482, 66.65742381660482, 73.50104894794686, 79.50104894794686], [0, 6.092146696078002, 8.097216945747423], [0, 4.5, 5.635416666666667, 7.429655349794239, 13.429655349794238], [4, 8.5, 9.635416666666666, 11.429655349794238, 17.42965534979424], [0, 9.020248658708152, 11.591677230136723, 15.87739151585101, 27.020248658708155, 29.671868591464, 35.296868591464005, 37.546868591464005, 42.796868591464005, 47.296868591464005, 48.43228525813067, 50.22652394125824, 56.22652394125824, 62.22652394125824, 68.31867063733624, 70.32374088700566]], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
"""plan = [['Roanne-Lyon',
  'Roanne-Saint-Etienne',
  'Lyon-Saint-Etienne',
  'Lyon-Macon',
  'Lyon-Valence',
  'Lyon-Grenoble',
  'Valence-Grenoble',
  'Grenoble-Chambery',
  'Chambery-Annecy',
  'Lyon-Bourg-en-Bresse',
  'Bourg-en-Bresse-Macon',
  'Lyon-Chambery',
  'Lyon-Annecy',
  'TGV Creusot-Lyon',
  'TGV Lyon-Marseille',
  'TGV Lyon-Montpellier',
  'TGV Lille-Grenoble',
  'Lyon-Roanne',
  'StE-Roanne',
  'StE-Lyon',
  'Macon_Lyon',
  'Valence-Lyon',
  'Grenoble-Lyon',
  'Grenoble-Valence',
  'Chambéry-Grenoble',
  'Annecy-Chambéry',
  'Bourg-en-Bresse-Lyon',
  'Macon-Bourg-en-Bresse',
  'Chambery-Lyon',
  'Annecy-Lyon',
  'TGV Lyon-Creusot',
  'TGV Marseille-Lyon',
  'TGV Montpellier-Lyon',
  'TGV Grenoble-Lille'],
 [[0, 0, 25, 25, 40, 40, 58, 58, 66, 66, 76.4, 78.0, 78.0, 89.0, 92.0, 96.0],
  [0, 0, 42, 42, 74, 88],
  [0, 0, 2.5, 8.0, 24.0, 24.0, 40.0, 40.0, 50.0, 50.0, 62.0],
  [0, 0, 4, 7, 18, 18, 19.6, 34.6, 34.6, 72.6],
  [0, 0, 4, 20, 20, 30, 30, 63, 63, 90, 90, 108],
  [0,
   0,
   4,
   7,
   7,
   11,
   23,
   37,
   37,
   43,
   43,
   58,
   58,
   65,
   65,
   91,
   91,
   101,
   101,
   107,
   107,
   127],
  [0, 0, 11, 11, 21, 21, 35, 40, 43.4, 68.4, 68.4, 88.4],
  [0, 0, 6, 6, 52, 52, 67],
  [0, 0, 14, 14, 34, 34, 52],
  [0, 0, 4, 8, 8, 33, 33, 60],
  [0, 0, 34, 42],
  [0, 0, 4, 21, 21, 49, 49, 100, 100, 126, 126, 140],
  [0, 0, 4, 21, 21, 49, 49, 100, 100, 126, 126, 146, 146, 164],
  [0, 4, 8],
  [0, 0, 4, 7, 11, 23],
  [0, 0, 4, 7, 11, 23],
  [0, 4, 8, 8, 12, 15, 19, 31, 45, 51, 66, 73, 99, 109, 115, 135],
  [0,
   0,
   4,
   7,
   18,
   18,
   19.6,
   30.0,
   30.0,
   38.0,
   38.0,
   56.0,
   56.0,
   71.0,
   71.0,
   96.0],
  [0, 0, 14, 46, 46, 88],
  [0, 0, 12, 12, 22, 22, 38, 38, 54, 59.5, 62.0],
  [0, 0, 38, 38, 53, 54.6, 54.6, 65.6, 68.6, 72.6],
  [0, 0, 18, 18, 45, 45, 78, 78, 88, 88, 104, 108],
  [0,
   0,
   20,
   20,
   26,
   26,
   36,
   36,
   62,
   62,
   69,
   69,
   84,
   84,
   90,
   90,
   104,
   116,
   120,
   120,
   123,
   127],
  [0, 0, 20, 20, 45, 48.4, 53.4, 67.4, 67.4, 77.4, 77.4, 88.4],
  [0, 0, 15, 15, 61, 61, 67],
  [0, 0, 18, 18, 38, 38, 52],
  [0, 0, 27, 27, 52, 52, 56, 60],
  [0, 0, 8, 42],
  [0, 0, 14, 14, 40, 40, 91, 91, 119, 119, 136, 140],
  [0, 0, 18, 18, 38, 38, 64, 64, 115, 115, 143, 143, 160, 164],
  [0, 0, 4, 8],
  [0, 12, 16, 19, 23],
  [0, 12, 16, 19, 23],
  [0, 0, 20, 26, 36, 62, 69, 84, 90, 104, 116, 120, 123, 127, 127, 131, 135]],
 [[-10,
   0,
   14.567007268121483,
   16.567007268121483,
   25.41972882195725,
   27.41972882195725,
   37.986736090078736,
   39.986736090078736,
   44.83945764391451,
   46.83945764391451,
   51.74542058833694,
   52.431134874051224,
   54.431134874051224,
   59.32969041106625,
   63.82969041106625,
   69.82969041106625],
  [-10,
   0,
   26.90437972948718,
   28.90437972948718,
   43.17033913910086,
   51.57033913910086],
  [-10,
   0,
   3.842146696078001,
   7.5915310444773,
   15.970415530933144,
   17.970415530933145,
   26.020134451017192,
   28.020134451017192,
   33.189853371101236,
   35.189853371101236,
   41.31957229118528],
  [-10,
   0,
   6.090607591731187,
   10.590607591731187,
   15.691079166225041,
   17.69107916622504,
   18.889912499558374,
   24.665258301673624,
   26.665258301673624,
   41.66166121079343],
  [-10,
   0,
   6.092146696078002,
   12.840896315568783,
   14.840896315568783,
   20.186786000490088,
   22.186786000490088,
   36.77846323062681,
   38.77846323062681,
   50.79871188933496,
   52.79871188933496,
   60.961817690900254],
  [-5,
   5,
   11.090607591731187,
   13.191790626807823,
   15.191790626807823,
   17.438790626808196,
   21.949202008889518,
   27.199202008889518,
   29.199202008889518,
   33.34835015703766,
   35.34835015703766,
   41.719753066157466,
   43.719753066157466,
   47.8689012143056,
   49.8689012143056,
   61.55454711570651,
   63.55454711570651,
   68.38305015996457,
   70.38305015996457,
   73.4972674899369,
   75.4972674899369,
   84.61148481990924],
  [-10,
   0,
   5.257074472829483,
   7.257074472829483,
   12.08557751708754,
   14.08557751708754,
   20.628366275631308,
   22.77122341848845,
   24.228366275631306,
   34.942651989917024,
   36.942651989917024,
   46.056869319889365],
  [-10,
   0,
   3.1142173299723406,
   5.114217329972341,
   25.371291802801824,
   27.371291802801824,
   33.74269471192163],
  [-10,
   0,
   7.973553349006666,
   9.973553349006666,
   20.77362733252977,
   22.77362733252977,
   32.530223055183306],
  [7,
   17,
   23.10682650177269,
   26.573011686958292,
   28.573011686958292,
   40.10352136112224,
   42.10352136112224,
   54.491173892429046],
  [-10, 0, 13.324608323185261, 16.32460832318526],
  [-2,
   8,
   14.092146696078002,
   20.880424598736997,
   22.880424598736997,
   33.95503292192225,
   35.95503292192225,
   62.88696938881786,
   64.88696938881786,
   77.28174709950132,
   79.28174709950132,
   87.21983357717642],
  [-6,
   4,
   10.090607591731187,
   17.052108726221675,
   19.052108726221675,
   30.298511635341484,
   32.298511635341484,
   59.272498662342855,
   61.272498662342855,
   73.73597919381983,
   75.73597919381983,
   86.53605317734294,
   88.53605317734294,
   98.29264889999648],
  [0, 1.4497354497354498, 7.449735449735449],
  [-10,
   0,
   6.181227078531521,
   8.313628798978666,
   10.006402743318613,
   14.506402743318613],
  [-6,
   4,
   10.18122707853152,
   12.313628798978666,
   14.006402743318613,
   18.506402743318613],
  [5,
   6.449735449735449,
   12.44973544973545,
   18.44973544973545,
   24.63096252826697,
   26.763364248714115,
   28.456138193054063,
   32.95613819305406,
   38.20613819305406,
   40.45613819305406,
   46.08113819305406,
   48.54410115601702,
   59.68695829887417,
   63.97267258458845,
   66.54410115601702,
   75.11552972744559],
  [-10,
   0,
   6.090607591731187,
   10.590607591731187,
   15.691079166225041,
   17.69107916622504,
   18.889912499558374,
   23.379897410485597,
   25.379897410485597,
   30.262421291569172,
   32.26242129156917,
   42.859230886938455,
   44.859230886938455,
   53.741754768022034,
   55.741754768022034,
   70.33856436339133],
  [-10,
   0,
   8.815237415509364,
   22.710628944433502,
   24.710628944433502,
   51.615008673920684],
  [-10,
   0,
   6.129718920084046,
   8.129718920084045,
   13.29943784016809,
   15.29943784016809,
   23.349156760252136,
   25.349156760252136,
   33.8390642416405,
   37.29996959143474,
   41.04996959143474],
  [-10,
   0,
   14.82460832318526,
   16.82460832318526,
   22.86217960933348,
   23.547893895047768,
   25.547893895047768,
   30.446449432062796,
   34.94644943206279,
   40.94644943206279],
  [-10,
   0,
   8.257074472829483,
   10.257074472829483,
   22.371291802801824,
   24.371291802801824,
   39.05693770420274,
   41.05693770420274,
   46.452505762519394,
   48.452505762519394,
   55.216840184970486,
   61.216840184970486],
  [-5,
   5,
   14.02024865870815,
   16.020248658708148,
   19.040497317416296,
   21.040497317416296,
   25.77503169041016,
   27.77503169041016,
   39.366708920546884,
   41.366708920546884,
   44.56631724373214,
   46.56631724373214,
   52.7659255669174,
   54.7659255669174,
   57.59053389010266,
   59.59053389010266,
   65.41514221328792,
   69.91514221328792,
   71.41514221328792,
   73.41514221328792,
   75.43548952217705,
   81.43548952217705],
  [-1,
   9,
   18.11421732997234,
   20.11421732997234,
   31.371291802801828,
   32.82843465994468,
   34.97129180280183,
   40.97129180280183,
   42.97129180280183,
   47.799794847059886,
   49.799794847059886,
   55.05686931988937],
  [-10,
   0,
   6.1996083231852595,
   8.19960832318526,
   28.362714124750553,
   30.362714124750553,
   33.3829627834587],
  [-10,
   0,
   9.714545162547784,
   11.714545162547784,
   22.472568585965135,
   24.472568585965135,
   32.410655063640235],
  [-10,
   0,
   12.387652531306808,
   14.387652531306808,
   25.918162205470757,
   27.918162205470757,
   31.19805109435989,
   37.19805109435989],
  [-10, 0, 3.7464029091198086, 16.49640290911981],
  [-6,
   4,
   11.973553349006666,
   13.973553349006666,
   26.437033880483636,
   28.437033880483636,
   55.411020907485,
   57.411020907485,
   68.65742381660482,
   70.65742381660482,
   77.50104894794686,
   83.50104894794686],
  [-6,
   4,
   13.714545162547784,
   15.714545162547784,
   26.472568585965135,
   28.472568585965135,
   40.86734629664859,
   42.86734629664859,
   69.7992827635442,
   71.7992827635442,
   82.87389108672946,
   84.87389108672946,
   91.54572163213695,
   97.54572163213695],
  [2, 12, 18.18122707853152, 20.271605575644955],
  [4, 8.5, 9.635416666666666, 11.429655349794238, 17.42965534979424],
  [0, 4.5, 5.635416666666667, 7.429655349794239, 13.429655349794238],
  [-10,
   0,
   9.258504040449647,
   11.829932611878219,
   16.115646897592505,
   27.25850404044965,
   29.900254341063224,
   35.525254341063224,
   37.775254341063224,
   43.025254341063224,
   47.525254341063224,
   48.66067100772989,
   50.45490969085746,
   56.45490969085746,
   62.45490969085746,
   68.63613676938898,
   70.72651526650242]],
 [['Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain'],
  ['Feurs'],
  ['Givors', 'Rive de Gier', 'Saint Chamond'],
  ['Saint Germain', 'Villefranche'],
  ['Chasse sur Rhône', 'Vienne', 'Saint Rambert', 'Tain'],
  ['Vénissieux',
   "Isle d'Abeau",
   'Bourgoin',
   'Tour du Pin',
   'Saint André',
   'Rives',
   'Voiron',
   'Moirans'],
  ['Valence TGV', 'Romans', 'Moirans'],
  ['Grenoble université', 'Montmélian'],
  ['Aix-les-bains', 'Rumilly'],
  ['Sathonay', 'Villars'],
  [],
  ['Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains'],
  ['Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly'],
  [],
  [],
  [],
  ['Lyon'],
  ['Amplepuis', 'Tarare', 'Arbesle', 'Lozanne', 'Saint Germain'],
  ['Feurs'],
  ['Givors', 'Rive de Gier', 'Saint Chamond'],
  ['Saint Germain', 'Villefranche'],
  ['Chasse sur Rhône', 'Vienne', 'Saint Rambert', 'Tain'],
  ['Vénissieux',
   "Isle d'Abeau",
   'Bourgoin',
   'Tour du Pin',
   'Saint André',
   'Rives',
   'Voiron',
   'Moirans'],
  ['Valence TGV', 'Romans', 'Moirans'],
  ['Grenoble université', 'Montmélian'],
  ['Aix-les-bains', 'Rumilly'],
  ['Sathonay', 'Villars'],
  [],
  ['Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains'],
  ['Montluel', 'Ambérieu', 'Culoz', 'Aix-les-bains', 'Rumilly'],
  [],
  [],
  [],
  ['Lyon']],
 ['Regiolis',
  'Autorail',
  'Regiolis',
  '2N',
  'Regiolis',
  '2N',
  '2N',
  '2N',
  '2N',
  'Autorail',
  'Regiolis',
  'Regiolis',
  '2N',
  'TGV',
  'TGV',
  'TGV',
  'TGV',
  '2N',
  'Autorail',
  'Regiolis',
  'Regiolis',
  '2N',
  'Regiolis',
  '2N',
  'Regiolis',
  'Regiolis',
  'Autorail',
  '2N',
  '2N',
  'Regiolis',
  'TGV',
  'TGV',
  'TGV',
  'TGV']]"""
def g_e_t(ligne, plan):
    plt.close()
    troncons  = troncons_lignes[ligne]
    km = 0
    dist_cor_troncons = []
    for t in troncons[0]:
        dist_cor_troncons.append([km, km + t[3]])
        km += t[3]
    aff = [] # on crée la liste de tous les trajets à afficher sur le get
    # on cherche dans toutes les lignes lesquelles correspondent à celle qu'on considère (quelque soit le sens) ou celles qui ont des tronçons en commun avec la ligne considérée
    for ind_ligne in range(len(plan[0])) :
        label_l = plan[0][ind_ligne]
        if plan[0][ind_ligne] == ligne : # si c'est la même ligne parcourue dans le même sens

            # on ajoute la liste des heures et distances dans la variable d'affichage
            aff.append([plan[2][ind_ligne], plan[1][ind_ligne], label_l, couleurs_lignes[ligne]])

        elif troncons_lignes[plan[0][ind_ligne]][0] == list(reversed(troncons[0])) : # si c'est la même ligne dans l'autre sens

            # on prend la distance totale pour pouvoir afficher dans le bon sens
            dist_tot = plan[1][ind_ligne][-1]
            km_parcourus = []

            # on prend les km dans le sens décroissant
            for dist in plan[1][ind_ligne] :
                km_parcourus.append(dist_tot - dist)
            aff.append([plan[2][ind_ligne], km_parcourus, label_l, couleurs_lignes[ligne]])
        else :
            # si la ligne est différente, on cherche si elle a des tronçons en commun avec celle dont on veut tracer le get
            aff_temp0 = []
            aff_temp1 = []
            for ind_t_commun in range(len(troncons[0])) : # on parcours les tronçons de la ligne du get
                if troncons[0][ind_t_commun] in troncons_lignes[plan[0][ind_ligne]][0]: # si le tronçon est aussi dans la liste des tronçons de la ligne considérée

                    # recuperation de l'indice du tronçon dans la ligne considérée
                    i_t_ligneetuidee = troncons_lignes[plan[0][ind_ligne]][0].index(troncons[0][ind_t_commun])

                    # on prend le tronçon commun
                    troncon_commun = troncons_lignes[plan[0][ind_ligne]][0][i_t_ligneetuidee]

                    #on prend les heures d'entrée et sortie de ce tronçon sur cette ligne
                    heure_e, heure_s = entree_sortie_troncon(plan[2][ind_ligne], plan[1][ind_ligne], plan[0][ind_ligne])[1][i_t_ligneetuidee]

                    if troncons_lignes[plan[0][ind_ligne]][1][i_t_ligneetuidee] == troncons[1][ind_t_commun]: # si le tronçon est parcouru dans le même sens que le tronçon de la ligne get

                        # on ajoute les heures et les distances dans le même sens

                        aff_temp0.append(heure_e)
                        aff_temp0.append(heure_s)
                        aff_temp1.append(dist_cor_troncons[ind_t_commun][0])
                        aff_temp1.append(dist_cor_troncons[ind_t_commun][1])
                        '''
                        aff.append([[heure_e, heure_s], dist_cor_troncons[ind_t_commun], label_l, couleurs_lignes[plan[0][ind_ligne]]])
                        '''
                    else: # si il n'est pas parcouru dans le même sens

                        # on inverse les distances

                        aff_temp0 = [heure_e, heure_s] + aff_temp0
                        aff_temp1 = [dist_cor_troncons[ind_t_commun][1], dist_cor_troncons[ind_t_commun][0]] + aff_temp1
                        '''
                        aff.append([[heure_e, heure_s], list(reversed(dist_cor_troncons[ind_t_commun])), label_l, couleurs_lignes[plan[0][ind_ligne]]])
                        '''
            if len(aff_temp0) != 0:
                aff.append([aff_temp0, aff_temp1, label_l, couleurs_lignes[plan[0][ind_ligne]]])
    axes = plt.axes()
    for t in aff :
        plt.plot(t[0], t[1], label = t[2], color = t[3])
    plt.axhline(y = 0 , linestyle = '--', color = 'grey', linewidth = 0.5)
    for w in dist_cor_troncons:
        plt.axhline(y = w[1], linestyle = '--', color = 'grey', linewidth = 0.5)
    distances, gares = dist_noeuds_ligne(troncons[0], troncons[1])
    axes.set_yticks(distances)
    axes.set_yticklabels(gares)
    axes.set_xticks([k*60 for k in range(18)])
    axes.set_xticklabels(['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'])
    plt.xticks(rotation = 90)
    plt.legend()
    plt.show()
    plt.close()

g_e_t(plan[0][0],plan)

""".0

axes = plt.axes()
plt.plot(heures, distances)
gares = ['Roanne', 'Feurs', 'Saint Just Saint Rambert', 'Saint Etienne']
heures = ['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
axes.set_yticks([0, 42, 74, 88])
axes.set_xticks([k*60 for k in range(18)])
axes.set_yticklabels(gares)
axes.set_xticklabels(heures)
plt.xlim(0,17*60)
plt.xticks(rotation = 90)
plt.show()
time.sleep(1)
plt.close()
g_e_t(plan[0][0],plan)
"""