from PyQt5 import QtGui
from time import sleep
x = QtGui.QWindow()
x.create()
x.baseSize()
x.show()
sleep(5)
x.destroy()