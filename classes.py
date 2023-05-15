#-------------------------------------------------------------------------------
# Name:        classes
# Purpose:
#
# Author:      barbier lucas
#
# Created:     05/05/2023
# Copyright:   (c) barbi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Pile(object):
    def __init__(self):
        self.pile = []
    def taille(self):
        return len(self.pile)
    def empile(self,x):
        self.pile.append(x)
    def depile(self):
        if self.taille != 0 :
            self.pile.pop()
    def voir(self):
        print(self.pile)
