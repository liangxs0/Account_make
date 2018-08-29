from PyQt5.QtWidgets import QApplication
import sys
from mainWindow import mainWindow
import acount
from Figure import Draw

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mainWindow()
    MainWindow.initUI()
    sys.exit(app.exec_())

