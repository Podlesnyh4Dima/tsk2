import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 750, 750)
        self.setWindowTitle('Генерация флага')
        self.btn = QPushButton('Ввести количество цветов флага', self)
        self.btn.resize(75, 10)
        self.btn.move(45, 20)
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        x = randint(1, 250)
        y = randint(1, 250)
        a = randint(25, 300)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())

