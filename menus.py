import sys, pygame

import boardClass

board = boardClass.Board()
board.setDefaultPos()

# --- CONSTANTS ---

pygame.init()

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
activeMenu = None

font = pygame.font.SysFont("segoeuisymbol", 18)
boldFont = pygame.font.SysFont("segoeuisymbol", 30)
boldFont.set_bold(True)
titleFont = pygame.font.SysFont("segoeuisymbol", 80)
titleFont.set_bold(True)

# --- Classes and functions ---

def centeredMessage(txt, colour, x, y, chosenfont):
    textsurface = chosenfont.render(txt, True, colour)
    textrect = textsurface.get_rect()
    textrect.center = x, y
    screen.blit(textsurface, textrect)

class Button:  # button for the pygame menu buttons tingy
    def __init__(self, x, y, sizex, sizey, colour, text="", chosenfont=font, textcolour=(255, 255, 255),
                 connectedMenu=None, function=None, outlineColour=(255, 255, 255)):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.colour = colour
        self.text = text
        self.chosenfont = chosenfont
        self.textcolour = textcolour
        self.connectedMenu = connectedMenu
        self.function = function
        self.outlineColour = outlineColour
        self.outlineWidth = 4 # in pixels

    def draw(self):
        # button outline
        pygame.draw.rect(screen, self.outlineColour, (self.x - self.outlineWidth, self.y - self.outlineWidth,
                                                      self.sizex + self.outlineWidth*2, self.sizey + self.outlineWidth*2))

        # main button rectangle
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.sizex, self.sizey))
        # draw text
        centeredMessage(self.text, self.textcolour, self.x + (self.sizex / 2), self.y + (self.sizey / 2),
                        self.chosenfont)

    def pressed(self, mousex, mousey):  # check if button is clicked
        if mousex > self.x and mousex < self.sizex + self.x and mousey > self.y and mousey < self.sizey + self.y:
        # ^^^ All this does it check if the mouse coordinates are within the button's area ^^^

            if self.function != None:  # If there is a function to be run, then run it
                self.function()

            if self.connectedMenu != None: # If there is a connected menu to switch to, then switch to it
                print("HI")
                return self.connectedMenu

class Menu:
    def __init__(self, bgColour):
        self.bgColour = bgColour
        self.buttons = []

    def addButtons(self, buttons):
        for b in buttons:
            self.buttons.append(b)

    def draw(self):
        screen.fill(self.bgColour)
        for button in self.buttons:
            button.draw()

def closeGame():
    pygame.quit()
    sys.exit()

# ---  CREATING MENU OBJECTS ---

def createMainMenu():
    mainMenu = Menu((255,233,203))
    titleButton = Button(450, 100, 100, 100, (255,233,203), "c h e s s", titleFont, (0,0,0), outlineColour=(255,233,203))
    # ^ Title "button" is just used to display the title text, button colour is the same as the bg colour so it blends in

    # these are the main 2 play buttons in the middle
    playButton = Button(330,280,340,100,(255,204,135),"2 PLAYER", boldFont, (0,0,0), connectedMenu=None)
    playButtonAI = Button(330, 450, 340, 100, (255,204,135),"PLAYER VS AI", boldFont, (0,0,0), connectedMenu=None)

    # settings button
    settingsButton = Button(130,370,100,100,(255,204,135), "⚙️", titleFont, (0,0,0), connectedMenu=None)

    # quit button
    quitButton = Button(921,4,75,75,(255,204,135),"X", boldFont, (0,0,0), function=closeGame)

    mainMenu.addButtons([titleButton, playButton, playButtonAI, settingsButton, quitButton])
    return mainMenu

