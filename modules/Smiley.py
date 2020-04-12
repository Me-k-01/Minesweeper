

class Smiley :
    def __init__(self, cns, x, y):
        from tkinter import PhotoImage
        self.cns = cns
        self.x = x
        self.y = y
        #w = 50
        #self.cns.create_rectangle(self.x - w//2, self.y - w//2, self.x + w//2, self.y + w//2, fill="#1111AA")

        self.ref = {} # Reference de toute les images d'emotions
        path = "./img/emoticons/"

        for state in ["happy"]: # ["happy", "pokerface","bad","dead"]
            img = PhotoImage(file = path + state + ".gif")
            self.ref[state] = img.subsample(5, 5)

        self.draw("happy")

    def draw(self, state):
        if not state in self.ref: return
        self.cns.create_image(self.x, self.y, image = self.ref[state])
