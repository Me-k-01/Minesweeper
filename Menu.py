from Button import *

class Menu :
    def __init__(self, cv, res=(100, 100), thm=["#373533", "#403e3c"] ):
        ( self.w, self.h) = res
        self.cv = cv
        self.thm = thm
        self.body = self.cv.create_rectangle( self.w * 3 // 4, 0, self.w, self.h, fill=self.thm[1], outline="")
        self.head = self.cv.create_rectangle( 0, 0, self.w, self.h//5, fill=self.thm[0], outline="")
