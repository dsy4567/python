from turtle import *
import easygui,random,time
speed(100000000000)
screensize(10000,10000)
colormode(255)
pensize(10)
def a(b=None,c=None,d=(None,None,None),e="fastest",f=255):
	colormode(f)
	speed(e)
	pencolor(d)
	circle(b)
	penup()
	left(90)
	forward(c)
	right(90)
	pendown()
def b(gt=None,co=None):
	goto(gt)
	pencolor(co)
def aaa():
	i=0
	while 1:
		aa=random.randint(0,255);ab=random.randint(0,255);ac=random.randint(0,255)
		a(i,0.1,(aa,ab,ac))
		i=i-0.1
	mainloop()
def bbb():
	colormode(255)
	aa=random.randint(0,255);ab=random.randint(0,255);ac=random.randint(0,255)
	b(gt=(100,0),co=(aa,ab,ac))
	b(gt=(0,100),co=(aa,ab,ac))
	home()
	time.sleep(3)
	clear()

	aa=random.randint(0,255);ab=random.randint(0,255);ac=random.randint(0,255)
	b(gt=(50,20),co=(aa,ab,ac))
	b(gt=(30,150),co=(aa,ab,ac))
	home()
	time.sleep(3)

	clear()
	aa=random.randint(0,255);ab=random.randint(0,255);ac=random.randint(0,255)
	b(gt=(10,100),co=(aa,ab,ac))
	b(gt=(100,50),co=(aa,ab,ac))
	home()
	time.sleep(3)
	mainloop()
def ccc():
	a=["red","yellow","blue","black","green"]
	i=0
	while 1:
		i=i+1
		#pencolor(a[i%5])
		#forward(i*5)
		pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		forward(random.randint(1,50))
		left(90)
	done()

ccc()