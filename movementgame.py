import pygame
import random
pygame.init()

#設定視窗大小
windowSize = [400,300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

#角色起始位置
x = int(windowSize[0] / 2)
y = int(windowSize[1] / 2)

#球的起始位置
ballX = random.randrange(0,windowSize[0])
ballY = random.randrange(0,windowSize[1])

#球門的起始位置
goalX = windowSize[0] // 2 - 10
goalY = windowSize[1] // 2 - 10
goalW = 50
goalH = 50
#分數
points = 0

#顏色
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')



#判斷邊界X
def checkoffscreenX(x):
    if x > windowSize[0]:
        x = 0
    elif x < 0:
        x = windowSize[0]
    return x

#判斷邊界X
def checkoffscreenY(y):
    if y > windowSize[1]:
        y = 0
    elif y < 0:
        y = windowSize[1]
    return y

#判別碰撞
def checkTouching():
    global x,y,ballX,ballY
    if -10 < y-ballY < 10 and -10 < x-ballX < 10:
        pygame.draw.circle(screen,white,[x,y],15)
        xdiff = x - ballX
        ydiff = y - ballY
        
        #如果球在邊界
        if ballX == 0:
            xdiff -= 5
        elif ballX == windowSize[0]:
            xdiff += 5
        if ballY == 0:
            ydiff -= 5
        elif ballY == windowSize[1]:
            ydiff += 5
            
        #移動球和角色
        '''x += xdiff * 3'''
        ballX -= xdiff * 3
        '''y += ydiff * 3'''
        ballY -= ydiff * 3
        
#取的程式啟動時間
timeStart= pygame.time.get_ticks()

done = False
#game loop
while not done:
    screen.fill(black)
    pygame.draw.rect(screen,white,(goalX,goalY,goalW,goalH))
    keys = pygame.key.get_pressed()

    #判斷是否進球門
    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY + goalH:
        points += 1
        ballX = random.randrange(0,windowSize[0])
        ballY = random.randrange(0,windowSize[1])

    #移動
    if keys[pygame.K_w]:
        y -= 1
    elif keys[pygame.K_s]:
        y += 1
    elif keys[pygame.K_d]:
        x += 1
    elif keys[pygame.K_a]:
        x -= 1

    x = checkoffscreenX(x)
    y = checkoffscreenY(y)
    ballX = checkoffscreenX(ballX)
    ballY = checkoffscreenY(ballY)

    checkTouching()

    #計分
    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen,white,(pointX,3,4,10))
    #角色的初始位置
    pygame.draw.circle(screen,red,(x,y),6)

    #球的初始位置
    pygame.draw.circle(screen,blue,(ballX,ballY),6)
    pygame.display.flip()    

    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = True
    #clock.tick():控制程式畫面更新頻率
    clock.tick(72)

    #檢查遊戲是否超過60秒
    timeNow = pygame.time.get_ticks()
    if timeNow - timeStart >= 60000:
        done = True

pygame.quit()
print("total points:" + str(points))
    
