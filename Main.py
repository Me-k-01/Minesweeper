from tkinter import Tk, Canvas, PhotoImage
import sys

sys.path.append("./modules")
from UI import Menu
import Config, Game, Timer


def motion(event):
    """Runs everytime the cursor moves on the tkinter window."""
    coords = ( event.x, event.y )
    game.updateOnMotion(coords)
    playMenu.updateOnMotion(coords)
    mainMenu.updateOnMotion(coords)

def mousePress(event):
    """Runs everytime the left click of the mouse is pressed."""
    game.onClick()
    playMenu.updateOnPress()
    mainMenu.updateOnPress()

def mouseRelease(event):
    """Runs everytime the left click of the mouse is released."""
    playMenu.updateOnRelease()
    mainMenu.updateOnRelease()

#### Variables ####
width, height = 700, 700  # Taille de la fenetre
theme = Config.mainTheme["default"]
menuTheme = Config.bgTheme["night"]

#### Set up de la fenetre Tkinter ####
root = Tk()
cv = Canvas(root, width=width, height=height, bg=menuTheme[-1])
cv.pack()

timer = Timer.Timer(root, cv, width//2, height//6)

game = Game.Game(cv, (10, 150), 400, theme, timer)
game.start()

#### Creation du Menu principale ####
cv.create_rectangle( width * 3 // 4, 0, width, height, fill=menuTheme[1], outline="", tag="UI")
cv.create_rectangle( 0, 0, width, height//5, fill=menuTheme[0], outline="", tag="UI")

playMenu = Menu(cv, width - 400, height//5 , 200, 100, theme)
playMenu.selfDestruct = True

playMenu.addButton("New Game", game.start)
playMenu.addButton("Load"    , game.load)

mainMenu = Menu(cv, width - 200, height//5 , 200, 100, theme, [ playMenu ])
mainMenu.addButton( "Play"    , playMenu.start )
mainMenu.addButton( "Save"    , game.save )
mainMenu.addButton( "Help"  , lambda : print("comming soon") )
mainMenu.addButton( "Settings", lambda : print("comming soon") )
mainMenu.addButton( "Quit"    , root.destroy )

mainMenu.start()


cv.bind('<Motion>', motion)
cv.bind('<ButtonPress-1>', mousePress )
cv.bind('<ButtonRelease-1>', mouseRelease )

root.mainloop()
