import pgzrun
import random
WIDTH = 480
HEIGHT = 852
isLoose = False
background1 = Actor('background')
background2 = Actor('background') 
fj = Actor('hero')
dj = Actor('enemy')
bz = Actor('hero_blowup')
zd = Actor('bullet')
background2.x = 480/2 
background2.y = -852/2  
background1.x = 480/2  
background1.y = 852/2
zd.x = WIDTH/2 
zd.y = -HEIGHT
fj.x = 240
fj.y = 852
dj.x = 240
dj.y = -50
dj_speed = 3
score = 0
# sounds. game_music.play(-1)
def draw():
    background1.draw()
    background2.draw()
    fj.draw()
    dj.draw()
    zd.draw()
    screen.draw.text("得分: "+str(score), (200, HEIGHT-50), fontsize=30, color='black')
    if isLoose: 
        screen.draw.text("游戏失败！", (50, HEIGHT/2), fontsize=90, color='red')
def update():
    global dj_speed,score,isLoose
    if isLoose:
        return 
    if background1.y > 852/2 + 852:
        background1.y = -852/2 
    if background2.y > 852/2 + 852:
        background2.y = -852/2 
    background1.y += 1  
    background2.y += 1
    dj.y = dj.y + dj_speed
    if dj.y > HEIGHT:
        dj.x = random.randint(5,475)
        dj.y = -50
    if zd.y > -HEIGHT:
        zd.y = zd.y - 10
    if zd.colliderect(dj):
        # sounds.got_enemy.play()
        dj.x = random.randint(5, 475)
        dj.y = -50
        zd.x = WIDTH/2
        zd.y = -HEIGHT
        score = score + 1
        if score %5 == 0:
            dj_speed = dj_speed + 1
    if fj.colliderect(dj):
        # sounds.explode.play()
        isLoose = True
        fj.image = 'hero_blowup'
def on_mouse_move(pos, rel, buttons):
    if isLoose:
        return
    fj.x = pos[0]
    fj.y = pos[1]
def on_mouse_down():
    if isLoose:
        return
    zd.x = fj.x
    zd.y = fj.y - 70
    # sounds.gun.play()
pgzrun.go()
