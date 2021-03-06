import cv2,numpy,time,random
import os,sys,pyautogui, traceback
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
import numpy as np
import action

# 读取文件 精度控制   显示名字
imgs = action.load_imgs()
pyautogui.PAUSE = 0.1

start_time = time.time()
#print('程序启动，现在时间', time.ctime())


#以上启动，载入设置
##########################################################

def log(f):
    def wrap(*agrs, **kwagrs):
        try:
            ans = f(*agrs, **kwagrs)
            return ans
        except:
            traceback.print_exc()
            time.sleep(60)

    return wrap

@log
def select_mode():
    print('''\n菜单：  鼠标移动到最右侧中止并返回菜单页面,
        1 结界突破
        2 自动御魂通关(司机)
        3 自动御魂通关(打手)
        4 自动御魂通关(单刷)
        5 自动探索副本(打手)，          
        6 自动探索副本(单刷)
        7 百鬼夜行
        8 斗技
        9 当前活动
        10 结界自动合卡，自动选择前三张合成
        11 抽卡
        ''')
    action.alarm(1)
    raw = input("选择功能模式：")
    index = int(raw)

    mode = [0, tupo, yuhun, yuhun2, yuhundanren, goliang, solo, baigui, douji, huodong, card,chouka]
    comand = mode[index]
    comand()

##########################################################
#结节突破
def tupo():
    cishu = 0
    while True :   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1426, 798)
        a,b = upleft
        c,d = downright
        
        screen=np.array(ImageGrab.grab().convert('RGB'))
        screen = screen[b:d,a:c]

        #确定刷新
        want = imgs['queding']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('选择结节')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)
        
        #选择突破
        want = imgs['lingxunzhang']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('选择结节')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            t = random.randint(50,100) / 100
            time.sleep(t)

        #截屏
        screen=np.array(ImageGrab.grab().convert('RGB'))
        screen = screen[b:d,a:c]

        #开始突破
        want = imgs['jingong']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            if cishu >= 30:
                select_mode()
            cishu = cishu + 1
            print('进攻次数：',cishu)
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            t = random.randint(150,200) / 100
            time.sleep(t)
        
        #奖励
        for i in ['jujue','shuaxin','jiangli','jixu','shibai']:
            want=imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target=screen
            pts=action.locate(target,want,0)
            if not len(pts)==0:
                for pt in pts:
                    pt = action.cheat(pt, w, h)
                    pyautogui.click(pt)
                    t = random.randint(100,200) / 100
                    time.sleep(t)
                break


########################################################
#御魂司机
def yuhun():
    while True :
        #鼠标移到最右侧中止    
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (2550, 770) #上部并排

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('screen shot ok',time.ctime())
        #体力不足
        want = imgs['notili']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('体力不足: ',pts[0])
            select_mode()

        #确定退出
        want = imgs['queding']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('确定退出')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)
            
        #自动点击通关结束后的页面
        for i in ['jujue','yuhuntiaozhan','ying','jiangli','jiangli2','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                for pt in pts:
                    print('挑战中。。。')
                    pt = action.cheat(pt, w, h)
                    pyautogui.click(pt)
                    t = random.randint(200,300) / 1000
                    time.sleep(t)
                break
    
########################################################
#御魂打手
def yuhun2():
    while True :
        #鼠标移到最右侧中止    
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1426, 798)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('screen shot ok',time.ctime())
        #体力不足
        want = imgs['notili']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('体力不足: ',pts[0])
            select_mode()

        #确定退出
        want = imgs['queding']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('确定退出')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)
            
        #如果队友推出则自己也退出
        want = imgs['kaishizhandou']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('队友已退出')
            want = imgs['likaiduiwu']
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)
                
        
        #自动点击通关结束后的页面
        for i in ['jujue','jieshou2','jieshou','ying','jiangli','kaishi','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                for pt in pts:
                    print('挑战中。。。')
                    pt = action.cheat(pt, w, h)
                    pyautogui.click(pt)
                    t = random.randint(200,350) / 1000
                    time.sleep(t)
                break
            

########################################################
#御魂单人
def yuhundanren():
    while True :   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1426, 798)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('screen shot ok',time.ctime())
        
        #体力不足
        want = imgs['notili']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('体力不足')
            select_mode()
            
        #过关
        for i in ['jujue','ying','jiangli','tiaozhan','jixu']:
            want=imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target=screen
            pts=action.locate(target,want,0)
            if not len(pts)==0:
                print('挑战中。。。')
                for pt in pts:
                    pt = action.cheat(pt, w, h)
                    pyautogui.click(pt)
                    t = random.randint(20,50) / 100
                    time.sleep(t)
                break

