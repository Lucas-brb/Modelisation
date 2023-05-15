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

class File(object):
    def __init__(self):
        self.file = []
    def taille(self):
        return len(self.file)
    def entree(self,x):
        self.file.append(x)
    def sortie(self):
        if self.taille != 0 :
            self.file.pop(0)
    def voir(self):
        print(self.file)
    def dernier_elt(self):
        return self.file[0]
