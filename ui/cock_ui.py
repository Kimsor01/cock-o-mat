# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qrainbowstyle import load_stylesheet


class Ui_cockomat(object):
    def setupUi(self, cockomat):
        cockomat.setObjectName("cockomat")
        cockomat.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        cockomat.setEnabled(True)
        cockomat.resize(800, 480)
        cockomat.setMaximumSize(QtCore.QSize(800, 480))
        cockomat.setBaseSize(QtCore.QSize(800, 480))
        cockomat.setUpdatesEnabled(True)
        # font set up
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        cockomat.setFont(font)
        cockomat.setStyleSheet(load_stylesheet(style="QDarkStyle"))
        cockomat.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(cockomat)
        self.centralwidget.setObjectName("centralwidget")
        self.listDrinkSelection = QtWidgets.QListWidget(self.centralwidget)
        self.listDrinkSelection.setGeometry(QtCore.QRect(10, 67, 320, 381))
        self.listDrinkSelection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listDrinkSelection.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listDrinkSelection.setLineWidth(1)
        self.listDrinkSelection.setMidLineWidth(0)
        self.listDrinkSelection.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listDrinkSelection.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listDrinkSelection.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listDrinkSelection.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listDrinkSelection.setProperty("showDropIndicator", False)
        self.listDrinkSelection.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listDrinkSelection.setAlternatingRowColors(True)
        self.listDrinkSelection.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listDrinkSelection.setObjectName("listDrinkSelection")
        self.listDrinkDetails = QtWidgets.QListWidget(self.centralwidget)
        self.listDrinkDetails.setGeometry(QtCore.QRect(470, 120, 320, 160))
        self.listDrinkDetails.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listDrinkDetails.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listDrinkDetails.setAlternatingRowColors(True)
        self.listDrinkDetails.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listDrinkDetails.setObjectName("listDrinkDetails")
        self.pbOptions = QtWidgets.QPushButton(self.centralwidget)
        self.pbOptions.setGeometry(QtCore.QRect(760, 10, 30, 30))
        self.pbOptions.setObjectName("pbOptions")
        self.pbPourDrink = QtWidgets.QPushButton(self.centralwidget)
        self.pbPourDrink.setGeometry(QtCore.QRect(660, 420, 121, 31))
        self.pbPourDrink.setObjectName("pbPourDrink")
        self.cmbTypes = QtWidgets.QComboBox(self.centralwidget)
        self.cmbTypes.setGeometry(QtCore.QRect(90, 10, 34, 25))
        self.cmbTypes.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cmbTypes.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbTypes.setDuplicatesEnabled(False)
        self.cmbTypes.setObjectName("cmbTypes")
        self.cmbTypes.addItem("-")
        self.pbFart = QtWidgets.QPushButton(self.centralwidget)
        self.pbFart.setGeometry(QtCore.QRect(350, 130, 80, 25))
        self.pbFart.setObjectName("pbFart")
        self.pbRandom = QtWidgets.QPushButton(self.centralwidget)
        self.pbRandom.setGeometry(QtCore.QRect(350, 90, 77, 25))
        self.pbRandom.setCheckable(True)
        self.pbRandom.setObjectName("pbRandom")
        self.pbShowAll = QtWidgets.QPushButton(self.centralwidget)
        self.pbShowAll.setGeometry(QtCore.QRect(10, 10, 77, 25))
        self.pbShowAll.setTabletTracking(False)
        self.pbShowAll.setCheckable(False)
        self.pbShowAll.setChecked(False)
        self.pbShowAll.setObjectName("pbShowAll")
        self.labelDrink = QtWidgets.QLabel(self.centralwidget)
        self.labelDrink.setGeometry(QtCore.QRect(470, 67, 311, 31))
        self.labelDrink.setFont(font)
        self.labelDrink.setFixedWidth(320)
        self.labelDrink.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.labelDrink.setAlignment(QtCore.Qt.AlignHCenter)
        self.labelDrink.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.labelDrink.setObjectName("labelDrink")
        self.cbAua = QtWidgets.QCheckBox(self.centralwidget)
        self.cbAua.setGeometry(QtCore.QRect(470, 420, 181, 31))
        self.cbAua.setObjectName("cbAua")
        self.ldBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ldBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.ldBar.setMinimum(0)
        self.ldBar.setMaximum(400)
        self.ldBar.setObjectName("ldBar")
        self.ldBar.setFixedSize(600, 80)
        self.ldBar.move(100, 200)
        self.ldBar.hide()

        # changing the styles a bit

        self.listDrinkSelection.setFont(font)
        self.listDrinkDetails.setFont(font)
        self.pbShowAll.setFont(font)
        self.cmbTypes.setFont(font)
        self.pbFart.setFont(font)
        self.pbRandom.setFont(font)
        self.pbPourDrink.setFont(font)
        self.pbOptions.setFont(font)
        self.cbAua.setFont(font)
        self.ldBar.setFont(font)

        self.retranslateUi(cockomat)
        QtCore.QMetaObject.connectSlotsByName(cockomat)

    def retranslateUi(self, cockomat):
        _translate = QtCore.QCoreApplication.translate
        cockomat.setWindowTitle(_translate("cockomat", "Cock-o-mat"))
        self.listDrinkSelection.setSortingEnabled(True)
        # self.listDrinkDetails.setSortingEnabled(True)
        self.pbOptions.setText(_translate("cockomat", "x"))
        self.pbPourDrink.setText(_translate("cockomat", "Go to Work"))
        self.cmbTypes.setItemText(0, _translate("cockomat", "-"))
        self.pbFart.setText(_translate("cockomat", "Fart"))
        self.pbRandom.setText(_translate("cockomat", "Zufall"))
        self.pbShowAll.setText(_translate("cockomat", "Alle"))
        self.labelDrink.setText(_translate("cockomat", "💀"))
        self.cbAua.setText(_translate("cockomat", "💀Double Trouble💀"))
        # self.ldBar.setText(_translate("cockomat", "Ich zeig dir wie weit dein Drink ist 🍹"))
