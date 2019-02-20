import pygame

pygame.init()

#視窗設定
width = 400
height = 300
windowSide = [width,height]
screen = pygame.display.set_mode(windowSide)

#初始顏色
colour = pygame.color.Color('#F54455')
row = 0
done = False

while not done:
    increment = 30
    while row <= height:
        #一個矩形的寬為400(跟視窗一樣寬)，高為255/100
        pygame.draw.rect(screen,colour,(0,row,width,row + increment))
        pygame.display.flip()
        if colour[1] + increment < 255:
            colour[1] = int(increment) + colour[1]
        row += increment
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
        
