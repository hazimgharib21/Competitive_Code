import pygame

# Change variable below to get different results
resolution = 800
offset = 5
totalPoints = 50 

# Loading screen and environment variable
print("Loading Screen...")
screen = pygame.display.set_mode((resolution + offset, resolution + offset))
clock = pygame.time.Clock()
running = 1
WHITE = (255,255,255)

# Loading and calculating variables
print("Loading Calculations...")
size = resolution // totalPoints
widhtValue = 0
heightValue = resolution
widhtPoint = []
for i in range(totalPoints):
    widhtPoint.append(widhtValue + offset)
    widhtValue += size
    heightValue -= size
widhtPoint.append(widhtValue)
heightPoint = widhtPoint[::-1] 

count = 0
countPattern = 1

# Load the window
print("Loading Pygame Window...")
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    clock.tick(60)
    if (count == 0) and (countPattern == 1):
        screen.fill((0, 0, 0))
    for i in range(len(widhtPoint)):
        if(i > count):
            break
        if(countPattern == 1):
            pygame.draw.aaline(screen, WHITE, (widhtPoint[i],offset),(offset,heightPoint[i]))
        elif(countPattern == 2):
            pygame.draw.aaline(screen, WHITE,(widhtPoint[i],offset),(resolution,widhtPoint[i]))
        elif(countPattern == 3):
            pygame.draw.aaline(screen,WHITE,(resolution,widhtPoint[i]),(heightPoint[i],resolution))
        elif(countPattern == 4):
            pygame.draw.aaline(screen, WHITE,(offset,heightPoint[i]),(heightPoint[i], resolution))
        
                           
    pygame.display.flip()
    if(count < len(widhtPoint)):
        count += 1
    else:
        count = 0
        if(countPattern < 4):
            countPattern += 1
        else:
            countPattern = 1
    
