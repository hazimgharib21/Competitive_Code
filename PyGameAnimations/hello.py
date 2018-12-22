import pygame

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
running = 1
barheight = 124
y = 0
dir = 1

bgcolor = (0,0,0)
barcolor = []
for i in range(1, 63):
    barcolor.append((0,0,i*4))
for i in range(1, 63):
    barcolor.append((0,0,255 - i*4))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)
    for i in range(0, barheight):
        pygame.draw.aaline(screen, barcolor[i], (0,y+i), (width - 1, y + i))

    y += dir
    if y + barheight > 599 or y < 0:
        dir *= -1

    pygame.display.flip()
