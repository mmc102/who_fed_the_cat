
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton,QVBoxLayout, QWidget, QMessageBox, QDateTimeEdit
from PyQt5.QtCore import QTimer
import datetime




app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
header = QLabel('cat')

layout.addWidget(header)
button = QPushButton('i fed')
layout.addWidget(button)
other_button = QPushButton('i didnt')
layout.addWidget(other_button)
window.setLayout(layout)
window.show()


cat_fed = False


def on_feed_button_clicked():
    alert = QMessageBox()
    alert.setText('You Fed That Cat! Thanks for your service!')
    cat_fed = True
    alert.exec_()
def on_other_button_clicked():
    alert = QMessageBox()
    alert.setText('Why didnt you feed the cat?!?!')
    alert.exec_()



button.clicked.connect(on_feed_button_clicked)
other_button.clicked.connect(on_other_button_clicked)
app.exec_()
