from random import randrange as rdm

def disp(M) :
    for l in M:
        for x in l:
            spacing = ""
            if ( x >= 0 ):
                spacing = " "
            print(spacing, x, end="")

        print()


class MineField :
    def __init__(self, n, p, nMine) :
        self.n = n
        self.p = p
        self.nMine = nMine


    def placeMine(self) :
        n, p = self.n, self.p

        def blankMatrice(n, p):
            matrice = []
            for i in range(n):
                matrice.append([])
                for j in range(p):
                    matrice[i].append(0)
            return matrice

        def addToAdj(m, x, y):

            container = [-1, 0, 1]
            for k in container:
                for h in container:
                    i = y+h
                    j = x+k
                    if ( 0 <= i < n and 0 <= j < p and m[i][j] >= 0):
                        m[i][j] += 1
            return m

        self.m = blankMatrice(self.n, self.p)

        while self.nMine > 0:
            x, y = rdm(self.n), rdm(self.p)
            if self.m[y][x] >= 0:
                self.m[y][x] = -1
                self.nMine -= 1
                self.m = addToAdj(self.m, x, y)

        disp(self.m)

class Game:
    def __init__(self, cv, theme):
        self.n = 10  # Hauteur
        self.p = 10  # Longueur
        self.bomb = 9 # Nombre de bombe
        self.mf = MineField(self.n, self.p, self.bomb)

        self.cv = cv
        self.theme = theme

    def changeDim(self, n, p):
        self.n = n
        self.p = p
        self.draw()

    def destroy(self):
        self.cv.delete("MineField")

    def draw(self, startAtCoord):
        w = 25 # Taille des blocks
        d = 2  # Distance de l'espacement entre chaque block.
        x, y = startAtCoord  # On commence a une certaine distance du bord de l'ecran.
        self.destroy()
        for i in range(self.n):
            for j in range(self.p):
                x += w + d
                self.cv.create_rectangle(x, y, x+w, y+w,fill=self.theme[0], outline="", tag="MineField")
            x = startAtCoord[0]
            y += w + d

    def start(self, startAt):
        self.mf.placeMine()
        self.draw(startAt)
