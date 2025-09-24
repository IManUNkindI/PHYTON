import pygame
import numpy as np
import time

#Pantalla
pygame.init()
width, height = 700, 700
screen = pygame.display.set_mode ((height, width))
#Fondo
bg = 15, 15, 15
screen.fill(bg)
#numero de celdas y dimensiones
nxC, nyC = 150, 150
dimCW = width / nxC
dimCH = height / nyC
#Estado de las celdas (Vivas = 1 / Muertas = 0)
gameState = np.zeros((nxC, nyC))
#Pausa
pause = True

#Bucle de ejecucion
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    
    ev = pygame.event.get()
    
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause
        click = pygame.mouse.get_pressed()
        if sum(click) > 0:
            posX, posY = pygame.mouse.get_pos()

            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not click[2]
            
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pause:
                #Numero de vecinos cercanos
                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC]+ \
                          gameState[(x)   % nxC, (y-1) % nyC]+ \
                          gameState[(x+1) % nxC, (y-1) % nyC]+ \
                          gameState[(x-1) % nxC, (y)   % nyC]+ \
                          gameState[(x+1) % nxC, (y)   % nyC]+ \
                          gameState[(x-1) % nxC, (y+1) % nyC]+ \
                          gameState[(x)   % nxC, (y+1) % nyC]+ \
                          gameState[(x+1) % nxC, (y+1) % nyC]

                #Regla 1: Una celula muerta con exactamente 3 vecinas vivas, "REVIVE"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                
                #Regla 2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "MUERE"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                
            #Poligono de cada celda
            poly=[((x)* dimCW, y * dimCH),
                  ((x+1) * dimCW, y * dimCH),
                  ((x+1) * dimCW, (y+1) * dimCH),
                  ((x) * dimCW, (y+1) * dimCH)]

            if newGameState[x, y]== 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
            
    gameState = np.copy(newGameState)
    
    pygame.display.flip()

    pass
