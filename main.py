from PyQt5.QtWidgets import QApplication
import sys
from mainWindow import mainWindow
from DrawLine import DrawLine
from PyQt5 import *
import acount
from Figure import Draw

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mainWindow()
    MainWindow.initUI()
    DrawLine()
    sys.exit(app.exec_())

