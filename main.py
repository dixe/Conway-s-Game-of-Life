import pygame,sys
from Grid import *
from Cell import *
from pygame.locals import *

def run_game():
    screen_height=400
    screen_width=400
    screen = pygame.display.set_mode((screen_height, screen_width),0,32)
    BG_COLOR = 255,255,255
    clock=pygame.time.Clock()
    cell_image="cell.png"
    world = Grid(screen,40,40,cell_image)
    world.setCell(5,5,True)
    world.setCell(6,5,True)
    world.setCell(7,5,True)
    world.setCell(8,6,True)
    world.setCell(6,6,True)
    world.setCell(7,6,True)
    world.setCell(5,10,True)
    world.setCell(6,5,True)
    world.setCell(7,10,True)
    world.setCell(8,10,True)
    world.setCell(6,6,True)
    world.setCell(7,6,True)
    world.setCell(20,6,True)
    world.setCell(20,7,True)
    world.setCell(21,6,True)
    world.setCell(21,7,True)
    world.setCell(22,9,True)
    world.setCell(22,8,True)
    world.setCell(23,9,True)
    world.setCell(23,8,True)
    screen.fill(BG_COLOR)
    count =0
    while True: # main game loop
        time_passed = clock.tick(3)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for i in range(world.getRows()):
            for j in range(world.getCols()):
                world.getCell(i,j).blitme()
        world.updateCells()
        pygame.display.update()


run_game()