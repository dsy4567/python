import pgzrun,random,time
WIDTH = 500 ; HEIGHT = 500 ; TITLE = '贪吃蛇'
蛇头 = Actor('蛇') ; 食物 = Actor('食物')
食物.pos = random.randint(10,490),random.randint(10,490) ; 蛇头.pos = WIDTH/2,HEIGHT/2
方向 = '左'
很多蛇 = [] ; 很多蛇.append(蛇头)
a = 0.2 ; 死了 = 0
copyright = 'DSY'
for i in range(5):
    蛇身 = Actor('蛇')
    蛇身.x = 很多蛇[i].x + 15
    蛇身.y = 很多蛇[i].y
    很多蛇.append(蛇身)
分数 = 0
def draw():
    # screen.fill('white')
    screen.clear()
    for 蛇身 in 很多蛇:
        蛇身.draw()
    食物.draw()
    screen.draw.text(str(分数),(WIDTH/2,HEIGHT-50),color='green')
    if 死了:
        screen.draw.text("GAME OVER!",(WIDTH/2,HEIGHT/2),color='red')
def update():
    global 方向
    if keyboard.right and 方向 != '左':
        方向 = '右'
    if keyboard.left and 方向 != '右':
        方向 = '左'
    if keyboard.up and 方向 != '下':
        方向 = '上'
    if keyboard.down and 方向 != '上':
        方向 = '下'
def 蛇蛇蛇():
    global 分数,死了
    新蛇 = Actor('蛇')
    if 方向 == '右':
        新蛇.x = 很多蛇[0].x + 15
        新蛇.y = 很多蛇[0].y
    if 方向 == '左':
        新蛇.x = 很多蛇[0].x - 15
        新蛇.y = 很多蛇[0].y
    if 方向 == '上':
        新蛇.x = 很多蛇[0].x
        新蛇.y = 很多蛇[0].y - 15
    if 方向 == '下':
        新蛇.x = 很多蛇[0].x 
        新蛇.y = 很多蛇[0].y + 15
    for 蛇 in 蛇身:
        if 新蛇.x > WIDTH or 新蛇.x < 0 or 新蛇.y > HEIGHT or 新蛇.y < -15 :
            死了=1
            return
        if float(新蛇.y)==float(蛇) and float(新蛇.y)==float(蛇):
            死了=1
            return
    if 新蛇.colliderect(食物):
        分数 += 1
        食物.pos = random.randint(10,490),random.randint(10,490)
    else:
        del 很多蛇[len(很多蛇)-1]
    很多蛇.insert(0,新蛇)
    clock.schedule_unique(蛇蛇蛇, 0.1)
蛇蛇蛇()
pgzrun.go()
# colliderect clock.schedule_unique(moveSnake, 0.2)