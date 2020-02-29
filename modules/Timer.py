from time import time
from datetime import timedelta as timeFormater

class Timer:
    def __init__(self, root, cv, x, y):
        self.root = root
        self.cv = cv

        self.x = x
        self.y = y

        self.initialTime = time()
        self.timeWhenSaved = None
        self.timeWhenLoading = None

        self.cv.create_rectangle(x-75, y-25, x+75, y+25, fill="#9592b4", outline="", tag="Timer")
        self.id = None
        self.updating()

    def save(self):
        return [self.initialTime, time()]

    def load(self, data):
        initialTime, timeWhenSaved = data
        deltaTime = time() - timeWhenSaved
        self.initialTime = initialTime + deltaTime


    def updating(self):
        t = int(time() - self.initialTime)

        if self.id != None:
            self.cv.delete(self.id)

        txt = timeFormater(seconds=t)
        self.id = self.cv.create_text(self.x, self.y, fill="#141417",font="Arial 22", text=txt, tag="Timer")
        self.root.after(200, self.updating)

    def restart(self):
        self.initialTime = time()
