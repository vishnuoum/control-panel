import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *
app=QtWidgets.QApplication(sys.argv)
w=QWebEngineView()
w.load(QtCore.QUrl('http://zateart.com/covidapp/cp/index.php')) ## load google on startup
w.showMaximized()
w.setWindowTitle("Control Panel")
w.setWindowIcon(QtGui.QIcon('icon.png'))
app.exec_()
