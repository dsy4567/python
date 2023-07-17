import pgzrun,random,easygui
WIDTH=800
HEIGHT=800
_zhen=[]
qiu=Actor('qiu')
qiu.x=530
qiu.y=280
xinzhen=Actor("zhen",anchor = (170+50,1.5))
xinzhen.x=300
xinzhen.y=300
_zhen.append(xinzhen)
fenshu=0
def draw():
    screen.fill('white')
    screen.draw.filled_circle((550,300),180,"yellow")
    screen.draw.text(str(fenshu),(40,100),fontsize=100,color="black")
    for zhen in _zhen:
        zhen.draw()
def update():
    for zhen in _zhen:
        if zhen.x==550:
            zhen.angle+=1
    
    # _zhen.append(xinzhen)
def on_mouse_down():
    global fenshu
    xinzhen=Actor("zhen",anchor = (170+50,1.5))
    xinzhen.x=550
    xinzhen.y=300
    for zhen in _zhen:
        if xinzhen.colliderect(zhen):
            easygui.msgbox("游戏失败")
            quit()
    _zhen.append(xinzhen)
    fenshu+=1
pgzrun.go()