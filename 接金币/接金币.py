import pgzrun,random,easygui,os,time
start=time.time()
WIDTH=600
HEIGHT=600
bg=Actor("bg")
jb=Actor("jb")
box=Actor("box")
zda=Actor("zd")
zdb=Actor("zd")
jb.x=random.randint(50,550)
box.x=300
zda.x=random.randint(50,550)
zda.y=-50
zdb.x=random.randint(50,550)
zdb.y=-50
jb.y=50
box.y=500
a=0
b=5
c=0
e=0
co="green"
def draw():
    bg.draw()
    jb.draw()
    box.draw()
    zda.draw()
    zdb.draw()
    screen.draw.text(str(a),(40,40),fontsize=100,color="blue")
    screen.draw.text(str(b),(40,100),fontsize=100,color=co)
def update():
    global a,b,co,c,e
    if box.colliderect(jb):
        jb.x=random.randint(50,550)
        jb.y=50
        a+=1
        if b<=15:
            b+=0.5
        os.system("cls")
        print("当前分数："+str(a))
        print("当前速度："+str(b))

    if jb.y>600:
        a-=1
        jb.y=50
        jb.x=random.randint(50,550)
    if box.colliderect(zda) or box.colliderect(zdb) or a<0:
        end=time.time()-start
        easygui.msgbox("游戏失败,持续时间："+str(end)+"\n得分:"+str(a))
        quit()
    jb.y+=b
    if a>=15:
        c=1
    if a>=50:
        e=1
    if c==1:
        if e==1:
            zdb.y+=2
        zda.y+=1
        if e==1:
            co="black"
        elif c==1:
            co="red"
    if zda.y>600:
        zda.y=50
        zda.x=random.randint(50,550)
    if zdb.y>600:
        zdb.y=50
        zdb.x=random.randint(50,550)
def on_mouse_move(pos,rel,buttons):
    if mouse.LEFT in buttons:
        box.x=pos[0]
pgzrun.go()