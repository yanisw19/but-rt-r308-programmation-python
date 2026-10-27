class Parking:

    def __init__(self,adresse,capacite,nb_portails, places_libres):
        self.adresse = adresse
        self.capacite = capacite
        self.nb_portails = nb_portails
        self.places_libres = places_libres

    def entree(self):
        if self.places_libres > 0 :
            self.places_libres -= 1
            return True
        return False

    def sortie(self):
        if self.places_libres < self.capacite :
            self.places_libres +=1
            return True
        return False

    def est_complet(self):
        return self.places_libres == 0

class Portail:
    def __init__(self,numero,parking):
        self.numero = numero
        self.parking = parking
        self.nb_entrees = 0
        self.nb_sorties = 0

    def Compte_Entree(self):
        if self.parking.entree():
            self.nb_entrees += 1
            return True
        return False
    
    def Compte_Sortie(self):
        if self.parking.sortie():
            self.nb_sorties -= 1
            return True
        return False
    