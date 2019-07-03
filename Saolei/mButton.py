from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QObject,pyqtSignal
import sys
from PyQt5.QtGui import QFont   
import time


class MySignal(QObject):
    doubleClick=pyqtSignal()
    rightClick=pyqtSignal()
    leftClick=pyqtSignal()


class MyButton(QPushButton):
    def __init__(self,text,parent=None):
        super().__init__(text,parent)
        self.c=MySignal()
        self.lastTime=0
    
    def mousePressEvent(self,e):
        #当信号发射时，连接的槽函数将会自动执行。
        if(e.buttons()==Qt.RightButton):
            self.c.rightClick.emit()
        elif(e.buttons()==Qt.LeftButton):#左键事件处理
            current=time.time()
            delta=current-self.lastTime
            self.lastTime=current
            if(delta<0.2):#鼠标双击时
                self.c.doubleClick.emit()
            else:
                self.c.leftClick.emit()
        

'''
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def test(self):
        print("ok")

    def test1(self):
        print("test1")
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = MyButton('Button', self)

        btn.c.rightClick.connect(self.test)
        btn.c.doubleClick.connect(self.test1)

        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''