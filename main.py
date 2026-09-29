import pygame,sys,threading,time
import boardClass, pieces
from menus import *

pygame.init()

# --- Constants ---

HEIGHT = 800
WIDTH = 1000
clock = pygame.time.Clock()
font = pygame.font.SysFont("comic sans", 30)
boldFont = pygame.font.SysFont("comic sans", 30)
boldFont.set_bold(True)
titleFont = pygame.font.SysFont("comic sans", 80)
titleFont.set_bold(True)

# Board class
#board = board.Board()
#board.setDefaultPos()
# the board class belongs to the menus.py now

#screen = pygame.display.set_mode((WIDTH,HEIGHT)) --> IMPORTED THROUGH MENUS.PY

activeMenu = mainMenu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP: # Check for mouse input
            # Get mouse coordinates
            mouseCoords  = pygame.mouse.get_pos()
            mouseX,mouseY = mouseCoords[0],mouseCoords[1]

            # run pressed() method on each button in menu, using mouse coordinates
            for button in activeMenu.buttons:
                newMenu = button.pressed(mouseX,mouseY) # assign possible new menu to a variable

                # if a menu is returned, set activemenu to be this new menu
                if newMenu != None:
                    activeMenu = newMenu

            # --- This is mouse check for BOARD EDITOR moving piece around ts ---
            if activeMenu == boardEditor:
                # Check if mouse coordinates are within the board display
                if mouseX >= 40 and mouseX <= 560 and mouseY >= 230 and mouseY <= 750:
                    # Remove board offset from coordinates
                    mouseX -= 40
                    mouseY -= 230

                    # Divide and truncate to get index value
                    mouseX = mouseX // 65
                    mouseY = mouseY // 65

                    # now make it do something
                    


    # draw here
    activeMenu.draw()

    # --- MENU SPECIFIC THINGS (LIKE LIVE BOARD UPDATE AND TIMERS) ---

    if activeMenu == boardEditor:
        for i in range(8):
            for j in range(8):
                if (j+i) % 2 == 0:
                    pygame.draw.rect(screen, (255,211,151), (40+(j*65),230+(i*65),65,65))
                else:
                    pygame.draw.rect(screen, (175, 116, 35), (40+(j*65),230+(i*65),65,65))
                if board.board[i][j] != 0:
                    screen.blit(pygame.transform.scale(board.board[i][j].sprite, (62,62)), (40+(j * 65), 230+(i * 65)))

    pygame.display.flip()
    clock.tick(30)