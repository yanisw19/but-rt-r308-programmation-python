class Intervalle:
    """ Cette classe représente un intervalle avec les 13 relations possible de l'Algèbre d'Allen
Les bornes sont stockées dans les variables deb (d) et fin (f)."""

    #Question 1
    def __init__(self,deb,fin):
        assert deb <= fin # Respecte la condition initiale
        self.deb = deb
        self.fin = fin
    def __str__(self):
        return f"[{self.deb}, {self.fin}]"
    
    #Question 2
    
    def e(self,y):
        """ X = Y """
        return (self.deb == y.deb) and (self.fin == y.fin)

    #Question 3

    def b(self,y):
        """ X avant Y """
        return self.fin < y.deb

    def m(self,y):
        """ Y qui commence à X fin """
        return self.fin == y.fin
    

    def o(self, y):
        """ X chevauche Y """
        return (self.deb > y.deb) and (y.deb < self.fin) and (self.fin < y.fin)
    
    def s(self,y):
        """ Quand X commence Y commence """
        return (self.deb == y.deb) and (self.fin < y.fin)
    
    def f(self,y):
        """ Y se termine X se termine """
        return (self.deb > y.deb) and (self.fin == y.fin)

    def d(self,y):
        """ X commence et se termine avant """
        return (self.deb > y.fin) and (self.fin < y.fin)
    

    #Question 4
    def bi(self,y):
        """ X après Y avant X"""
        return y.b(self)








if __name__ == "__main__":
    x = Intervalle(1, 3)
    y = Intervalle(5, 8)
    print(x, "avant", y, "?", x.b(y))
 
    x = Intervalle(5, 8)
    y = Intervalle(1, 3)
    print(x, "après", y, "?", x.bi(y))
 
    x = Intervalle(1, 5)
    y = Intervalle(5, 9)
    print(x, "précède", y, "?", x.m(y))
 
    x = Intervalle(1, 6)
    y = Intervalle(4, 9)
    print(x, "chevauche", y, "?", x.o(y))
 
    x = Intervalle(2, 5)
    y = Intervalle(2, 8)
    print(x, "commence", y, "?", x.s(y))
 
    x = Intervalle(5, 9)
    y = Intervalle(2, 9)
    print(x, "termine", y, "?", x.f(y))
 
    x = Intervalle(4, 6)
    y = Intervalle(2, 9)
    print(x, "pendant", y, "?", x.d(y))
 
    x = Intervalle(3, 7)
    y = Intervalle(3, 7)
    print(x, "égal", y, "?", x.e(y))