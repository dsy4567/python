import pgzrun
import random
WIDTH=600;HEIGHT=800;真=True;假=False
死了 = 假
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
背景2.x=600/2
背景2.y=-800/2
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
窗户2.x = 窗户.x
窗户3.x = 窗户.x
窗户2.y = 窗户.y
窗户3.y = 窗户.y
分数 = 0
a=1
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
    screen.draw.text(str(分数), (WIDTH/2, 50), fontsize=50, color='green')
    if 死了: 
        screen.draw.text("GAME OVER!", (50, HEIGHT/2), fontsize=90, color='red')
def update():
    global 分数,死了,a
    if 死了:
        return 
    背景2.y+=1
    背景1.y+=1
    if 背景2.y>=800/2+800:
        背景2.y=-800/2
    if 背景1.y>=800/2+800:
        背景1.y=-800/2
    窗户.y = 窗户.y + 3
    if 窗户.y > HEIGHT:
        窗户.x = random.randint(5,595)
        窗户.y = -50
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
        窗户.x = random.randint(5, 600)
        窗户.y = -50
        锤子1.x = WIDTH/2
        锤子1.y = -HEIGHT
        锤子2.x = WIDTH/2
        锤子2.y = -HEIGHT
        锤子3.x = WIDTH/2
        锤子3.y = -HEIGHT
        分数 = 分数 + 1
        a=1
    if 窗户.y >= 0:
        窗户.image = 'ch'
        
    if 飞机.colliderect(窗户):
        # sounds.explode.play()
        死了 = 真
        飞机.image = 'bz'
def on_mouse_move(pos, rel, buttons):
    if 死了:
        return
    飞机.x = pos[0]
    飞机.y = pos[1]
def on_mouse_down():
    if 死了:
        return
    if a:
        锤子1.x = 飞机.x
        锤子1.y = 飞机.y - 70
        锤子2.x = 飞机.x + 50
        锤子2.y = 飞机.y - 70
        锤子3.x = 飞机.x - 50
        锤子3.y = 飞机.y - 70
    # sounds.gun.play()
pgzrun.go()
