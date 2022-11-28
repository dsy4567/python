import pgzrun,random
WIDTH = 600;HEIGHT = 800
角色 = [Actor('角色1'),Actor('角色2'),Actor('角色3'),Actor('角色4'),Actor('角色5'),Actor('角色6')]
角色数 = len(角色)
角色样式 = 0
角色变化速度 =0
砖 = Actor('砖')
砖.pos=300,456
_砖 = []
s了=False
赢了=False
a=0
b=0
c=0
d=0
得分=0
sounds.boom.play(-1)
for i in range(100):
    if i==0:
        砖.pos=WIDTH/2,150*(i+1)
    砖 = Actor('砖')
    砖.pos = random.randint(100,500),250*(i+1)
    _砖.append(砖)
for b in range(0,角色数):
    角色[b].x = WIDTH/2
    角色[b].y = HEIGHT/2
def draw():
    screen.fill('black')
    for 砖 in _砖:
        砖.draw()
    角色[角色样式-1].draw()
    screen.draw.text(str(d), (50, HEIGHT/2), fontsize=90, color='red')
def update():
    global 角色样式,角色变化速度,a,b,c,得分,d,赢了,s了
    d=_砖[99].y-角色[角色样式].y
    # print(str(角色[角色样式].x)+' '+str(得分)+' ',角色[角色样式].y)
    角色在砖块上 = False
    角色变化速度 += 1
    if 角色变化速度 %50 == 0:
        角色样式 += 1
        if 角色样式 == 角色数-1:
            角色样式=0
    # if 角色[角色样式].x >= WIDTH:
    #     for b in range(0,角色数):
    #         角色[b].x = 0
    if not s了:
        if keyboard.right:
            for b in range(0,角色数):
                角色[b].x += 5
                if 角色[b].x >= WIDTH:
                    角色[b].x = WIDTH
        if keyboard.left:
            for b in range(0,角色数):
                角色[b].x -= 5
                if 角色[b].x <= 0:
                    角色[b].x = 0
        for b in range(0,角色数):
            角色[b].y += 2
        for 砖 in _砖:
            砖.y -= 2
            if abs(角色[b].bottom - 砖.top )< 5 and 砖.left - 角色[b].left < 角色[b].width*2/3 and 角色[b].right - 砖.right < 角色[b].width*2/3 :
                角色在砖块上 = True
                for b in range(0,角色数):
                    角色[b].bottom = 砖.top
                if keyboard.right:
                    for b in range(0,角色数):
                        角色[b].x += 5
                if keyboard.left:
                    for b in range(0,角色数):
                            角色[b].x -= 5
            if 角色[角色样式].y>HEIGHT or 角色[角色样式].y<0:
                s了=True
            if 角色[角色样式].colliderect(_砖[99]):
                赢了=True
    if s了:
        d='GAME OVER'
    if 赢了:
        d='YOU WIN'


pgzrun.go()