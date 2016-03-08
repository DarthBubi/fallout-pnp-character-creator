import sys
from PyQt5 import QtWidgets
import mainView


class CharacterCreator(QtWidgets.QMainWindow, mainView.Ui_MainWindow):

    def __init__(self, parent=None):
        super(CharacterCreator, self).__init__(parent)
        self.setupUi(self)
        self.quitAction.triggered.connect(self.quit)
        self.aboutAction.triggered.connect(self.about)
        self.openCharacterAction.triggered.connect(self.file_open)

    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

    def quit(self):
        choice = QtWidgets.QMessageBox.question(self, 'Quit Application', "Do you want to quit the application?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def about(self):
        QtWidgets.QMessageBox.about(self, 'About Character Creator',
                                    "This version 0.1.0 of the Fallout PnP Character Creator")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = CharacterCreator()
    form.show()
    sys.exit(app.exec_())

main()
