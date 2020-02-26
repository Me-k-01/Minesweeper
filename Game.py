from random import randrange as rdm

def disp(M) :
    for l in M:
        for d in l:
            x = d["value"]
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
                    matrice[i].append({"value": 0, "visible": False}) # state: 0 = invisible | 1 = visible
            return matrice

        def addToAdj(m, x, y):

            container = [-1, 0, 1]
            for k in container:
                for h in container:
                    i = y+h
                    j = x+k
                    if ( 0 <= i < n and 0 <= j < p and m[i][j]["value"] >= 0):
                        m[i][j]["value"] += 1
            return m

        self.m = blankMatrice(self.n, self.p)

        while self.nMine > 0:
            x, y = rdm(self.n), rdm(self.p)
            if self.m[y][x]["value"] >= 0:
                self.m[y][x]["value"] = -1
                self.nMine -= 1
                self.m = addToAdj(self.m, x, y)

        disp(self.m)

class Game:
    def __init__(self, cv, theme):
        self.n = 10  # Hauteur
        self.p = 10  # Longueur
        self.bomb = 3# Nombre de bombe

        self.xOffset, self.yOffset = 0, 0  # coordonnés a partir duquelle on peut dessiner le champ de mine
        self.width, self.height = 0, 0  # Taille du champ de mine

        self.blockLength = 40 # Taille des blocks
        self.blockSpace = 2 # Taille en comprenant l'espacement

        self.cv = cv
        self.theme = theme

        self.selectionIndex = (0, 0)
        self.cheat = False  # le cheat est de base inactif
        self.mf = MineField(self.n, self.p, self.bomb)


    def changeDim(self, n, p):
        self.n = n
        self.p = p
        self.draw()

    def destroy(self):
        self.cv.delete("MineField")
        self.cv.delete("MF_Selection")

    def draw(self, offset=None):
        """Dessin initial du champ de mine sur le canvas"""
        w = self.blockLength
        d = self.blockSpace + w # Distance de l'espacement
        mid = d//2

        # On commence a une certaine distance du bord de l'ecran.
        if offset == None:
            offset = ( self.xOffset, self.yOffset )
        else:
            ( self.xOffset, self.yOffset ) = offset

        self.width, self.height  = d*(self.n-1), d*(self.p-1)  # Taille du champ de mine
        x, y = offset


        self.destroy()  # On supprime le precedant champ de mine du canvas

        for i in range(self.n):
            for j in range(self.p):
                if not self.mf.m[i][j]["visible"]:
                    self.cv.create_rectangle(x, y, x+w, y+w,fill=self.theme[0], outline="", tag="MineField")
                else:
                    self.cv.create_rectangle(x, y, x+w, y+w,fill="#AAAAAA", outline="", tag="MineField")
                    self.cv.create_text(x+mid, y+mid+5, fill=self.theme[0],font="Arial 20", text=self.mf.m[i][j]["value"], tag="MineField")

                x += d
            x = self.xOffset
            y += d

    def start(self, startAt):
        self.mf.placeMine()
        self.draw(startAt)

    def select(self, i=None, j=None):
        self.cv.delete("MF_Selection")

        if i == None:
            i, j = self.selectionIndex
        else:
            self.selectionIndex = (i, j)

        case = self.mf.m[i][j]

        space = self.blockSpace
        w = self.blockSpace + self.blockLength

        x = w*j + self.xOffset
        y = w*i + self.yOffset



        if ( case["visible"] ): # Révélé
            self.cv.create_rectangle(x-space, y-space, x+w, y+w, fill="#AAAAAA", outline="", tag="MF_Selection")
            self.cv.create_text(x+w//2, y+w//2+5, fill=self.theme[0],font="Arial 20", text=self.mf.m[i][j]["value"], tag="MineField")
        else:  # Quand la case n'a pas deja ete revelé
            self.cv.create_rectangle(x-space, y-space, x+w, y+w,fill=self.theme[2], outline="", tag="MF_Selection")


    def updateOnMotion(self, coords):
        """Update on click"""
        x, y = coords
        cursorOffset = -12
        x += cursorOffset
        y += cursorOffset

        if ( self.xOffset < x < self.xOffset + self.width and self.yOffset < y < self.yOffset + self.height ):

            x, y = x-self.xOffset, y-self.yOffset # On commence a 0, 0
            j, i = x // self.blockLength,  y // self.blockLength # On normalise les coordonnés en index


            self.select(i, j)
        print(self.selectionIndex)

    def reveal(self, list):
        """Affichage de toute les case au alentour lorsque l'on tombe sur une valeur de zero"""
        # TODO: affichage de toute les case au alentour

        container = [-1, 0, 1]
        cases = []

        print(list)
        for indexCouple in list:
            i, j = indexCouple
            for k in container:
                for h in container:
                    iNext, jNext = i+k, j+h
                    if ( 0 <= iNext < self.n and 0 <= jNext < self.p):  # Si on est dans les limites du bord de l'ecran
                        case = self.mf.m[iNext][jNext]  # La nouvelle case a decouvrir

                        if not case["visible"]:  # Si c'est une case qui n'a pas deja ete decouverte

                            case["visible"] = True
                            if case["value"] == 0:  # Si c'est encore une case nulle,
                                # On ajoute une prochaine verification a effectuer.
                                cases.append((iNext, jNext))


        self.draw()
        if cases != []:
            self.reveal(cases)

    def onClick(self):

        i, j = self.selectionIndex
        case = self.mf.m[i][j]

        if not case["visible"]:  # Si on avait pas deja clické sur cette case
            case["visible"] = True
            if case["value"] == 0:
                self.reveal([(i, j)])
            elif case["value"] < 0:
                # TODO: On perd
                pass
            self.draw()

    def onRelease(self):
        pass
