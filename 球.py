import pgzrun,random
# coding=utf-8
co=["red","orange","yellow","green","blue","cyan","purple","white"]
r=[350,325,300,275,250,225,200,175]
def a():
    ##os.system("E:\\hehe\\haha.mp3")
    #
    ##while 1:
    ##try:

    #b=(co[random.randint(0,7)])
    #c=(co[random.randint(0,7)])
    ##800x600
    ##400,300
    #x=0
    #y=0
    #a=50
    #yy=50
    #xx=50
    #def draw():
    #    screen.fill(c)
    #    screen.draw.filled_circle((x,y),a,b)
    #    #screen.draw.filled_circle((x-10,y-10),a,b)
    #    #screen.draw.filled_circle((x-20,y-20),a,b)
    #
    #def update():
    #    global y,x,a,xx,yy,b,c
    #    #x=x+xx
    #    y=y+yy
    #    if x==800:
    #        xx=-50
    #    if x==0:
    #        xx=50
    #    if y>600:
    #        y=y-600
    #        x=x+xx
    #        
    #    c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #    b=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #pgzrun.go()

    #except:
    #    continue

    # a=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # b=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    # def draw():
    #     screen.fill(a)
    #     for i in range(255,0,-1):
    #         screen.draw.filled_circle((400,300),i,(i,i,i))
    print()
WIDTH=1920
HEIGHT=1048
balls=[]
for i in range(100):
    x = random.randint(100,WIDTH - 100)#小球的X坐标
    y = random.randint(100,HEIGHT - 100)#小球的Y坐标
    speed_x = random.randint(1,5)#小球X方向的速度
    speed_y = random.randint(1,5)#小球y方向的速度
    r = random.randint(5,50)#小球半径
    colorR = random.randint(10,255)
    colorG = random.randint(10,255)
    colorB = random.randint(10,255)
    #存储小球所有信息的列表
    ball = [x,y,speed_x,speed_y,r,colorR,colorG,colorB]
    balls.append(ball)#把第i个小球的信息添加到balls中
def update():
    for ball in balls:
        ball[0]=ball[0]+ball[2]
        ball[1]=ball[1]+ball[3]
        if ball[0]>WIDTH-ball[4] or ball[0]<ball[4]:
            ball[2]=-ball[2]
        if ball[1]>HEIGHT-ball[4] or ball[1]<ball[4]:
            ball[3]=-ball[3]
# haha=[]
# for i in range(100):
#     haha.append(i)
# screen.draw.filled_circle((x-20,y-20),a,b)
def on_mouse_down():
    draw()

def draw():
    screen.fill('white')
    for ball  in balls:
        screen.draw.filled_circle((ball[0],ball[1]),ball[4],(ball[5],ball[6],ball[7]))

# a=[1,9]
# b=[2,8]
# c=[3,9]
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)

# for ball in d:
#     print(ball[0],ball[1])



pgzrun.go()

