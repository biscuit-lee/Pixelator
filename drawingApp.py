import pygame as pg
import os
import tkinter
import tkinter.filedialog
# mode correlates to color that is drawn

#global mode
mode = 11

# window size
window_x = 0
window_y = 0

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
LBLUE = (207,238,250)
LRED = (255,204,203)
BROWN = (165,42,42)
GRAY = (142,142,142)
LYELLOW = (255,204,0)
ORANGE = (255,140,0)

# for fill function


def main():
    # ensure that we are in the working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)


    # window
    pg.font.init()
    print(os. getcwd())
    # define font
    myfont = pg.font.SysFont('Comic Sans MS', 11)

    saveImg = pg.image.load("images\saveImage.png")
    EraImg = pg.image.load("images\eraser.png")
    fillImg = pg.image.load("images\sfill.png")
    obFont = myfont.render("Simulate",False,(0,0,0))
    erase = myfont.render("Clear",False,(0,0,0))

    pg.init()
    mode = 4
    screen = pg.display.set_mode([795,500])
    createGrid(39,20)

    root = tkinter.Tk()
    root.withdraw()

    run = True
    global fil
    fil = False
    while run:
        for event in pg.event.get():

            if event.type==pg.QUIT:
                run=False
            else:
                
                # drawing mechanics
                if pg.mouse.get_pressed()[0]:

                    pos = pg.mouse.get_pos()
                    
                    pos_x = pos[0] // (20)
                    pos_y = (pos[1] - 100) //(20)

                    # catch error if user click outside of "drawing zone"
                    if (pos_x < 39 and pos[1] > 100):
                        if (fil == True):
                         
                            fill(grid,pos_y,pos_x,mode)
                        else:
                            grid[pos_y][pos_x] = mode
                        
                    else:

                        # if click save
                        if (15 < pos[0] < 15+50) and (15 < pos[1] < 15+40):
                        
                            # subsurface for saving
                            saveZone = pg.Rect(0,100,795,400)
                            sub = screen.subsurface(saveZone)
                            currdir = os.getcwd()
                           
                            # navigate window
                            tempdir = tkinter.filedialog.asksaveasfilename(defaultextension=".png")



                            if (0 < len(tempdir)):
                                # change dir to the directory that user wants to save
                                os.chdir(os.path.dirname(tempdir))
                      
                                # get file name
                                filename = os.path.basename(tempdir)
                                # save image
                                pg.image.save(sub,filename)
                                # change directory to original
                                os.chdir(currdir)
                              
                                

                        # if erase button is clicked
                        if (85 < pos[0] < 50+85) and (15 < pos[1] < 15+40):
                            eraseButton.color = GRAY
                            mode = 4
                            fil = False

                        # if fill button click
                        if (155 < pos[0] < 50+155) and (15 < pos[1] < 15+40):
                            fil = True

                        # colors buttons
                        elif (370 < pos[0] < 370+15) and (15 < pos[1] < 30):
                            mode = 1
                            fil = False
                        elif (370 < pos[0] < 370+15) and (35 < pos[1] < 35+15):
                            mode = 2
                        elif (350 < pos[0] <350+15) and (15 < pos[1] <15+15):
                            mode = 11
                            fil = False
                        elif (350 < pos[0] < 350+15) and (35 < pos[1] < 35+15):
                            mode = 9
                            fil = False
                        elif (390 < pos[0] < 390+15) and (15 < pos[1] <15+15):
                            mode = 6
                            fil = False
                        elif (390 < pos[0] < 390+15) and (35 < pos[1] < 35+15):
                            mode = 5
                            fil = False
                        elif (410 < pos[0] < 410+15) and (15 < pos[1] < 30):
                            mode = 12
                            fil = False
                        elif (410 < pos[0] < 410+15) and (35 < pos[1] < 35+15):
                            mode = 8
                            fil = False
                        elif (430 < pos[0] < 430+15) and (15 < pos[1] < 30):
                            mode = 7
                            fil = False
                        elif (430 < pos[0] < 430+15) and (35 < pos[1] < 35+15):
                            mode = 3
                            fil = False
                        elif (450 < pos[0] < 450+15) and (15 < pos[1] < 30):
                            mode = 10
                            fil = False
                        
                        # erase button
                        elif (350 < pos[0] < 390) and (20 < pos[1] < 265):
                            clear(grid)
        screen.fill(WHITE)
        
        drawGrid(screen,WHITE,20,5,5,grid)
        
        # draw text + buttons
        saveButton = Button(50,40,2,15,15,screen,WHITE)
 
        # erase button
        eraseButton = Button(50,40,4,85,15,screen,WHITE)
        
        # fill button
        fillButton = Button(50,40,4,155,15,screen,WHITE)

        # save icon
        screen.blit(saveImg,(10,5))
        screen.blit(EraImg,(80,5))
        screen.blit(fillImg,(150,5))
        # line
        line = pg.draw.line(screen,BLACK,(0,100),(800,100))

        # the colors buttons
        color1 = Button(15,15,11,350,15,screen,BLACK)
        color2 = Button(15,15,1,370,15,screen,RED)
        color3 = Button(15,15,2,370,35,screen,GREEN)
        color4 = Button(15,15,9,350,35,screen,PURPLE)
        color5 = Button(15,15,6,390,15,screen,LRED)
        color6 = Button(15,15,5,390,35,screen,LBLUE)

        color7 = Button(15,15,12,410,15,screen,ORANGE)
        color8 = Button(15,15,8,410,35,screen,GRAY)
        color9 = Button(15,15,7,430,15,screen,BROWN)
        color10 = Button(15,15,3,430,35,screen,YELLOW)
        color11 = Button(15,15,10,450,15,screen,LYELLOW)


        #color5 = Button(15,15,1,350,35,screen,RED)
        #color6 = Button(15,15,1,350,35,screen,RED)

        pg.display.update()

