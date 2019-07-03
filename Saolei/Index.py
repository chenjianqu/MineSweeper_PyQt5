import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from content import Content
 
class Index(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.basePath=os.path.join(os.getcwd(),'Saolei')
        
    def initUI(self):    
        self.btnQuit = QPushButton('退出游戏', self)
        self.btnQuit.resize(self.btnQuit.sizeHint())
        self.btnQuit.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')

        self.btnStart8x8 = QPushButton('开始游戏-8x8', self)
        self.btnStart8x8.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.btnStart8x8.resize(self.btnStart8x8.sizeHint())

        self.btnStart16x16 = QPushButton('开始游戏-16x16', self)
        self.btnStart16x16.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.btnStart16x16.resize(self.btnStart16x16.sizeHint())

        self.btnStart16x30 = QPushButton('开始游戏-16x30', self)
        self.btnStart16x30.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.btnStart16x30.resize(self.btnStart16x30.sizeHint())

        self.btnStart30x20 = QPushButton('开始游戏-30x20', self)
        self.btnStart30x20.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.btnStart30x20.resize(self.btnStart30x20.sizeHint())

        self.btnAbout = QPushButton('关于作者', self)
        self.btnAbout.setStyleSheet('font-size:20px;font-family:"黑体";color:rgb(150,150,255)')
        self.btnAbout.resize(self.btnAbout.sizeHint())
        

        vbox = QVBoxLayout()#纵向布局
        vbox.addStretch(1)#添加伸展因子
        vbox.addWidget(self.btnStart8x8)
        vbox.addWidget(self.btnStart16x16)
        vbox.addWidget(self.btnStart16x30)
        vbox.addWidget(self.btnStart30x20)
        vbox.addWidget(self.btnAbout)
        vbox.addWidget(self.btnQuit)
        vbox.addStretch(1)
        
        hbox = QHBoxLayout()#横向布局
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        widget=QWidget()
        widget.setLayout(hbox)#把布局放到widget
        self.setCentralWidget(widget) #把widget放到window里面

        iconPath=os.path.join(os.getcwd(),r'Saolei/res/icon/window.png')#设置图标
        self.setWindowIcon(QIcon(iconPath))
        self.setWindowTitle('扫雷-主菜单')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def aboutMe(self):
        reply = QMessageBox.question(self, '关于作者', 'Coded by 陈建驱 \n Github:Github：https://github.com/chenjianqu \n'+\
            '个人博客：www.chenjianqu.com', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pass
        else:
            self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    index = Index()
    content=Content()

    index.btnQuit.clicked.connect(QCoreApplication.instance().quit)
    index.btnStart8x8.clicked.connect(content.setSize8x8)
    index.btnStart16x16.clicked.connect(content.setSize16x16)
    index.btnStart16x30.clicked.connect(content.setSize16x30)
    index.btnStart30x20.clicked.connect(content.setSize30x20)
    index.btnAbout.clicked.connect(index.aboutMe)

    sys.exit(app.exec_())  