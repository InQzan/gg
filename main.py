import os
import webbrowser
from dis import Ui_MainWindow
from PyQt6.QtWidgets import QApplication,QMainWindow, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.cal)
        self.ui.pushButton_2.clicked.connect(self.gdz)
        self.ui.pushButton_3.clicked.connect(self.youtube)
        self.ui.pushButton_4.clicked.connect(self.wg)
        self.ui.pushButton_5.clicked.connect(self.sh)


    def cal(self):
        os.startfile("C:/Windows/System32/calc.exe")
    def gdz(self):
        webbrowser.open("https://resheba.top/")
    def youtube(self):
        webbrowser.open("https://www.youtube.com/")
    def wg(self):
        webbrowser.open("https://store.steampowered.com/app/730/CounterStrike_2/?l=russian")
    def sh(self):
        os.system("shutdown -s -t 1")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