########################################################
#组队探索
def goliang():
    while True:   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        #screen = ImageGrab.grab()
        #screen.save('screen.png')
        #screen = cv2.imread('screen.png')
        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (2550, 768)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('cursor:',pyautogui.position())
        
        #设定目标，开始查找
        #进入后
        want = imgs['guding']

        x1 = (785, 606)
        x2 = downright
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('正在地图中')
            
            want = imgs['xiao']
            x1,x2 = (5, 405), (119, 560)
            target = action.cut(screen, x1, x2)
            pts = action.locate(target,want,0)
            
            if not len(pts) == 0:
                print('组队状态中')
            else:
                print('退出重新组队')
                
                for i in ['queren', 'tuichu']:
                    want = imgs[i]
                    size = want[0].shape
                    h, w , ___ = size
                    x1,x2 = upleft, (965, 522)
                    target = action.cut(screen, x1, x2)
                    pts = action.locate(target,want,0)
                    
                    if not len(pts) == 0:
                        print('退出中',pts[0])
                        try:
                            queding = pts[1]
                        except:
                            queding = pts[0]
                        queding = action.cheat(queding, w, h)
                        pyautogui.click(queding)
                        t = random.randint(50,80) / 100
                        time.sleep(t)
                        break
                continue

        want = imgs['jieshou']
        size = want[0].shape
        h, w , ___ = size
        x1,x2 = upleft, (250, 380)
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('接受组队')
            xx = pts[0]
            xx = action.cheat(xx, w, h)
            if xx[0] > 120:           
                pyautogui.click(xx)
                t = random.randint(40,80) / 100
                time.sleep(t)
            else:
                pass
            continue

        for i in ['jujue','ying','jiangli','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('领取奖励')
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                t = random.randint(30,80) / 100
                time.sleep(t)
                break

########################################################
#单人探索
def solo():
    while True:   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 900)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('screen shot ok',time.ctime())
        #print(pyautogui.position())
        #体力不足
        want = imgs['notili']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('体力不足: ',pts[0])
            select_mode()


        
        want = imgs['queren']
        size = want[0].shape
        h, w , ___ = size
        x1,x2 = upleft, (965, 522)
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('确认退出')
            try:
                queding = pts[1]
            except:
                queding = pts[0]
            xy = action.cheat(queding, w, h)
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

        
        #设定目标，开始查找
        #进入后
        want=imgs['guding']

        x1 = (785, 606)
        x2 = downright
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('正在地图中')
            
            want = imgs['left']
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                right = (854, 527)
                right = action.cheat(right, 10, 10)
                pyautogui.click(right)
                t = random.randint(50,80) / 100
                time.sleep(t)
                continue

            want = imgs['jian']
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('点击小怪')
                xx = action.cheat(pts[0], 10, 10)        
                pyautogui.click(xx)
                time.sleep(0.5)
                continue
            else:
                for i in ['queren', 'tuichu']:
                    want = imgs[i]
                    size = want[0].shape
                    h, w , ___ = size
                    x1,x2 = upleft, (965, 522)
                    target = action.cut(screen, x1, x2)
                    pts = action.locate(target,want,0)
                    if not len(pts) == 0:
                        print('退出中')
                        try:
                            queding = pts[1]
                        except:
                            queding = pts[0]
                        queding = action.cheat(queding, w, h)
                        pyautogui.click(queding)
                        t = random.randint(50,80) / 100
                        time.sleep(t)
                        break
                continue

        for i in ['jujue','ying','jiangli','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('领取奖励')
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)
                break

        want = imgs['tansuo']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('进入地图: ',pts[0])
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

