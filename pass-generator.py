from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random

letters = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"y", 25:"z"}

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.GUI()

    def GUI(self):
        self.length_edit = QLineEdit(self)
        self.number_incluce_checkbox = QCheckBox(self)
        self.submit_btn = QPushButton('Generate', self)
        self.password = QLineEdit(self)
        self.programmer = QLabel('Made by Shayan Kermani', self)
        self.f1 = QFormLayout(self)

        self.password.setReadOnly(True)

        self.submit_btn.clicked.connect(self.generate)

        self.programmer.setAlignment(Qt.AlignCenter)

        self.f1.addRow('Lenght:', self.length_edit)
        self.f1.addRow('Include numbers:', self.number_incluce_checkbox)
        self.f1.addRow(self.submit_btn)
        self.f1.addRow('Yout generated password:', self.password)
        self.f1.addRow(self.programmer)

        self.setLayout(self.f1)
        self.setWindowIcon(QIcon('img/logo.png'))
        self.resize(500, 180)

    def generate(self):
        length = int(self.length_edit.text())
        password = ""

        for i in range(length):
            if self.number_incluce_checkbox.isChecked():
                rln = random.randint(0, 1) # 0: letter, 1: number
                if rln == 0:
                    rc = random.randint(0, 1) # 0: lowercase, 1: uppercase
                    rt = random.randint(1, 25) # letters
                    if rc == 0:
                        password += letters[rt]
                    elif rc == 1:
                        password += letters[rt].upper()
                elif rln == 1:
                    rt = random.randint(0, 9) # numbers
                    password += str(rt)
            elif not(self.number_incluce_checkbox.isChecked()):
                rc = random.randint(0, 1) # 0: lowercase, 1: uppercase
                rt = random.randint(1, 25) # letters
                if rc == 0:
                    password += letters[rt]
                elif rc == 1:
                    password += letters[rt].upper()

        self.password.setText(password)

if __name__ == "__main__":
    app = QApplication([])
    window = Ui()
    window.show()
    app.exec_()