import easygui,random,os,datetime,webbrowser,time,tkinter,sys
try:
    qs=0
    cw=0
    if sys.platform != 'win32':
        if easygui.boolbox("您使用的不是windows系统，不建议继续运行","啊哦",("继续","退出"))==False:
            quit()
    os.system("title 小游戏控制台，请勿关闭此窗口")
    os.system("echo.")
    os.system("echo.----------这是小游戏控制台，用于输出运行信息，不想看到请最小化----------")
    os.system("echo.")
    os.system("md C:\yx3.0\sj")
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def hehe():
        ha=easygui.buttonbox("要退出吗",ti,("是","否","使用高级功能"))
        if ha=="是":
            if jhzt=="-软件未激活":
                s=random.randint(1,3)
                if s==1:
                    easygui.msgbox("拜拜！",ti)
                    import time
                    time.sleep(60)
                    def aaa():
                        nnnn=random.randint(1,500)
                        mnmn=random.randint(1,500)
                        root.geometry(str(nnnn)+"x"+str(mnmn))
                        root.after(100,aaa)
                    root = tkinter.Tk()
                    root.title('你关不掉我')
                    root.resizable(0,0)
                    lb = tkinter.Label(root,text="你关不掉我",fg='blue',font=("黑体",50))
                    lb.pack()
                    aaa()
                    root.mainloop()
                else:
                    easygui.msgbox("嗨起来",ti)
                    os.system("C:\yx3.0\sj\cc.bat")
                    quit()
            else:
                easygui.msgbox("拜拜！",ti)
                quit()
        if ha=="否":
            pass
        while ha=="使用高级功能":
            ts=input("请输入指令 q：退出 c：输入cmd指令 p：输入python指令\n-->")
            if ts=="q":
                break
            while ts=="c":
                cts=input("请输入cmd指令 q：退出\n-->")
                if cts=="q":
                    break
                tb=os.system(cts)
                print("返回值为：",tb)
            while ts=="p":
                pts=input("请输入python指令 q：退出\n-->")
                if pts=="q":
                    break
                try:
                    tb=eval(pts)
                    print("返回值为：",tb)
                except:
                    pass
    jhbm=random.randint(10000000000000000,99999999999999999)
    jhm=format(jhbm,"x")
    if os.path.exists("C:\yx3.0\sj\yxjh.txt")==True:
        jhjh=open("C:\yx3.0\sj\yxjh.txt","r")
        jjhh=jhjh.read()
        jhjh.close()
        if jjhh=="1":
            jjh=1
            jhzt="-软件已激活"
        else:
            jjh=0
            jjhh="0"
            jhzt="-软件未激活"
    else:
        jjhh="0"
    while jjhh=="0":
        jh=easygui.enterbox("请输入激活码，以跳过广告并使用更多功能\n软件编码："+str(jhbm)+"。","激活")
        if jh==jhm:
            jhjh=open("C:\yx3.0\sj\yxjh.txt","w")
            jhjh.write("1")
            jhjh.close()
            jhdsj=datetime.datetime.now()
            jhsj=open("C:\yx3.0\sj\yxjhsj.txt","w")
            jhsj.write(str(jhdsj))
            jhsj.close()
            jjh=1
            jhzt="-软件已激活"
            easygui.msgbox("激活成功","激活")
            break
        if jh=="" or jh==None:
            easygui.msgbox("已放弃激活","激活")
            jjh=0
            jhzt="-软件未激活"
            break
        else:
            easygui.msgbox("激活失败","激活")
    while True:
        ti="小游戏"+str(jhzt)
        ww=easygui.choicebox("您希望做什么",ti,["注册账号","退出","删除账号","查询账号","开始游戏","卸载游戏并删除游戏数据","查看战绩","关于","查询激活状态","设置（仅本次有效）"])
        if ww==None:
            quit()
        while ww=="设置（仅本次有效）":
            a=easygui.choicebox("选择一个设置项（关闭窗口则开始游戏）","设置",["退出时要求按回车键-开","退出时要求按回车键-关","出现错误时显示信息-开","出现错误时显示信息-关","退出"])
            if a=="退出时要求按回车键-开":
                qs=1
            if a=="退出时要求按回车键-关":
                qs=0
            if a=="出现错误时显示信息-开":
                cw=1
            if a=="出现错误时显示信息-关":
                cw=0
            if a=="退出" or a==None:
                break
        if ww=="查询激活状态":
           if jjh==1 :
                jhdrq=open("C:\yx3.0\sj\yxjhsj.txt","r")
                jhddsj=jhdrq.read()
                jhdrq.close()
                qxjh=easygui.boolbox("已激活，激活时间："+jhddsj,"查询激活状态",["知道了","取消激活"])
                if qxjh==False:
                    os.system("del /q C:\yx3.0\sj\yxjhsj.txt")
                    os.system("del /q C:\yx3.0\sj\yxjh.txt")
                    easygui.msgbox("完成","取消激活")
                    quit()
            else:
                easygui.msgbox("还没有激活","查询激活状态")
            
        if ww=="关于":
            os.system("start C:\yx3.0\sj\c.txt")
            
        if ww=="查看战绩":
            os.system("start C:\yx3.0\sj\zj.txt")
            
        if ww=="注册账号":

            while True:
                aa=easygui.enterbox("请输入名字","账号注册")
                if aa==None or aa=="":
                    hehe()
                    continue
                break
            while True:
                bb=easygui.passwordbox("请输入密码","账号注册")
                if bb==None or bb=="":
                    hehe()
                    continue
                break
            while True:
                dd=easygui.enterbox("请输入年龄(请输入数字)","账号注册")
                if dd==None or dd=="":
                    hehe()
                    continue
                try:
                    dd=int(dd)
                except:
                    continue
                break
            wwcn=0
            if dd<3:
                easygui.msgbox("您未满3岁，无法注册账号","账号注册")
                
            elif dd<18:
                easygui.msgbox("您未成年，将受到防沉迷限制","账号注册")
                wwcn=1
                
            
            bbb=os.path.exists("C:\yx3.0\sj\cxxmz1.txt")
            if bbb==True:
                bbb=os.path.exists("C:\yx3.0\sj\cxxmz2.txt")
                if bbb==True:
                    bbb=os.path.exists("C:\yx3.0\sj\cxxmz3.txt")
                    if bbb==True:
                        easygui.msgbox("账号数已达上限，无法注册账号","啊哦")
                        quit()
                    else:
                        xxx=open("C:\yx3.0\sj\cs3.txt","x")
                        xxa=open("C:\yx3.0\sj\cxxmz3.txt","w")
                        xxb=open("C:\yx3.0\sj\cxxmm3.txt","w")
                        xxc=open("C:\yx3.0\sj\cxxcn3.txt","w")
                        ddmmd=3
                else:
                    xxx=open("C:\yx3.0\sj\cs2.txt","x")
                    xxa=open("C:\yx3.0\sj\cxxmz2.txt","w")
                    xxb=open("C:\yx3.0\sj\cxxmm2.txt","w")
                    xxc=open("C:\yx3.0\sj\cxxcn2.txt","w")
                    ddmmd=2
            else:
                xxx=open("C:\yx3.0\sj\cs1.txt","x")
                xxa=open("C:\yx3.0\sj\cxxmz1.txt","w")
                xxb=open("C:\yx3.0\sj\cxxmm1.txt","w")
                xxc=open("C:\yx3.0\sj\cxxcn1.txt","w")
                ddmmd=1
            xxa.write(str(aa))
            xxa.close()
            xxb.write(str(bb))
            xxb.close()
            xxc.write(str(wwcn))
            xxc.close()
            easygui.msgbox("完成","账号注册")
            easygui.msgbox("您的用户代码是"+str(ddmmd)+"，请不要忘记哦","账号注册")
            
        if ww=="退出":
            quit()
        if ww=="删除账号":
            wwww=easygui.boolbox("确定要继续吗","删除账号")
            if wwww==True:
                wwww=easygui.enterbox("请输入用户代码","删除账号")
                os.system("del C:\yx3.0\sj\cxxmz"+str(wwww)+".txt")
                os.system("del C:\yx3.0\sj\cxxmm"+str(wwww)+".txt")
                os.system("del C:\yx3.0\sj\cs"+str(wwww)+".txt")
                easygui.msgbox("完成","删除账号")
            
            
        if ww=="查询账号":
            while True:
                dm=easygui.integerbox("请输入用户代码","查询账号",None,1,4)
                if dm==None or dm=="":
                    hehe()
                    continue
                break
            bb=os.path.exists("C:\yx3.0\sj\cxxmz"+str(dm)+".txt")
            if bb==False:
                easygui.msgbox("账号不存在","查询账号")
                quit()
            ccddcc=open("C:\yx3.0\sj\cs"+str(dm)+".txt","r")
            ccd=ccddcc.read()
            ccddcc.close()
            zmz=open("C:\yx3.0\sj\cxxmz"+str(dm)+".txt","r")
            mz=zmz.read()
            zmz.close()
            zmm=open("C:\yx3.0\sj\cxxmm"+str(dm)+".txt","r")
            mm=zmm.read()
            zmm.close()
            ffccm=open("C:\yx3.0\sj\cxxcn"+str(dm)+".txt","r")
            wcn=int(ffccm.read())
            ffccm.close()
            mmm=easygui.passwordbox("请输入密码","查询账号")
            if mmm==None or mmm=="":
                mm="已隐藏"
            if mm==mmm:
                pass
            if mm!=mmm:
                mm="已隐藏，因为密码输入错误"
            if wcn==1:
                wcn="是"
            else:
                wcn="否"
            if ccd==1:
                ccd="是"
            else:
                ccd="否"
            easygui.msgbox("名字："+str(mz)+"\n密码："+str(mm)+"\n受防沉迷影响："+str(wcn)+"\n账号是否冻结："+str(ccd),"查询账号")
            
        if ww=="卸载游戏并删除游戏数据":
            ww=easygui.boolbox("确定要继续吗？","卸载游戏并删除游戏数据")
            if ww==True:
                os.system("start C:\yx3.0\sj\c.bat")
            quit()
        if ww=="开始游戏":
            gwm=easygui.boolbox("敢玩吗？？？",ti,("是","否"))
            if gwm==True:
                easygui.msgbox("好!",ti)
            else:
                easygui.msgbox("胆小鬼，拜拜",ti)
                
            while True:
                dm=easygui.integerbox("请输入用户代码\n如果你没有账号，请输入4",ti,None,1,4)
                if dm==None or dm=="":
                    hehe()
                    continue
                break
            bb=os.path.exists("C:\yx3.0\sj\cxxmz"+str(dm)+".txt")
            if bb==False:
                easygui.msgbox("用户代码错误",ti)
                quit()
            ccddcc=open("C:\yx3.0\sj\cs"+str(dm)+".txt","r")
            ccd=ccddcc.read()
            ccddcc.close()
            zmz=open("C:\yx3.0\sj\cxxmz"+str(dm)+".txt","r")
            mz=zmz.read()
            zmz.close()
            zmm=open("C:\yx3.0\sj\cxxmm"+str(dm)+".txt","r")
            mm=zmm.read()
            zmm.close()
            ffccm=open("C:\yx3.0\sj\cxxcn"+str(dm)+".txt","r")
            wcn=int(ffccm.read())
            ffccm.close()
            cs=0
            while True:
                if ccd=="1":
                        easygui.msgbox("账号已冻结,请重新注册",ti)
                        quit()
                if cs==3:
                        easygui.msgbox("账号已冻结,请重新注册",ti)
                        ccc=open("C:\yx3.0\sj\cs"+str(dm)+".txt","w")
                        ccc.write("1")
                        ccc.close()
                        quit()
                while True:
                    mmm=easygui.passwordbox("请输入密码\n如果你没有账号，请输入1234",ti)
                    if mmm==None or mmm=="":
                        hehe()
                        continue
                    break
                if mm==mmm:
                        easygui.msgbox("亲爱的"+mz+",您已登录成功",ti)
                        break
                if mm!=mmm:
                        easygui.msgbox("密码错误",ti)
                        cs=cs+1
                        continue
            if jjh==1:
                easygui.msgbox("已为您跳过小广告","小广告")
            else:
                easygui.msgbox("请看一段烦人的小广告","小广告")
                os.system("start C:\yx3.0\sj\c.mp4")
                time.sleep(180)
                easygui.buttonbox("好看吗？","小广告",["好看","除了好看还是好看","太好看了"])
                webbrowser.open("https://hi.codemao.cn/")
            yx=easygui.choicebox("请选择游戏",ti,["猜数字","该死的数学题","数方块"])
            if wcn==1:
                if time.strftime("%H")=="22" or time.strftime("%H")=="23" or time.strftime("%H")=="24" or time.strftime("%H")=="00" or time.strftime("%H")=="01" or time.strftime("%H")=="02" or time.strftime("%H")=="03" or time.strftime("%H")=="04" or time.strftime("%H")=="05" or time.strftime("%H")=="06" or time.strftime("%H")=="07":
                    easygui.msgbox("您是未成年人，为了您的健康，22点至次日8点将不能进行游戏，请合理安排游戏时间")
                    quit()
                from time import time
                pa=time()
                import time
            while yx=="猜数字":
                ti="猜数字"+str(jhzt)
                l=0
                while True:
                    w=easygui.choicebox("请选择游戏难度\n低为机会10次，猜数范围1-15\n中为机会5次，猜数范围1-20\n高为机会3次，猜数范围1-25\n变态难好像没人玩，机会100次，猜数范围0.0000000000000001-0.9999999999999999",ti,["低","中","高","变态难"])
                    if w==None or w=="":
                        hehe()
                        continue
                    if w=="低":
                        m=10
                        a = random.randint(1,15)
                    if w=="中":
                        m=5
                        a = random.randint(1,20)
                    if w=="高":
                        m=3
                        a = random.randint(1,25)
                    if w=="变态难":
                        m=100
                        a=random.random()
                    break
                easygui.msgbox("亲爱的"+str(mz)+",猜数字游戏开始了",ti)
                while True:
                    if m==0:
                        easygui.msgbox("机会已用完，下次再来\n正确答案是"+str(a)+"哦",ti)
                        p=easygui.boolbox("还玩吗",ti,("是","否"))
                        easygui.msgbox("好的",ti)
                        ttt = datetime.datetime.now()
                        zjj=open("C:\yx3.0\sj\zj.txt", "a")
                        zjj.write("名字："+str(mz)+"\n")
                        zjj.write("时间："+str(ttt)+"\n")
                        zjj.write("您的难度："+str(w)+"\n")
                        zjj.write("游戏：猜数字\n")
                        zjj.write("这是您人生的污点，机会被用完了\n")
                        zjj.write("\n")
                        zjj.write("--------------------i'm 分割线--------------------")
                        zjj.write("\n\n")
                        zjj.close()
                        easygui.msgbox("记得打开游戏目录下的的“zj.txt”查看战绩哦")
                        if p==True:
                            if wcn==1:
                                from time import time
                                pb=time()
                                import time
                                if pb-pa==5400:
                                    easygui.msgbox("您是未成年人或游客，为了您的健康，每天游戏时间不能超过1.5时，请合理安排游戏时间")
                                    quit()
                                if time.strftime("%H")=="22" or time.strftime("%H")=="23" or time.strftime("%H")=="24" or time.strftime("%H")=="00" or time.strftime("%H")=="01" or time.strftime("%H")=="02" or time.strftime("%H")=="03" or time.strftime("%H")=="04" or time.strftime("%H")=="05" or time.strftime("%H")=="06" or time.strftime("%H")=="07":
                                    easygui.msgbox("您是未成年人或游客，为了您的健康，22点至次日8点将不能进行游戏，请合理安排游戏时间")
                                    quit()
                            break
                        else:
                            easygui.msgbox("拜拜！",ti)
                            restart_program()
                    while True:
                        b=easygui.enterbox("请输入您的答案(请输入数字)","还剩"+str(m)+"次")
                        if b==None or b=="":
                            hehe()
                            continue
                        try:
                            float(b)
                        except:
                            continue
                        break
                    m=m-1
                    l=l+1
                    if float(b)==float(a):
                        easygui.msgbox("你过关了",ti)
                        if l==1:
                            easygui.msgbox("您简直是神仙，只用了1次",ti)
                        elif l<=3:
                            easygui.msgbox("您的智商简直比pig还高，只用了"+str(l)+"次",ti)
                        elif l<=5:
                            easygui.msgbox("您太腻害了，只用了"+str(l)+"次",ti)
                        else:
                            easygui.msgbox("您用了"+str(l)+"次，下次加油哦",ti)
                        p=easygui.boolbox("还玩吗",ti,("是","否"))
                        easygui.msgbox("好的",ti)
                        ttt = datetime.datetime.now()
                        zjj=open("C:\yx3.0\sj\zj.txt", "a")
                        zjj.write("名字："+str(mz)+"\n")
                        zjj.write("时间："+str(ttt)+"\n")
                        zjj.write("游戏：猜数字\n")
                        zjj.write("您的难度："+str(w)+"\n")
                        zjj.write("您用的次数："+str(l)+"\n")
                        zjj.write("\n")
                        zjj.write("--------------------i'm 分割线--------------------")
                        zjj.write("\n\n")
                        zjj.close()
                        easygui.msgbox("记得打开游戏目录下的的“zj.txt”查看战绩哦")
                        if p==True:
                            if wcn==1:
                                from time import time
                                pb=time()
                                import time
                                if pb-pa==5400:
                                    easygui.msgbox("您是未成年人或游客，为了您的健康，每天游戏时间不能超过1.5时，请合理安排游戏时间")
                                    quit()
                                if time.strftime("%H")=="22" or time.strftime("%H")=="23" or time.strftime("%H")=="24" or time.strftime("%H")=="00" or time.strftime("%H")=="01" or time.strftime("%H")=="02" or time.strftime("%H")=="03" or time.strftime("%H")=="04" or time.strftime("%H")=="05" or time.strftime("%H")=="06" or time.strftime("%H")=="07":
                                    easygui.msgbox("您是未成年人或游客，为了您的健康，22点至次日8点将不能进行游戏，请合理安排游戏时间")
                                    quit()
                            break
                        else:
                            easygui.msgbox("拜拜！",ti)
                            restart_program()
                    else:
                        if float(b)>float(a):
                            easygui.msgbox("大了",ti)
                        if float(b)<float(a):
                            easygui.msgbox("小了",ti)
            while yx=="该死的数学题":
                ti="该死的数学题"+str(jhzt)
                easygui.msgbox("亲爱的"+str(mz)+",该死的数学题游戏开始了，请在3秒内答对题目",ti)
                l=0
                from time import time
                while True:
                    start = time()
                    a=random.randint(1,20)
                    b=random.randint(1,20)
                    减法或加法a=random.randint(1,2)
                    减法或加法b=random.randint(1,2)
                    对或错=random.randint(1,2)
                    错=random.randint(1,5)
                    if 对或错==1: #对
                        if 减法或加法a==1: #减法
                            if a<b:
                                aa=easygui.boolbox(str(b)+"-"+str(a)+"="+str(b-a),ti,("对","错"))
                            if a>b:
                                aa=easygui.boolbox(str(a)+"-"+str(b)+"="+str(a-b),ti,("对","错"))
                            if a==b:
                                aa=easygui.boolbox(str(b)+"-"+str(a)+"=0",ti,("对","错"))
                        if 减法或加法a==2: #加法
                            aa=easygui.boolbox(str(a)+"+"+str(b)+"="+str(b+a),ti,("对","错"))
                    if 对或错==2: #错
                        if 减法或加法a==1:#减
                            if a<b:
                                c=b-a
                                if 减法或加法b==1:
                                    c=c-错
                                if 减法或加法b==2:
                                    c=c+错
                                aa=easygui.boolbox(str(b)+"-"+str(a)+"="+str(c),ti,("对","错"))
                            if a>b:
                                c=a-b
                                if 减法或加法b==1:
                                    c=c-错
                                if 减法或加法b==2:
                                    c=c+错
                                aa=easygui.boolbox(str(a)+"-"+str(b)+"="+str(c),ti,("对","错"))
                            if a==b:
                                c=0
                                if 减法或加法b==1:
                                    c=c-错
                                if 减法或加法b==2:
                                    c=c+错
                                aa=easygui.boolbox(str(a)+"-"+str(b)+"="+str(c),ti,("对","错"))
                        if 减法或加法a==2:#加
                            c=a+b
                            if 减法或加法b==1:
                                c=c-错
                            if 减法或加法b==2:
                                c=c+错
                            aa=easygui.boolbox(str(a)+"+"+str(b)+"="+str(c),ti,("对","错"))
                    stop = time()
                    if aa==None or b=="":
                        hehe()
                        continue
                    if 对或错==2:
                        if aa==False:
                            easygui.msgbox("回答正确",ti)
                            if int(stop-start)>3:
                                easygui.msgbox("但是时间已到",ti)
                                w=0
                                break
                            w=1
                            l=l+1
                            continue
                        if aa==True:
                            easygui.msgbox("回答错误",ti)
                            w=0
                            break
                        else:
                            quit()
                    if 对或错==1:
                        if aa==True:
                            easygui.msgbox("回答正确",ti)
                            if int(stop-start)>3:
                                easygui.msgbox("但是时间已到",ti)
                                w=0
                                break
                            w=1
                            l=l+1
                            continue
                        if aa==False:
                            easygui.msgbox("回答错误",ti)
                            w=0
                            break
                        else:
                            quit()
                p=easygui.boolbox("还玩吗",ti,("是","否"))
                easygui.msgbox("好的",ti)
                ttt = datetime.datetime.now()
                zjj=open("C:\yx3.0\sj\zj.txt", "a")
                zjj.write("名字："+str(mz)+"\n")
                zjj.write("时间："+str(ttt)+"\n")
                zjj.write("游戏：该死的数学题\n")
                zjj.write("您成功的次数："+str(l)+"\n")
                zjj.write("\n")
                zjj.write("--------------------i'm 分割线--------------------")
                zjj.write("\n\n")
                zjj.close()
                easygui.msgbox("记得打开游戏目录下的的“zj.txt”查看战绩哦")
                if p==True:
                    if wcn==1:
                        from time import time
                        pb=time()
                        import time
                        if pb-pa>5400:
                            easygui.msgbox("您是未成年人或游客，为了您的健康，每天游戏时间不能超过1.5时，请合理安排游戏时间")
                            quit()
                        if time.strftime("%H")=="22" or time.strftime("%H")=="23" or time.strftime("%H")=="24" or time.strftime("%H")=="00" or time.strftime("%H")=="01" or time.strftime("%H")=="02" or time.strftime("%H")=="03" or time.strftime("%H")=="04" or time.strftime("%H")=="05" or time.strftime("%H")=="06" or time.strftime("%H")=="07":
                            easygui.msgbox("您是未成年人或游客，为了您的健康，22点至次日8点将不能进行游戏，请合理安排游戏时间")
                            quit()
                    continue
                else:
                    break
            while yx=="数方块":
                ti="数方块"
                easygui.msgbox("亲爱的"+str(mz)+",该死的数学题游戏开始了，请答对随机抽取的10道题目",ti)
                y=0;n=0
                c=time.time()
                while not y+n==10:
                    while True:
                        a=random.randint(1,60)
                        if os.path.exists("C:\yx3.0\sj\sfk\sfk"+str(a)+".jpg")==False:
                            continue
                        else:
                            break
                    while True:
                        os.system("start C:\yx3.0\sj\sfk\sfk"+str(a)+".jpg")
                        b=easygui.enterbox("有多少个方块？(请输入数字)",ti)
                        if b==None or b=="":
                            hehe()
                            continue
                        try:
                            int(b)
                        except:
                            continue
                        break
                    if b==a:
                        easygui.msgbox("对了",ti)
                        y=y+1
                    else:
                        easygui.msgbox("错了",ti)
                        n=n+1
                d=time.time()-c
                easygui.msgbox("恭喜你完成了挑战，对了"+str(y)+"次，错了"+str(n)+"次",ti)
                p=easygui.boolbox("还玩吗",ti,("是","否"))
                easygui.msgbox("好的",ti)
                ttt = datetime.datetime.now()
                zjj=open("C:\yx3.0\sj\zj.txt", "a")
                zjj.write("名字："+str(mz)+"\n")
                zjj.write("时间："+str(ttt)+"\n")
                zjj.write("游戏：数方块\n")
                zjj.write("您答对的次数："+str(y)+"\n")
                zjj.write("您答错的次数："+str(n)+"\n")
                zjj.write("您用的时间："+str(d)+"\n")
                zjj.write("\n")
                zjj.write("--------------------i'm 分割线--------------------")
                zjj.write("\n\n")
                zjj.close()
                easygui.msgbox("记得打开游戏目录下的的“zj.txt”查看战绩哦")
                if p==True:
                    if wcn==1:
                        from time import time
                        pb=time()
                        import time
                        if pb-pa>5400:
                            easygui.msgbox("您是未成年人或游客，为了您的健康，每天游戏时间不能超过1.5时，请合理安排游戏时间")
                            quit()
                        if time.strftime("%H")=="22" or time.strftime("%H")=="23" or time.strftime("%H")=="24" or time.strftime("%H")=="00" or time.strftime("%H")=="01" or time.strftime("%H")=="02" or time.strftime("%H")=="03" or time.strftime("%H")=="04" or time.strftime("%H")=="05" or time.strftime("%H")=="06" or time.strftime("%H")=="07":
                            easygui.msgbox("您是未成年人或游客，为了您的健康，22点至次日8点将不能进行游戏，请合理安排游戏时间")
                            quit()
                    continue
                else:
                    break
    quit()
except:
    if cw==1:
        easygui.exceptionbox("出了点小问题，即将退出\n如果有需要，以下信息可能对你有帮助","啊哦")
    if qs==1:
        input("按回车键退出 . . .")
        exit()
    if qs==0:
        exit()

####邓叉叉制作####
