#-------------------------------------------------------------------------------
# Name:        Class_train
# Purpose:     Définir la classe des trains
#
# Author:      barbier lucas
#
# Created:     20/03/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Train:
    def __init__(self, masse, RAV_A, RAV_B, RAV_C, v_max, Matrice_vitesse_effort , nbe_passagers):
        self.masse = masse
        self.RAV_A = RAV_A
        self.RAV_B = RAV_B
        self.RAV_C = RAV_C
        self.v_max = v_max
        self.M_v_e = Matrice_vitesse_effort
        self.nbe_passagers = nbe_passagers