def createModeMenu(): # menu for choosing different mode
    modeSelector = Menu((255,233,203))

    # Title "button" is just used to display the title text, button colour is the same as the bg colour so it blends in
    titleButton = Button(450, 100, 100, 100, (255,233,203), "Choose Mode", titleFont, (0,0,0), outlineColour=(255,233,203))

    # -- standard button and text description ->
    standardButton = Button(80, 290, 170, 100, (255,204,135), "Standard", boldFont, (0,0,0),connectedMenu=gameplayMenu,function=board.setDefaultPos)
    #                                           ^^^ CHANGE CONNECTEDMENU TO GAMEPLAY MENU WHEN DONE
    standardDesc = Button(270,290, 630,100,(255,204,135),"Start the game with the standard chess starting position and regular rules",
                          font, (0,0,0))

    # custom board button
    customButton = Button(80,440,170,50,(255,204,135),"Custom",boldFont,(0,0,0),connectedMenu=boardEditor)
    customDesc = Button(270,440,630,50,(255,204,135), "Create your own custom position", font, (0,0,0))

    backButton = Button(5,5,50,50,(255,204,135),"<--",boldFont,(0,0,0),connectedMenu=mainMenu) 

    modeSelector.addButtons([titleButton, standardButton, standardDesc, customButton,customDesc, backButton])
    return modeSelector

def createSettingsMenu():
    settingsMenu = Menu((255,233,203))
  
    titleButton = Button(450, 100, 100, 100, (255,233,203), "Settings", titleFont, (0,0,0), outlineColour=(255,233,203))

    settingsButton1 = Button(290,290,330,60,(255,204,135),"im a setting", font,(0,0,0))
    tickBox1 = Button(650,290,60,60,(255,204,135)) # THIS has no text because it is dynamic. it might be tick or cross so cant add fixed value

    backButton = Button(5,5,50,50,(255,204,135),"<--",boldFont,(0,0,0),connectedMenu=mainMenu) 

    settingsMenu.addButtons([titleButton,settingsButton1,tickBox1,backButton])
    return settingsMenu

def createBoardEditor():
    boardEditor = Menu((255,233,203))

    titleButton = Button(450,90,100,100,(255,233,203), "edit board", titleFont,(0,0,0), outlineColour=(255,233,203))

    # this is board background, live board will be handled in main pygame loop
    boardBG = Button(25,215,550,550,(125,79,0),outlineColour=(255,233,203))

    # this is bg for the piece dragger part
    piecesBG = Button(610,215,360,370,(125,79,0),outlineColour=(255,233,203))

    # Button do set board to default position
    defaultPosButton = Button(650,603,160,80,(125,79,0),"Set Default Position", font, function=board.setDefaultPos)

    #clear board button
    clearButton = Button(835,603,100,80,(125,79,0),"Clear Board", font, function=board.clearBoard)

    playButton = Button(615,700,360,70,(126,217,87),"PLAY",boldFont,connectedMenu=gameplayMenu)

    backButton = Button(5,5,50,50,(255,204,135),"<--",boldFont,(0,0,0),connectedMenu=mainMenu)

    boardEditor.addButtons([titleButton,boardBG, piecesBG,defaultPosButton,clearButton,playButton,backButton])
    return boardEditor


def createGameplayMenu():
    gameplayMenu = Menu((255,233,203))

    # background for the move history list
    moveHistoryBG = Button(10,70,175,650,(125,79,0))

    boardBG = Button(200,55,660,660,(125,79,0))

    # background for live timer bar at bottom
    timerBar = Button(200,720,660,70,(125,79,0))
    whiteTimerBG = Button(430,725,95,60,(255,255,255),outlineColour=(125,79,0))
    blackTimerBG = Button(535,725,95,60,(0,0,0),outlineColour=(125,79,0))

    backButton = Button(5,5,50,50,(255,204,135),"<--",boldFont,(0,0,0),connectedMenu=mainMenu) 

    gameplayMenu.addButtons([moveHistoryBG,boardBG,timerBar,whiteTimerBG,blackTimerBG,backButton])
    return gameplayMenu
    
mainMenu = createMainMenu()
gameplayMenu = createGameplayMenu()
boardEditor = createBoardEditor()
settingsMenu = createSettingsMenu()
modeSelector = createModeMenu()

# After all menus are created, assign main menu buttons their respective connectedMenu

for button in mainMenu.buttons:
    match button.text:
        case "2 PLAYER":
            button.connectedMenu = modeSelector
        case "PLAYER VS AI":
            button.connectedMenu = modeSelector
        case "⚙️":
            button.connectedMenu = settingsMenu