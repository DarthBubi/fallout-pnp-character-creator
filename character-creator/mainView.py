# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\mainView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")
        self.saveCharacterAction = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/themes/oxygen/32x32/actions/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.saveCharacterAction.setIcon(icon)
        self.saveCharacterAction.setObjectName("saveCharacterAction")
        self.newCharacterAction = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/themes/oxygen/22x22/actions/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.newCharacterAction.setIcon(icon1)
        self.newCharacterAction.setObjectName("newCharacterAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.openCharacterAction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/themes/oxygen/32x32/actions/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openCharacterAction.setIcon(icon2)
        self.openCharacterAction.setObjectName("openCharacterAction")
        self.menuFile.addAction(self.quitAction)
        self.menuHelp.addAction(self.aboutAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.newCharacterAction)
        self.toolBar.addAction(self.saveCharacterAction)
        self.toolBar.addAction(self.openCharacterAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fallout PnP Character Creator"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.quitAction.setText(_translate("MainWindow", "Quit"))
        self.quitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.saveCharacterAction.setText(_translate("MainWindow", "Save"))
        self.saveCharacterAction.setToolTip(_translate("MainWindow", "Save Character"))
        self.saveCharacterAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.newCharacterAction.setText(_translate("MainWindow", "New"))
        self.newCharacterAction.setToolTip(_translate("MainWindow", "New Character"))
        self.newCharacterAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.aboutAction.setText(_translate("MainWindow", "About"))
        self.openCharacterAction.setText(_translate("MainWindow", "openCharacter"))
        self.openCharacterAction.setToolTip(_translate("MainWindow", "Open"))
        self.openCharacterAction.setShortcut(_translate("MainWindow", "Ctrl+O"))

import oxygen_rc
