from PyQt5 import QtWidgets
import sys
if __name__ == '__main__':
    from UI_Base import *
else:
    from UI.UI_Base import *  # импорт нашего сгенерированного файла
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
