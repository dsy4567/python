import pgzrun,random
WIDTH = 1000;HEIGHT = 1000
蛇 = Actor('蛇')
食物 = Actor('食物')
食物.pos = random.randint(10,900),random.randint(10,900)
蛇.pos = WIDTH/2,HEIGHT/2
方向 = '右'
很多蛇 = []
很多蛇.append(蛇)
for i in range(0,99):
    _蛇 = Actor('蛇')
    _蛇.x = 很多蛇[i].x 
    _蛇.y = 很多蛇[i].y
    很多蛇.append(_蛇)
分数 = 0
def draw():
    screen.fill('black')
    screen.clear()
    
    食物.draw()
    for _蛇 in 很多蛇:
        _蛇.draw()
def update():
    global 分数
    if 方向 == '右':
        很多蛇[分数].x +=  10
    if 方向 == '左':
        很多蛇[分数].x -=  10
    if 方向 == '上':
        很多蛇[分数].y -= 10
    if 方向 == '下':
        很多蛇[分数].y += 10
    if 很多蛇[分数].colliderect(食物):
        食物.pos = random.randint(10,900),random.randint(10,900)
        分数 += 1
        很多蛇[分数].x += 15*分数
def on_key_down():
    global 方向
    if keyboard.right:
        方向 = '右'
    if keyboard.left:
        方向 = '左'
    if keyboard.up:
        方向 = '上'
    if keyboard.down:
        方向 = '下'
pgzrun.go()