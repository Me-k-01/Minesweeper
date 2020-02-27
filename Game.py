from random import randrange as rdm
import Save as IE
import Timer

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

    def placeMine(self, i=None, j=None) :
        n, p = self.n, self.p
        mineToPlace = self.nMine
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

        while mineToPlace > 0:
            x, y = rdm(self.n), rdm(self.p)

            if i == None:
                i = -1
                j = -1


            if not ( ( y-1 <= i <= y+1) and ( x-1 <= j <= x+1) ):  # Quand la bombe est assez loin du curseur
                case = self.m[y][x]
                if case["value"] >= 0:
                    case["value"] = -1
                    self.m = addToAdj(self.m, x, y)

                    mineToPlace -= 1
        #disp(self.m)







class Game:
    def __init__(self, cv, offset, theme, time=None):
        self.n = 10  # Hauteur
        self.p = 10  # Longueur
        self.bomb = 9# Nombre de bombe

        self.xOffset, self.yOffset = offset # coordonnés a partir duquelle on peut dessiner le champ de mine
        self.width, self.height = 0, 0  # Taille du champ de mine

        self.blockLength = 40 # Taille des blocks
        self.blockSpace = 2 # Taille en comprenant l'espacement

        self.cv = cv
        self.theme = theme

        self.firstClick = True
        self.selectionIndex = None
        self.cheat = False  # le cheat est de base inactif
        self.mf = MineField(self.n, self.p, self.bomb)

        if time != None:
            self.timer = time

    def changeDim(self, n, p):
        self.n = n
        self.p = p
        self.start()

    def destroy(self):
        self.cv.delete("MineField")
        self.cv.delete("MF_Selection")

    def draw(self):
        """Dessin initial du champ de mine sur le canvas"""
        w = self.blockLength
        d = self.blockSpace + w # Distance de l'espacement
        mid = d//2

        self.width, self.height  = (d + self.blockSpace)*(self.n-1)  , (d + self.blockSpace)*(self.p-1)  # Taille du champ de mine
        x, y = self.xOffset, self.yOffset


        self.destroy()  # On supprime le precedant champ de mine du canvas

        for i in range(self.n):
            for j in range(self.p):
                case = self.mf.m[i][j]
                if case["visible"]:
                    if case["value"] >= 0:
                        self.cv.create_rectangle(x, y, x+w, y+w,fill="#AAAAAA", outline="", tag="MineField")
                        self.cv.create_text(x+mid, y+mid+5, fill=self.theme[0],font="Arial 20", text=case["value"], tag="MineField")
                    else: # Si c'est une bombe
                        self.cv.create_rectangle(x, y, x+w, y+w,fill="#AA3233", outline="", tag="MineField")
                        self.cv.create_text(x+mid, y+mid+8, fill=self.theme[0],font="Arial 20", text="*", tag="MineField")
                else:
                    self.cv.create_rectangle(x, y, x+w, y+w,fill=self.theme[0], outline="", tag="MineField")
                x += d
            x = self.xOffset
            y += d

    def start(self):
        self.firstClick = True
        self.mf.placeMine()
        self.draw()
        if self.timer != None:
            self.timer.restart()

    def save(self):
        data = [self.mf, self.timer.initialTime]
        IE.save(data)

    def load(self):
        data = IE.load()
        if data != -1:  # Si on a pas eut d'erreur
            self.mf = data[0]
            self.firstClick = False
            self.timer.initialTime = data[1]
            self.draw()
        else:
            print("Loading error")


    def select(self, i=None, j=None):
        self.cv.delete("MF_Selection")

        if i == None:
            self.selectionIndex = None
            return
        else:
            self.selectionIndex = (i, j)

        case = self.mf.m[i][j]

        space = self.blockSpace
        w = self.blockSpace + self.blockLength

        x = w*j + self.xOffset
        y = w*i + self.yOffset



        if ( case["visible"] ): # Si c'est un case revelé
            if case["value"] < 0:  # Si c'est une bombe
                self.cv.create_rectangle(x-space, y-space, x+w, y+w,fill="#AA3233", outline="", tag="MF_Selection")
                self.cv.create_text(x+w//2, y+ w//2 +8, fill=self.theme[0],font="Arial 20", text="*", tag="MF_Selection")
            else:
                self.cv.create_rectangle(x-space, y-space, x+w, y+w, fill="#AAAAAA", outline="", tag="MF_Selection")
                self.cv.create_text(x+w//2, y+ w//2 +5, fill=self.theme[0],font="Arial 20", text=case["value"], tag="MF_Selection")

        else:  # Quand la case n'a pas deja ete revelé
            self.cv.create_rectangle(x-space, y-space, x+w, y+w,fill=self.theme[2], outline="", tag="MF_Selection")

    def reveal(self, list):
        """Affichage de toute les case au alentour lorsque l'on tombe sur une valeur de zero"""

        container = [-1, 0, 1]
        cases = []

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

    def loose(self):
        """Lorsque l'on perd"""
        for i in range(self.n):
            for j in range(self.p):
                case = self.mf.m[i][j]
                if case["value"] < 0:
                    case["visible"] = True
        self.draw()


    def updateOnMotion(self, coords):
        """Update on click"""
        x, y = coords
        cursorOffset = -10
        x += cursorOffset
        y += cursorOffset

        if ( self.xOffset <= x <= self.xOffset + self.width  and self.yOffset <= y <= self.yOffset + self.height ):

            x, y = x-self.xOffset, y-self.yOffset # On commence a 0, 0
            j, i = x // self.blockLength,  y // self.blockLength # On normalise les coordonnés en index

            if (i, j) != self.selectionIndex:
                self.select(i, j)
        else:
            self.select()

    def onClick(self):
        if self.selectionIndex != None:  # Si on a une selection
            i, j = self.selectionIndex

            if self.firstClick: # Si c'est ble premier clique,
                self.firstClick = False
                self.mf.placeMine(i, j)  # On place les mine en fonction de l'emplacement du clique

            case = self.mf.m[i][j]

            if not case["visible"]:  # Si on avait pas deja clické sur cette case
                case["visible"] = True
                if case["value"] == 0:
                    self.reveal([(i, j)])
                elif case["value"] < 0:
                    self.loose()
                self.draw()
