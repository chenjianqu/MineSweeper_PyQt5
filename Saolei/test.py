# _*_ coding:utf-8 _*_
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,QLayoutItem)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        #设置窗口属性
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('创建主窗口')
        self.setWindowIcon(QIcon(r"E:\\abcd.jpg"))
        #设置状态栏
        self.status = self.statusBar()
        self.status.showMessage('我是状态栏', 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv[1:])
    window = MainWindow()
    window.show()
    t=QLayoutItem()
    
    sys.exit(app.exec_())

    

