import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import os
from kernel import Brick
from functools import partial
from mButton import MyButton
import time


class Content(QMainWindow):
    def __init__(self):
        super().__init__()
        self.size=(8,8)
        self.n=10
        self.kernal=None
        self.initMenu(self)
    
    def setSize8x8(self):
        self.size=(8,8)
        self.n=10
        self.initUI()
        self.show()
    
    def setSize16x16(self):
        self.size=(16,16)
        self.n=30
        self.initUI()
        self.show()

    def setSize16x30(self):
        self.n=40
        self.size=(16,30)
        self.initUI()
        self.show()

    def setSize30x20(self):
        self.n=100
        self.size=(30,20)
        self.initUI()
        self.show()

    #单击
    def display(self,btn):
        pos=eval(btn.objectName())#解析位置元组
        self.expand(pos)
    
    def expand(self,pos):
        if(self.kernal.OpenFlagArr[pos[0],pos[1]]==1 or self.kernal.OpenFlagArr[pos[0],pos[1]]==2):#掀开这个方块的标记
            return

        n=self.kernal.getSurplusNumber()
        self.lblNumber.setText('剩余数量：'+str(n))

        if(self.kernal.isVictory()):
            self.victory()

        self.kernal.OpenFlagArr[pos[0],pos[1]]=1
        n=self.kernal.getBrickArr()[pos[0],pos[1]]#获得对应的值
        #获取gridlayout中对应的按钮
        lyitem=self.grid.itemAtPosition(pos[0],pos[1])
        btn=lyitem.widget()
        btn.setStyleSheet("background-color:rgb(200,200,255)")

        if(n==10):
            btn.setText('*')
            btn.setStyleSheet("background-color:rgb(150,255,150)")
            self.failure()
        elif(n==0):
            btn.setText('')
            i=pos[0]
            j=pos[1]
            #四个角落的值
            if(i==0 and j==0):
                self.expand((i,j+1))
                self.expand((i+1,j))
                self.expand((i+1,j+1))
            elif(i==self.size[0]-1 and j==0):
                self.expand((i-1,j))
                self.expand((i,j+1))
                self.expand((i-1,j+1))
            elif(i==0 and j==self.size[1]-1):
                self.expand((i,j-1))
                self.expand((i+1,j))
                self.expand((i+1,j-1))
            elif(i==self.size[0]-1 and j==self.size[1]-1):
                self.expand((i,j-1))
                self.expand((i-1,j))
                self.expand((i-1,j-1))
            #四个边缘的值
            elif(i==0):
                self.expand((i,j-1))
                self.expand((i,j+1))
                self.expand((i+1,j-1))
                self.expand((i+1,j))
                self.expand((i+1,j+1))
            elif(i==self.size[0]-1):
                self.expand((i-1,j-1))
                self.expand((i-1,j))
                self.expand((i-1,j+1))
                self.expand((i,j-1))
                self.expand((i,j+1))
            elif(j==0):
                self.expand((i-1,j))
                self.expand((i-1,j+1))
                self.expand((i,j+1))
                self.expand((i+1,j))
                self.expand((i+1,j+1))
            elif(j==self.size[1]-1):
                self.expand((i-1,j-1))
                self.expand((i-1,j))
                self.expand((i,j-1))
                self.expand((i+1,j-1))
                self.expand((i+1,j))
            else:
                self.expand((i-1,j-1))
                self.expand((i-1,j))
                self.expand((i-1,j+1))
                self.expand((i,j-1))
                self.expand((i,j+1))
                self.expand((i+1,j-1))
                self.expand((i+1,j))
                self.expand((i+1,j+1))
        else:
            btn.setText(str(n))
        
    def victory(self):
        self.timer.stop()
        reply = QMessageBox.question(self, '结果', '恭喜你，你赢了', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass
    
    def failure(self):
        self.timer.stop()
        reply = QMessageBox.question(self, '结果', '你输了', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass

    #右击，设定方块标记
    def markBrick(self,btn):
        pos=eval(btn.objectName())
        if(self.kernal.OpenFlagArr[pos[0],pos[1]]==0):
            self.kernal.OpenFlagArr[pos[0],pos[1]]=2
            if(self.kernal.isVictory()):
                self.victory()
            btn.setStyleSheet("background-color:rgb(255,150,150)")
        else:
            self.kernal.OpenFlagArr[pos[0],pos[1]]=0
            btn.setStyleSheet("background-color:rgb(230,230,230)")
        n=self.kernal.getSurplusNumber()
        self.lblNumber.setText('剩余数量：'+str(n))

    #双击
    def dbButton(self,pos):
        lyitem=self.grid.itemAtPosition(pos[0],pos[1])
        btn=lyitem.widget()
        self.display(btn)


    def doubleHandle(self,btn):
        pos=eval(btn.objectName())
        if(self.kernal.isNoBomb(pos)):
            i=pos[0]
            j=pos[1]
            #四个角落的值
            if(i==0 and j==0):
                self.dbButton((i,j+1))
                self.dbButton((i+1,j))
                self.dbButton((i+1,j+1))
            elif(i==self.size[0]-1 and j==0):
                self.dbButton((i-1,j))
                self.dbButton((i,j+1))
                self.dbButton((i-1,j+1))
            elif(i==0 and j==self.size[1]-1):
                self.dbButton((i,j-1))
                self.dbButton((i+1,j))
                self.dbButton((i+1,j-1))
            elif(i==self.size[0]-1 and j==self.size[1]-1):
                self.dbButton((i,j-1))
                self.dbButton((i-1,j))
                self.dbButton((i-1,j-1))
            #四个边缘的值
            elif(i==0):
                self.dbButton((i,j-1))
                self.dbButton((i,j+1))
                self.dbButton((i+1,j-1))
                self.dbButton((i+1,j))
                self.dbButton((i+1,j+1))
            elif(i==self.size[0]-1):
                self.dbButton((i-1,j-1))
                self.dbButton((i-1,j))
                self.dbButton((i-1,j+1))
                self.dbButton((i,j-1))
                self.dbButton((i,j+1))
            elif(j==0):
                self.dbButton((i-1,j))
                self.dbButton((i-1,j+1))
                self.dbButton((i,j+1))
                self.dbButton((i+1,j))
                self.dbButton((i+1,j+1))
            elif(j==self.size[1]-1):
                self.dbButton((i-1,j-1))
                self.dbButton((i-1,j))
                self.dbButton((i,j-1))
                self.dbButton((i+1,j-1))
                self.dbButton((i+1,j))
            else:
                self.dbButton((i-1,j-1))
                self.dbButton((i-1,j))
                self.dbButton((i-1,j+1))
                self.dbButton((i,j-1))
                self.dbButton((i,j+1))
                self.dbButton((i+1,j-1))
                self.dbButton((i+1,j))
                self.dbButton((i+1,j+1))


    def initUI(self):
        self.grid = QGridLayout()
        self.kernal=Brick(self.size,self.n)

        if(self.size[1]==8):
            brickSize=(80,60)
            self.grid.setSpacing(6)#设置组件之间的间距。
        elif(self.size[1]==16):
            brickSize=(50,40)
            self.grid.setSpacing(4)
        elif(self.size[1]==30):
            brickSize=(40,30)
            self.grid.setSpacing(1)
        elif(self.size[0]==30):
            brickSize=(40,20)
            self.grid.setSpacing(1)

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                button=MyButton("")
                button.setObjectName(str((i,j)))
                button.setFixedSize(brickSize[0],brickSize[1])
                button.setStyleSheet("font-size:20px;background-color:rgb(230.230.230)")
                button.c.leftClick.connect(partial(self.display,button))
                button.c.rightClick.connect(partial(self.markBrick,button))
                button.c.doubleClick.connect(partial(self.doubleHandle,button))
                self.grid.addWidget(button,i,j)

        self.lblTimer = QLabel('时间',self)
        self.lblTimer.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.lblNumber = QLabel('剩余',self)
        self.lblNumber.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTimer)
        self.timer.start()
        self.initTime=time.time()
        lblLayout=QHBoxLayout()
        lblLayout.addWidget(self.lblNumber)
        lblLayout.addWidget(self.lblTimer)

        self.mainLayout=QVBoxLayout()
        self.mainLayout.addLayout(lblLayout)
        self.mainLayout.addLayout(self.grid)


        widget=QWidget()
        widget.setLayout(self.mainLayout)#把布局放到widget
        self.setCentralWidget(widget) #把widget放到window里面

    
    def showTimer(self):
        deltaTime=time.time()-self.initTime
        self.lblTimer.setText(str(deltaTime))



    @staticmethod
    def initMenu(self):
        #退出游戏
        self.basePath=os.path.join(os.getcwd(),'Saolei')
        pathIcon=os.path.join(self.basePath,r'res/icon/close.png')
        exitAction = QAction(QIcon(pathIcon), '&退出', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        #回到主菜单
        pathIcon=os.path.join(self.basePath,r'res/icon/toindex.png')
        backAction = QAction(QIcon(pathIcon), '&回到首页', self)        
        backAction.setShortcut('Ctrl+B')
        backAction.setStatusTip('Back to index')
        backAction.triggered.connect(self.close)

        self.statusBar()
 
        #创建一个菜单栏
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')#添加菜单
        fileMenu.addAction(exitAction)#添加事件
        fileMenu.addAction(backAction)#添加事件
        
        #创建一个工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(backAction)
        
        iconPath=os.path.join(os.getcwd(),r'Saolei/res/icon/window.png')#设置图标
        self.setWindowIcon(QIcon(iconPath))
        self.setWindowTitle('扫雷-游戏界面')
        
        self.setGeometry(300, 300, 300, 200)
