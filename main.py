import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example")

        self.nameLabel = QLabel(self)
        self.resultLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.resultLabel.move(20, 100)
        self.resultLabel.resize(200, 32)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def clickMethod(self):
        item = self.line.text()
        self.resultLabel.setText(str(item))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())