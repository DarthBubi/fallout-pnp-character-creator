import sys
from PyQt5 import QtWidgets, QtCore
import mainView


class CharacterCreator(QtWidgets.QMainWindow, mainView.Ui_MainWindow):

    def __init__(self, parent=None):
        super(CharacterCreator, self).__init__(parent)
        self.setupUi(self)
        self.quit()

    def quit(self):
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = CharacterCreator()
    form.show()
    sys.exit(app.exec_())

main()