########################################################
#百鬼
def baigui():
    while True:   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        #print('screen shot ok',time.ctime())
        #print(pyautogui.position())
        
        #设定目标，开始查找
        #进入后
        want=imgs['inbaigui']
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('正在百鬼中')
            
            want = imgs['blank']
            target = screen
            pts = action.locate(target,want,0)
            if len(pts) == 0:
                #小怪出现！
                print('点击小怪')
                pts2 = (640, 450)
                xx = action.cheat(pts2, 10, 10)        
                pyautogui.click(xx)
                time.sleep(0.5)
                continue

        want = imgs['jinru']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('进入百鬼: ',pts[0])
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

        want = imgs['kaishi']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('选择界面: ',pts[0])

            want = imgs['ya']
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts2 = action.locate(target,want,0)
            if not len(pts2) == 0:
                print('点击开始: ',pts[0])
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                pyautogui.moveTo(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)
            else:
                #选择押注
                index=random.randint(0,2)
                pts2 = (300+index*340, 500)
                
                xy = action.cheat(pts2, w, h-10 )
                pyautogui.click(xy)
                pyautogui.moveTo(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)

                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                pyautogui.moveTo(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)

        want = imgs['fenxiang']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('结束界面: ',pts[0])
            pts[0]=(1200, 100)
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

########################################################
#斗技
def douji():
    while True:   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        for i in ['douji','doujiend','ying','doujiqueren','tui','doujiother']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('领取奖励')
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)
                break

########################################################
#当前活动
def huodong():
    while True:   #直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        screen=np.array(ImageGrab.grab().convert('RGB'))

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        want = imgs['xiayihui']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('下一回 ',pts[0])
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

        for i in ['jujue','huodongtiaozhan','jiangli','jixu','zhunbei','yun']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('活动中。。。')
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)
                break

        #体力不足
        want = imgs['notili']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('体力不足')
            select_mode()

##########################################################
#合成结界卡，较简单，未偏移直接点
def card():
    while True:
        #鼠标移到右侧中止    
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        #截图
        screen=np.array(ImageGrab.grab().convert('RGB'))
        
        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        want = imgs['taiyin2']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if len(pts) == 0:
                print('结界卡不足')
                select_mode()
        else:
            print('结界卡*')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

        for i in range(2):
            #截图
            screen=np.array(ImageGrab.grab().convert('RGB'))

            #截屏，并裁剪以加速
            upleft = (0, 0)
            downright = (1358, 768)
            downright2 = (1280, 720)

            a,b = upleft
            c,d = downright
            screen = screen[b:d,a:c]

            want = imgs['taiyin']
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if len(pts) == 0:
                print('结界卡不足')
                select_mode()
            else:
                print('结界卡',i)
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                pyautogui.moveTo(xy)
                t = random.randint(15,30) / 100
                time.sleep(t)

        #截图
        screen=np.array(ImageGrab.grab().convert('RGB'))
        
        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        want = imgs['hecheng']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('合成中。。。')
            xy = action.cheat(pts[0], w, h-10 )
            pyautogui.click(xy)
            pyautogui.moveTo(xy)
            t = random.randint(15,30) / 100
            time.sleep(t)

        t = random.randint(15,30) / 100
        time.sleep(1)

##########################################################
#抽卡
def chouka():
    while True:
        #鼠标移到右侧中止    
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()

        #截图
        screen=np.array(ImageGrab.grab().convert('RGB'))
        
        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (1280, 720)

        a,b = upleft
        c,d = downright
        screen = screen[b:d,a:c]

        for i in ['cezhi','zaicizhaohuan']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('抽卡中。。。')
                xy = action.cheat(pts[0], w, h-10 )
                pyautogui.click(xy)
                #t = random.randint(1,3) / 100
                #time.sleep(t)
                break
####################################################
if __name__ == '__main__':
    select_mode()

