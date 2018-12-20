import pygame

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
running = 1
barheight = 124
y = 0
dir = 1

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
    pygame.draw.line(screen, linecolor, (0,y), (width-1, y))

    y += dir
    if y == 0 or y == height -1:
        dir *= -1

    pygame.display.flip()
