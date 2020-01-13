from random import randrange as rdm


class Game:
    def __init__(self):
        self.n = 5  # Hauteur
        self.p = 6  # Longueur
        self.bomb = 9 # Nombre de bombe
        self.m = [[]]

    def changeDim(self, n, p):
        self.n = n
        self.p = p

    def start(self):
        self.m = self.createMatrice()

    def createMatrice(self):
        m = []
        for i in range(0, self.n):
            m.append([])
            for j in range(0, self.p):
                if self.bomb > 0 and 1 == rdm(0, 7):
                    v = -1  # Est une bombe
                else:
                    v = 0
                m[i].append(v)
            print(m[i])

m = Game()
m.start()