# class for all the drawing buttons
class Button():
    def __init__(self,width,height,mode,posx,posy,screen,color):
        self.width = width
        self.height = height
        self.mode = mode
        self.posx = posx
        self.posy = posy
        self.screen = screen    
        self.color = color
        rect = pg.Rect(posx,posy,width,height)
        pg.draw.rect(screen,color,rect)

# fill function
def fill(gri,posx,posy,mode):
    # base case
    if (gri[posx][posy] != 4):

        return
    if (posx < 0) or (posy < 0):
        return

    if (posx > 18) or (posy > 37):
        return

    if gri[posx][posy] == mode:
        return
    
    # color the grid
    gri[posx][posy] = mode
    
    # continue checking left , right, up and down of current x,y till med base case
    fill(grid,posx-1,posy,mode)
    fill(grid,posx+1,posy,mode)
    fill(grid,posx,posy-1,mode)
    fill(grid,posx,posy+1,mode)

#draw the grids on the window
def drawGrid(win,color,size,sx,sy,grid):
    syy = 0
    for y in range(20):
        sxx=sx
        for x in range(39):
            
            if grid[y][x] == 1:
                color = RED
            elif grid[y][x] == 2:
                color = GREEN
            elif grid[y][x] == 3:
                color = YELLOW
            elif grid[y][x] == 4:
                color = WHITE
            elif grid[y][x] == 5:
                color = LBLUE
            elif grid[y][x] == 6:
                color = LRED
            elif grid[y][x] == 7:
                color = BROWN
            elif grid[y][x] == 8:
                color = GRAY
            elif grid[y][x] == 9:
                color = PURPLE
            elif grid[y][x] == 10:
                color = LYELLOW
            elif grid[y][x] == 11:
                color = BLACK
            elif grid[y][x] == 12:
                color = ORANGE

            else:
                color=(255,255,255)
            rect = pg.Rect((x*size+sxx),(y*size+syy+100),size,size)
            pg.draw.rect(win,color,rect)
            #sxx+=sx

        #syy+=sy

# clear grid
def clear(grid):
    for i in range(len(grid)):
        for z in range(len(grid)):
            grid[i][z] = 4

#function that creates 2d list of the map
def createGrid(colDim,rowDim):
    global grid
    grid=[]
    for row in range(rowDim):
        grid.append([])
        for col in range(colDim):
            grid[row].append(4)


if __name__ == "__main__":
    main()