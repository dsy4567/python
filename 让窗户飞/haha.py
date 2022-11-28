import pgzrun,random,time,easygui
WIDTH=600
HEIGHT=600
background1=Actor('background1')
background2=Actor('background2')
background=background2
bird=Actor('window')
bar_u=Actor('hammers')
bar_d=Actor('hammers')
bbird=Actor('damaged_window')
bird.y=300
bar_u.x=600
bar_d.x=600
score=0
yy=random.randint(-300,100)
bar_u.y=yy
bar_d.y=yy+800
a=0
def draw():
    background1.draw()
    bird.draw()
    bar_u.draw()
    bar_d.draw()
    screen.draw.text(str(score),(40,40),fontsize=100,color="red")
def update():
    global score,a,bird,background
    # print(bird.y)
    if a==1:
        easygui.msgbox("游戏失败，你的得分是"+str(score))
        quit()
    if bird.y<=600.0:
        bird.y+=5
    if bird.y<=10.0:
        bird.y=10
    if bar_u.x<=0:
        bar_u.x=600
        bar_d.x=600
        yyy=random.randint(-300,100)
        bar_u.y=yyy
        bar_d.y=yyy+800
        score+=1
    bar_u.x-=2
    bar_d.x-=2
    if bird.colliderect(bar_d) or bird.colliderect(bar_u):
        # easygui.msgbox("游戏失败，你的得分是"+str(score))
        bbird.x=bird.x
        bbird.y=bird.y
        bird=bbird
        a=1
        return 0
        #🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮
        # for i in range(50):
        #     os.system("start")
        # quit()
def on_mouse_down():
    bird.y-=100
# def on_mouse_move(pos,rel,buttons):
#     if mouse.LEFT in buttons:
#         yy=pos[1]
#         bird.y=yy
pgzrun.go()