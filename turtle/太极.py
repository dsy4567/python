from turtle import *
import random,time,easygui
#colormode(255)
#screensize(2000,2000,"white")
#hideturtle()
#speed(100000000000000000000000000000000000000)
def a():
    pensize(1)
    forward(50)
    for i in range(3):
        right(90)
        forward(50)
    penup()
    goto(25,-25)
    pendown()
    for i in range(3):
        forward(10)
        penup()
        forward(10)
        pendown()
    left(135)
    penup()
    goto(25,-25)
    pendown()
    for i in range(2):
        forward(10)
        penup()
        forward(10)
        pendown()

    penup()
    home()
    goto(25,-25)
    pendown()
    for i in range(2):
        forward(10)
        penup()
        forward(10)
        pendown()
    forward(10)
    left(90)
    forward(50)
    left(90)
    forward(50)
    home()
    penup()
    goto(75,-25)
    pendown()
    goto(50,-50)
    
def b():

    a=0
    pencolor("red")
    while not a==360:
        forward(90)
        right(a)
        a=a+1
        left(a)
        goto(0,0)
    b=0
    while not b==360:
        forward(180)
        right(b)
        b=b+1
        left(b)
        goto(0,0)
    c=0
    while not c==360:
        forward(270)
        right(c)
        c=c+1
        left(c)
        goto(0,0)
    
def c():
    for i in range(3):
        forward(90)
        right(120)
    time.sleep(3)
    clear()
    penup()
    home()
    pendown()
    forward(90)
    right(random.randint(120,179))
    forward(90)
    home()
    time.sleep(3)
    clear()
    penup()
    home()
    pendown()
    forward(90)
    left(random.randint(30,80))
    forward(90)
    home()
    time.sleep(3)
    clear()
    penup()
    home()
    pendown()
    forward(90)
    right(90)
    forward(90)
    home()
    
def d():
    while 1:
        a=random.randint(1,4)
        if a==1:
            goto((random.randint(1,9999)),(random.randint(1,9999)))
            if random.randint(0,1)==1:
                right(random.randint(1,179))
            else:
                left(random.randint(1,179))
            home()
        if a==2:
            goto(0-(random.randint(1,9999)),(0-(random.randint(1,9999))))
            if random.randint(0,1)==1:
                right(random.randint(1,179))
            else:
                left(random.randint(1,179))
            home()
        if a==3:
            goto((0-(random.randint(1,9999))),(random.randint(1,9999)))
            if random.randint(0,1)==1:
                right(random.randint(1,179))
            else:
                left(random.randint(1,179))
            home()
        if a==4:
            goto((random.randint(1,9999)),(0-(random.randint(1,9999))))
            if random.randint(0,1)==1:
                right(random.randint(1,179))
            else:
                left(random.randint(1,179))
            home()
def e():
    begin_fill()
    fillcolor("red")
    pencolor("red")
    circle(200)
    end_fill()
    penup()
    home()
    left(90)
    forward(50)
    right(90)
    pendown()
    

    begin_fill()
    fillcolor("white")
    pencolor("white")
    circle(150)
    end_fill()
    penup()
    home()
    left(90)
    forward(100)
    right(90)
    pendown()
    

    begin_fill()
    fillcolor("red")
    pencolor("red")
    circle(100)
    end_fill()
    penup()
    home()
    left(90)
    forward(150)
    right(90)
    pendown()
    

    begin_fill()
    fillcolor(2,69,140)
    pencolor(2,69,140)
    circle(50)
    end_fill()
    penup()
    home()
    left(90)
    forward(200)
    right(90)
    forward(-48)
    left(90)
    forward(15)
    right(90)
    pendown()

    begin_fill()
    fillcolor("white")
    pencolor("white")
    for i in range(10):
        forward(95)
        right(180-36)
    end_fill()

    
def f():
    B="blue"
    R="red"
    Y="yellow"
    BL="black"
    G="green"
    PU=penup
    PD=pendown
    H=home
    RI=right
    LE=left
    pensize(10)

    def aaa(Color=None,B=None,Goto=None):
        pencolor(Color)
        circle(B)
        PU()
        goto(Goto)
        PD()

    aaa(B,100,(220,0))
    aaa(BL,100,(440,0))
    aaa(R,100,(100,-100))
    aaa(Y,100,(350,-100))
    aaa(G,100,(0,0))

    
def g():
    while 1:
        while 1:
            try:
                a=int(easygui.enterbox("画几边形？"))
            except:
                easygui.msgbox("不是数字，请重新输入")
                continue
            break
        b=360/a
        for i in range(a):
            forward(50)
            left(b)
        if easygui.boolbox("还画吗")==True:
            continue
        else:
            break
def h():
    for i in range(3,100):
        forward(10)
        left(360/i)
def i():
    def p(pp=None):
        penup()
        goto(pp)
        pendown()
    def bf(bb,aa,co):
        begin_fill()
        color(co)
        circle(bb,aa)
        end_fill()
    
    bf(200,180,"black")
    circle(200,180)

    bf(100,180,co="white")
    p((0,400))

    bf(100,180,co="black")
    p((0,250))

    bf(50,360,co="white")
    p((0,50))
    
    bf(50,360,co="black")
def j():
    pass
i()

mainloop()