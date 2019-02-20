import pygame

#初始化pygame
pygame.init()

#設定視窗大小
windowSize = [500,500]
screen = pygame.display.set_mode(windowSize)

#設定視窗標題
pygame.display.set_caption("Circles")

#設定顏色
colour = pygame.color.Color('#AAAAAA')

done = False
while not done:
    pygame.draw.circle(screen,colour,[250,250],50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
