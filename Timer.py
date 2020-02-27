from time import time

class Timer:
    def __init__(self, root, cv, x, y, ):
        self.root = root
        self.cv = cv

        self.x = x
        self.y = y

        self.initialTime = time()
        self.wdg = None
        self.updating()


    def updating(self):
        t = int(time() - self.initialTime)

        if self.wdg != None:
            self.cv.delete(self.wdg)

        self.wdg = self.cv.create_text(self.x, self.y, fill="#AAAAAA",font="Arial 20", text=t)
        self.root.after(200, self.updating)

    def restart(self):
        self.initialTime = time()
