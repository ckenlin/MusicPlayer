import pygame as pg#import pygame module
from pygame.locals import QUIT,MOUSEBUTTONUP
pg.init()#初始化
pg.display.set_caption("ooxx")#視窗左上角名稱
screen = pg.display.set_mode((200,200))#視窗大小
screen.fill((0,0,0))#視窗顏色
clock = pg.time.Clock()
font = pg.font.SysFont("arial",20)#字體大小

left = False
win = 0
player = 1#預設為1P
data = [[0,0,0],[0,0,0],[0,0,0]]#建立一個3x3陣列

main_surface = pg.Surface((200,200))#建立主要圖層
pg.draw.rect(main_surface,(150,150,150),[25,25,150,150],3)#畫出格線
pg.draw.line(main_surface,(150,150,150),(25,75),(175,75),3)
pg.draw.line(main_surface,(150,150,150),(25,125),(175,125),3)
pg.draw.line(main_surface,(150,150,150),(75,25),(75,175),3)
pg.draw.line(main_surface,(150,150,150),(125,25),(125,175),3)

while 1:
    x,y = pg.mouse.get_pos()#滑鼠游標的座標
    left = pg.mouse.get_pressed()[0]#滑鼠左鍵是否被按下
    for event in pg.event.get():#退出遊戲判定
        if event.type == QUIT:
            pg.quit()
            break
        if event.type == MOUSEBUTTONUP:#滑鼠鍵放開判定
            if left:
                left = "depress"#如果滑鼠左鍵放開,則把left設為depress
    
    prompt_surface = pg.Surface((200,25))#建立空的提示圖層
    if win == -1:#平手
        prompt_surface.blit(font.render("No one won...",True,(255,255,255)),(50,0))#印出沒人贏
    elif win == 1 or win == 2:#某人贏了
        prompt_surface.blit(font.render("P%d win!"%win,True,(255,255,255)),(75,0))#印出誰贏
    elif left == "depress" and abs(x-100) < 75 and abs(y-100) < 75:#滑鼠按下判定區
        i,j = int((x-25)//50),int((y-25)//50)#計算行列
        if data[i][j] == 0:#空格子才能選
            if player == 1:
                data[i][j] = 1
                pg.draw.circle(main_surface,(50,255,50),(50+50*i,50+50*j),15,3)#P1畫圈
                player = 2#換人
            elif player == 2:
                data[i][j] = 2
                pg.draw.line(main_surface,(255,50,50),(40+50*i,40+50*j),(60+50*i,60+50*j),5)#P1畫叉
                pg.draw.line(main_surface,(255,50,50),(40+50*i,60+50*j),(60+50*i,40+50*j),5)
                player = 1#換人
    else:
        prompt_surface.blit(font.render("It's P%d turn"%player,True,(255,255,255)),(60,0))#印出輪到誰
    
    if [i.count(1) == 3 for i in data].count(True) > 0 or\
       [i.count(1) == 3 for i in zip(data[0],data[1],data[2])].count(True) > 0 or\
       [data[i][i] for i in range(3)].count(1) == 3 or\
       [data[i][2-i] for i in range(3)].count(1) == 3:#判定是誰連成線
        win = 1
    elif [i.count(2) == 3 for i in data].count(True) > 0 or\
         [i.count(2) == 3 for i in zip(data[0],data[1],data[2])].count(True) > 0 or\
         [data[i][i] for i in range(3)].count(2) == 3 or\
         [data[i][2-i] for i in range(3)].count(2) == 3:
        win = 2
    elif sum(i.count(0) for i in data) == 0:#如果框全被占滿但沒人連成線
        win = -1
    
    screen.blit(main_surface,(0,0))#把圖層貼在視窗上
    screen.blit(prompt_surface,(0,175))#印出提示圖層
    pg.display.update()#更新視窗頁面(很重要)
    clock.tick(30)
