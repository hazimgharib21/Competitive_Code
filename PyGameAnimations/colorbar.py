import pygame

running = 1
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

barheight = 124
redMove = 5
greenMove = 3
blueMove = 1
redPos = 0
greenPos = 0
bluePos = 0
dir = 1
barSize = width // 3

bgcolor = (0,0,0)
blueBar = []
redBar = []
greenBar = []
for i in range(1, 63):
    blueBar.append((0,0,i*4))
    redBar.append((i*4,0,0))
    greenBar.append((0,i*4,0))
for i in range(1, 63):
    blueBar.append((0,0,255 - i*4))
    redBar.append((255 - i*4,0,0,))
    greenBar.append((0,255 - i*4,0))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)
    for i in range(0, barheight):
        pygame.draw.aaline(screen, blueBar[i], (0,bluePos + i), (barSize, bluePos + i))
        pygame.draw.aaline(screen, greenBar[i], (barSize,greenPos + i), (barSize * 2, greenPos + i))
        pygame.draw.aaline(screen, redBar[i], (barSize * 2,redPos + i), (width, redPos + i))

    redPos += redMove
    if redPos + barheight > 599 or redPos < 0:
        redMove *= -1
    bluePos += blueMove
    if bluePos + barheight > 599 or bluePos < 0:
        blueMove *= -1
    greenPos += greenMove
    if greenPos + barheight > 599 or greenPos < 0:
        greenMove *= -1

    pygame.display.flip()
