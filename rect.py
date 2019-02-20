import pygame

pygame.init()

windowSide = [400,300]
screen = pygame.display.set_mode(windowSide)
pygame.display.set_caption("Draw Rectangles")

colour = pygame.color.Color('#0A32F4')

done = False
while not done:
    #pygame.draw.rect(surface,color,rect,width=0)
    #rect:[x,y,寬,高]
    #width:線條的粗細,莫認為0,表示填充矩形內部
    pygame.draw.rect(screen,colour,[10,20,20,20])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
