import sys, random

from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5 import uic

from UI import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.is_clicked = False
        self.qp = QPainter()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        if self.is_clicked:
            n = random.randint(2, 5)
            for i in range(n):
                self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                d = random.randint(1, 300)
                x = random.randint(1, 300)
                y = random.randint(1, 300)
                self.qp.drawEllipse(QtCore.QRect(x, y, d, d))

    def btn_clicked(self):
        self.is_clicked = True
        self.update()


app = QApplication(sys.argv)
mainwindow = Circles()
mainwindow.show()
sys.exit(app.exec_())