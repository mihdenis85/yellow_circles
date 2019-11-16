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
        self.circles = []
        self.n = 0

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        for i in range(self.n):
            self.qp.setBrush(self.circles[i][-1])
            d = self.circles[i][0]
            x = self.circles[i][1]
            y = self.circles[i][2]
            self.qp.drawEllipse(QtCore.QRect(x, y, d, d))

    def btn_clicked(self):
        self.is_clicked = True
        self.n = random.randint(2, 5)
        self.circles = []
        for i in range(self.n):
            self.d = random.randint(1, 300)
            self.x = random.randint(1, 300)
            self.y = random.randint(1, 300)
            self.circles.append([self.d, self.x, self.y,
                              QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])
        self.d = random.randint(1, 300)
        self.x = random.randint(1, 300)
        self.y = random.randint(1, 300)
        self.update()


app = QApplication(sys.argv)
mainwindow = Circles()
mainwindow.show()
sys.exit(app.exec_())