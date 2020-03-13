import tkinter

class Smiley :
    def __init__(self, root, cns, x, y):
        self.cns = cns
        self.x = x
        self.y = y
        w = 50

        self.path = "./img/emoticons/" # Path
        self.emotions =  ["happy", "pokerface","bad","dead"]

        img = tkinter.PhotoImage(file = self.path + 'happy.png')


        self.cns.create_rectangle(self.x, self.y, w, w, fill="#1111AA")
        self.cns.create_image(self.x, self.y, image=img)

    def event(self, state):
        for emotion in self.emotions:
            if state == emotion:
                self.cns.create_image(self.x, self.y,image=self.path+emotion+".png")
