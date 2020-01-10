from tkinter import Tk, Canvas, PhotoImage
from Button import *


width, height = 1200, 700
theme = ["#AA2323"]
cursor = { "x": 0, "y": 0 }

# App set up (app's root and window's canvas)
root = Tk()
cv = Canvas(root, width=width, height=height, bg="#343444")
cv.pack()








def drawCube(cv, x, y, w, h):
    cv.create_rectangle( x, y, x+w, y+h, fill="#ba2c23", outline="")
    cv.create_polygon([  x,  y+h,
                      x+20,  y+h+30,
                    x+w+20,  y+h+30,
                       x+w,  y+h ], fill="#cbad84", outline="")
    cv.create_polygon([  x+w,  y,
                      x+w+20, y+30,
                      x+w+20, y+h+30,
                         x+w, y+h ], fill="#181ebd", outline="")


drawCube(cv, cursor["x"]-50, cursor["y"] - 50, 100, 100)

# pour mettre une fonction qui a un parametre il faut mettre lambda:.
button = Button(cv, 0, 0, 200, 100, "yeeeeeet" )


def motion(event):
    cursor["x"], cursor["y"] = event.x, event.y
    button.onMotion(cursor)

def mousePress(event):
    button.onPress(cursor)

def mouseRelease(event):
    button.onRelease(cursor)

cv.bind('<Motion>', motion)
cv.bind('<ButtonPress-1>', mousePress )
cv.bind('<ButtonRelease-1>', mouseRelease )

root.mainloop()
