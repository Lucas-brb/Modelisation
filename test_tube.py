#-------------------------------------------------------------------------------
# Name:        test_tube
# Purpose:
#
# Author:      barbier lucas
#
# Created:     12/04/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Carac_trains import *
from acceleration_train import *
from Carac_trains import *

t1 = ['Roanne', 'Feurs', 95, 42, 0, 2]
t2 = ['Feurs', 'Saint Just Saint Rambert', 140, 32, 0, 2]
t3 = ['Saint Just Saint Rambert', 'Saint Etienne', 100, 14, 0, 2]
ligne = [t1, t2, t3]

print(temps_parcours_ligne(ligne, Ter_regiolis))