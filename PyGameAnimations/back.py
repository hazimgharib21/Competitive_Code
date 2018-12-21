import pygame

red = input("Enter red color: ")
blue = input("Enter blue color: ")
green = input("Enter green color: ")

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((int(red), int(green),int(blue)))
    pygame.display.flip()
