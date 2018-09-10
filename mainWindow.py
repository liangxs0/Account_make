#--utf8---
#界面绘制函数
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
                QLineEdit,QLabel,QPushButton,QToolTip,\
                QInputDialog,QMessageBox,QHBoxLayout,\
                QMouseEventTransition
from PyQt5.QtGui import QIcon,QFont,QPixmap,QColor,QBrush
from PyQt5 import QtGui,Qt
import pyglet
from xlrd import open_workbook
from acount import write_excel,creat_excel,Add_money

import time
btn_x = 280
btn_y = 560
btn_x0 = 750
btn_y0 = 10

le_Edit_x = 160
le_Edit_y = 200

class mainWindow(QWidget):
    def __int__(self):
        super().__init__()
        self.initUI()
        #主窗体的初始化
    def initUI(self):

        # 设置背景图
        '''
        Back_Ground = QHBoxLayout(self)
        pixmap = QPixmap("./source/background.png")
        back = QLabel(self)
        back.setPixmap(pixmap)
        Back_Ground.addWidget(back)
        self.setLayout(Back_Ground)'''

        self.bgpal = self.palette()
        self.bgpal.setBrush(self.backgroundRole(),QBrush(QPixmap('./source/background2.png')))
        self.setPalette(self.bgpal)

        self.btn_ok = QPushButton('确认',self)
        self.btn_no = QPushButton('取消',self)
        self.btn_Min = QPushButton('最小化',self)
        self.btn_Max = QPushButton('最大化',self)
        self.btn_close = QPushButton('关闭',self)

        self.btn_ok.move(btn_x, btn_y)
        self.btn_no.move(btn_x + 270, btn_y)
        self.btn_Min.move(btn_x0,btn_y0)
        self.btn_Max.move(btn_x0+80,btn_y0)
        self.btn_close.move(btn_x0+150,btn_y0)

        self.btn_ok.resize(100,150)
        self.btn_no.resize(100, 150)
        self.btn_Min.resize(50,50)
        self.btn_Max.resize(50,50)
        self.btn_close.resize(50, 50)
        self.btn_ok.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.btn_no.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.btn_Min.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.btn_Max.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.btn_close.setStyleSheet('background:transparent;border-width:0;border-style:outset')

        #槽函数绑定
        self.btn_ok.clicked.connect(self.btn_Ok)
        self.btn_no.clicked.connect(self.btn_No)
        self.btn_close.clicked.connect(self.closeEvent)

        #self.la_money.move(self.le_money.x()+self.le_money.size().width(),)
        self.le_money = QLineEdit(self)
        self.le_remark = QLineEdit(self)
        self.la_allmony = QLabel(self)
        self.le_money.move(le_Edit_x,le_Edit_y-55)
        self.le_remark.move(le_Edit_x,le_Edit_y+80)
        self.la_allmony.move(le_Edit_x+400,le_Edit_y-55)
        self.la_allmony.resize(320,30)
        self.le_remark.resize(320, 90)
        self.le_money.resize(320,30)
        self.le_money.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.le_remark.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        self.le_money.setText('0')
        self.le_remark.setText('无')
        self.la_allmony.setText('0')
        #self.le_remark.setStyleSheet('QLineEdit{border-image:url(./source/btn_ok.png)}')


        #设置logo
        self.setGeometry(200, 200, 996, 720)
        self.setWindowIcon(QIcon('./source/Title.png'))
        self.setWindowTitle('Account')
        #self.setStyleSheet("QWidget#mainWindow{border-radius:15px;}")
        #标题框去除
        #self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.setWindowFlags((Qt.Qt.FramelessWindowHint))
        self.show()

        #背景透明
        #self.setWindowOpacity(80)



    def btn_Ok(self):
        money = self.le_money.text()
        remark = self.le_remark.text()
        try:
            excel = open_workbook('account.xls', encoding_override='utf8')
        except :
            creat_excel()
            write_excel(money, remark)
        else:
            write_excel(money, remark)

        self.la_allmony.setText(str(Add_money()))
    def btn_No(self):
        print('放弃')


    def closeEvent(self,event):
        reply = QMessageBox.question(self,"Message","确认退出吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def mouseReleaseEvent(self, QmouseEvent):
        if self.underMouse():
            print("b")
        if self.releaseMouse():
            print("a")

    def Gif(self):

        self.animation = pyglet.resource.animation('./source/gif.gif')
        self.sprite = pyglet.sprite.Sprite(self.animation)
        self.win = pyglet.window.Window(width=self.sprite,height=self.sprite)
        self.win.clear()
        self.sprite.draw()
        pyglet.app.run()