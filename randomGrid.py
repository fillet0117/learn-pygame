import random
import pygame

pygame.init()

width = 400
height = 300
windowSide = [width,height]
screen = pygame.display.set_mode(windowSide)
clock = pygame.time.Clock()

sqrw = width / 10
sqrh = height / 10

done = False

while not done:
    red = random.randrange(0,256)
    blue = random.randrange(0,256)
    green = random.randrange(0,256)
    #生成從0到400的間格為10的隨機整數
    x = random.randrange(0,width,sqrw)
    y = random.randrange(0,height,sqrh)
    pygame.draw.rect(screen,(red,blue,green),(x,y,sqrw,sqrh))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(10)

pygame.quit()
    
