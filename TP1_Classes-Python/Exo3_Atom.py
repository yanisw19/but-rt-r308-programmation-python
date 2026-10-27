class Atom:
    # Attributs de classe : masse_neutron(float) : valeur fixe = 1,675e-27 kg et masse_proton(float) : 1.673e-27 kg , capacite_couche1(int) : valeur fixe = 2 (capacité de la 1ère couche électronique)  , capacite_couche(int) : valeur fixe = 8 (capacité des couches suivantes)
    # Attributs d'instance : symbole(str), A (int) : Non vide représente le nombre de nucléons  et Z(int) : Représente le nombre de charge

    masse_neutron = 1.675e-27
    masse_proton = 1.673e-27
    capacite_couche1 = 2
    capacite_couche = 8


    #2 Constructeur
    def __init__(self, symbole, A, Z):
        self.symbole = symbole
        self.A = A
        self.Z = Z


    #3 Masse totale
    def masse(self):
        nb_neutrons = self.A - self.Z
        return (self.Z * self.masse_proton) + (nb_neutrons * self.masse_neutron)


    # 4. Nombre d'électrons sur la couche externe
    def NbElecExt(self):
        nb_electrons = self.Z

        if nb_electrons <= self.capacite_couche1:
            return nb_electrons

        nb_electrons = nb_electrons - self.capacite_couche1

        while nb_electrons > self.capacite_couche:
            nb_electrons = nb_electrons - self.capacite_couche

        return nb_electrons


    # 5. Même famille
    def memeFamille(self, elem):
        return self.NbElecExt() == elem.NbElecExt()


    # 6. Isotope
    def isotope(self, elem):
        return self.Z == elem.Z and self.A != elem.A