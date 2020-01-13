from tkinter import Tk, Canvas, PhotoImage
from Menu import *
import Config, Game

#### Variables ####
width, height = 700, 700
theme = Config.mainTheme["default"]
menuTheme = Config.bgTheme["night"]
cursor = { "x": 0, "y": 0 }  # on stockera les coordonnées du cursor dans un dictionaire pour forcer le passage par reference.
#### Set up de la fenetre Tkinter ####
root = Tk()
cv = Canvas(root, width=width, height=height, bg=menuTheme[-1])
cv.pack()

def createButton(buttonArray, thm):
    """Fonction quit creer une liste de boutton"""

    # Pour mettre une fonction qui a un parametre il faut mettre lambda:
    buttonArray.append( Button(cv, width - 200, height//5 , 200, 100, "Play", lambda : print("comming soon"), thm ) )
    buttonArray.append( Button(cv, width - 200, height//5 + 100, 200, 100, "Help",  lambda : print("comming soon"), thm ) )
    buttonArray.append( Button(cv, width - 200, height//5 + 200, 200, 100, "Scores",  lambda : print("comming soon"), thm ) )
    buttonArray.append( Button(cv, width - 200, height//5 + 300, 200, 100, "Settings",  lambda : print("comming soon"), thm ) )
    buttonArray.append( Button(cv, width - 200, height//5 + 300, 200, 100, "Quit", root.destroy , thm ) )


menu = Menu(cv, (width, height), menuTheme)
menu.buttonArray = []  # On place la liste des bouttons dans l'objet menu pour que cette variable soit accessible et modifiable partout car cela force le passage par reference dans la mainloop de tkinter.
createButton(menu.buttonArray, theme)

def motion(event):
    """Runs everytime the cursor moves on the tkinter window."""
    cursor["x"], cursor["y"] = event.x, event.y
    for b in menu.buttonArray: # Pour chaque boutton dans la liste de boutton

        b.onMotion(cursor) # On execute la fonction associé à l'évènement.

def mousePress(event):
    """Runs everytime the left click of the mouse is pressed."""
    for b in menu.buttonArray:
        b.onPress(cursor)

def mouseRelease(event):
    """Runs everytime the left click of the mouse is released."""
    for b in menu.buttonArray:
        b.onRelease(cursor)

cv.bind('<Motion>', motion)
cv.bind('<ButtonPress-1>', mousePress )
cv.bind('<ButtonRelease-1>', mouseRelease )

root.mainloop()
