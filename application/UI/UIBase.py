# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aquaUI_Base.ui'
#
# Created: Tue Nov 24 13:36:30 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameVideo = QtGui.QFrame(self.centralwidget)
        self.frameVideo.setGeometry(QtCore.QRect(200, 50, 531, 361))
        self.frameVideo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameVideo.setFrameShadow(QtGui.QFrame.Raised)
        self.frameVideo.setObjectName(_fromUtf8("frameVideo"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 430, 731, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.labelControls = QtGui.QLabel(self.centralwidget)
        self.labelControls.setGeometry(QtCore.QRect(10, 450, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelControls.setFont(font)
        self.labelControls.setObjectName(_fromUtf8("labelControls"))
        self.labelPropellers = QtGui.QLabel(self.centralwidget)
        self.labelPropellers.setGeometry(QtCore.QRect(20, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelPropellers.setFont(font)
        self.labelPropellers.setObjectName(_fromUtf8("labelPropellers"))
        self.labelStatus = QtGui.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(20, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelStatus.setFont(font)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.labelProp1 = QtGui.QLabel(self.centralwidget)
        self.labelProp1.setGeometry(QtCore.QRect(20, 110, 56, 13))
        self.labelProp1.setObjectName(_fromUtf8("labelProp1"))
        self.labelProp2 = QtGui.QLabel(self.centralwidget)
        self.labelProp2.setGeometry(QtCore.QRect(20, 150, 56, 13))
        self.labelProp2.setObjectName(_fromUtf8("labelProp2"))
        self.labelProp3 = QtGui.QLabel(self.centralwidget)
        self.labelProp3.setGeometry(QtCore.QRect(20, 190, 56, 13))
        self.labelProp3.setObjectName(_fromUtf8("labelProp3"))
        self.labelProp4 = QtGui.QLabel(self.centralwidget)
        self.labelProp4.setGeometry(QtCore.QRect(20, 230, 56, 13))
        self.labelProp4.setObjectName(_fromUtf8("labelProp4"))
        self.boxProp1 = QtGui.QLineEdit(self.centralwidget)
        self.boxProp1.setGeometry(QtCore.QRect(92, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxProp1.setFont(font)
        self.boxProp1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxProp1.setReadOnly(True)
        self.boxProp1.setObjectName(_fromUtf8("boxProp1"))
        self.boxProp2 = QtGui.QLineEdit(self.centralwidget)
        self.boxProp2.setGeometry(QtCore.QRect(92, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxProp2.setFont(font)
        self.boxProp2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxProp2.setReadOnly(True)
        self.boxProp2.setObjectName(_fromUtf8("boxProp2"))
        self.boxProp3 = QtGui.QLineEdit(self.centralwidget)
        self.boxProp3.setGeometry(QtCore.QRect(92, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxProp3.setFont(font)
        self.boxProp3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxProp3.setReadOnly(True)
        self.boxProp3.setObjectName(_fromUtf8("boxProp3"))
        self.boxProp4 = QtGui.QLineEdit(self.centralwidget)
        self.boxProp4.setGeometry(QtCore.QRect(92, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxProp4.setFont(font)
        self.boxProp4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxProp4.setReadOnly(True)
        self.boxProp4.setObjectName(_fromUtf8("boxProp4"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 50, 181, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 250, 181, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.labelEnvironmental = QtGui.QLabel(self.centralwidget)
        self.labelEnvironmental.setGeometry(QtCore.QRect(20, 270, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEnvironmental.setFont(font)
        self.labelEnvironmental.setObjectName(_fromUtf8("labelEnvironmental"))
        self.boxDepth = QtGui.QLineEdit(self.centralwidget)
        self.boxDepth.setGeometry(QtCore.QRect(92, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxDepth.setFont(font)
        self.boxDepth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxDepth.setReadOnly(True)
        self.boxDepth.setObjectName(_fromUtf8("boxDepth"))
        self.labelDepth = QtGui.QLabel(self.centralwidget)
        self.labelDepth.setGeometry(QtCore.QRect(20, 310, 56, 13))
        self.labelDepth.setObjectName(_fromUtf8("labelDepth"))
        self.boxTemp = QtGui.QLineEdit(self.centralwidget)
        self.boxTemp.setGeometry(QtCore.QRect(92, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxTemp.setFont(font)
        self.boxTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxTemp.setReadOnly(True)
        self.boxTemp.setObjectName(_fromUtf8("boxTemp"))
        self.labelTemp = QtGui.QLabel(self.centralwidget)
        self.labelTemp.setGeometry(QtCore.QRect(20, 350, 56, 13))
        self.labelTemp.setObjectName(_fromUtf8("labelTemp"))
        self.boxPressure = QtGui.QLineEdit(self.centralwidget)
        self.boxPressure.setGeometry(QtCore.QRect(92, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boxPressure.setFont(font)
        self.boxPressure.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.boxPressure.setReadOnly(True)
        self.boxPressure.setObjectName(_fromUtf8("boxPressure"))
        self.labeLPressure = QtGui.QLabel(self.centralwidget)
        self.labeLPressure.setGeometry(QtCore.QRect(20, 390, 56, 13))
        self.labeLPressure.setObjectName(_fromUtf8("labeLPressure"))
        self.labelMovement = QtGui.QLabel(self.centralwidget)
        self.labelMovement.setGeometry(QtCore.QRect(360, 470, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelMovement.setFont(font)
        self.labelMovement.setObjectName(_fromUtf8("labelMovement"))
        self.labelTrim = QtGui.QLabel(self.centralwidget)
        self.labelTrim.setGeometry(QtCore.QRect(30, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelTrim.setFont(font)
        self.labelTrim.setObjectName(_fromUtf8("labelTrim"))
        self.sliderMovementZRotation = QtGui.QSlider(self.centralwidget)
        self.sliderMovementZRotation.setGeometry(QtCore.QRect(370, 540, 160, 22))
        self.sliderMovementZRotation.setMinimum(-100)
        self.sliderMovementZRotation.setMaximum(100)
        self.sliderMovementZRotation.setProperty("value", 0)
        self.sliderMovementZRotation.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMovementZRotation.setObjectName(_fromUtf8("sliderMovementZRotation"))
        self.sliderMovementForward = QtGui.QSlider(self.centralwidget)
        self.sliderMovementForward.setGeometry(QtCore.QRect(590, 490, 22, 160))
        self.sliderMovementForward.setMinimum(-100)
        self.sliderMovementForward.setMaximum(100)
        self.sliderMovementForward.setProperty("value", 0)
        self.sliderMovementForward.setOrientation(QtCore.Qt.Vertical)
        self.sliderMovementForward.setObjectName(_fromUtf8("sliderMovementForward"))
        self.sliderMovementVertical = QtGui.QSlider(self.centralwidget)
        self.sliderMovementVertical.setGeometry(QtCore.QRect(710, 490, 22, 160))
        self.sliderMovementVertical.setMinimum(-100)
        self.sliderMovementVertical.setMaximum(100)
        self.sliderMovementVertical.setProperty("value", 0)
        self.sliderMovementVertical.setOrientation(QtCore.Qt.Vertical)
        self.sliderMovementVertical.setObjectName(_fromUtf8("sliderMovementVertical"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(340, 460, 20, 201))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.sliderTrimHorizontal = QtGui.QSlider(self.centralwidget)
        self.sliderTrimHorizontal.setGeometry(QtCore.QRect(140, 550, 101, 22))
        self.sliderTrimHorizontal.setMinimum(-100)
        self.sliderTrimHorizontal.setMaximum(100)
        self.sliderTrimHorizontal.setProperty("value", 0)
        self.sliderTrimHorizontal.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTrimHorizontal.setObjectName(_fromUtf8("sliderTrimHorizontal"))
        self.sliderTrimVertical = QtGui.QSlider(self.centralwidget)
        self.sliderTrimVertical.setGeometry(QtCore.QRect(60, 550, 22, 91))
        self.sliderTrimVertical.setMinimum(-100)
        self.sliderTrimVertical.setMaximum(100)
        self.sliderTrimVertical.setProperty("value", 0)
        self.sliderTrimVertical.setOrientation(QtCore.Qt.Vertical)
        self.sliderTrimVertical.setObjectName(_fromUtf8("sliderTrimVertical"))
        self.labelTrimHorizontal = QtGui.QLabel(self.centralwidget)
        self.labelTrimHorizontal.setGeometry(QtCore.QRect(140, 530, 111, 16))
        self.labelTrimHorizontal.setObjectName(_fromUtf8("labelTrimHorizontal"))
        self.labelTrimVertical = QtGui.QLabel(self.centralwidget)
        self.labelTrimVertical.setGeometry(QtCore.QRect(30, 530, 111, 16))
        self.labelTrimVertical.setObjectName(_fromUtf8("labelTrimVertical"))
        self.labelMovementHorizontalRotation = QtGui.QLabel(self.centralwidget)
        self.labelMovementHorizontalRotation.setGeometry(QtCore.QRect(370, 510, 121, 16))
        self.labelMovementHorizontalRotation.setObjectName(_fromUtf8("labelMovementHorizontalRotation"))
        self.labelMovementForward = QtGui.QLabel(self.centralwidget)
        self.labelMovementForward.setGeometry(QtCore.QRect(540, 470, 121, 16))
        self.labelMovementForward.setObjectName(_fromUtf8("labelMovementForward"))
        self.labelMovementVerticalRotation = QtGui.QLabel(self.centralwidget)
        self.labelMovementVerticalRotation.setGeometry(QtCore.QRect(690, 470, 51, 16))
        self.labelMovementVerticalRotation.setObjectName(_fromUtf8("labelMovementVerticalRotation"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Aquatic Inspector Application", None))
        self.labelControls.setText(_translate("MainWindow", "Controls:", None))
        self.labelPropellers.setText(_translate("MainWindow", "Propellers:", None))
        self.labelStatus.setText(_translate("MainWindow", "Status:", None))
        self.labelProp1.setText(_translate("MainWindow", "Prop 1:", None))
        self.labelProp2.setText(_translate("MainWindow", "Prop 2:", None))
        self.labelProp3.setText(_translate("MainWindow", "Prop 3:", None))
        self.labelProp4.setText(_translate("MainWindow", "Prop 4:", None))
        self.boxProp1.setText(_translate("MainWindow", "0.0", None))
        self.boxProp2.setText(_translate("MainWindow", "0.0", None))
        self.boxProp3.setText(_translate("MainWindow", "0.0", None))
        self.boxProp4.setText(_translate("MainWindow", "0.0", None))
        self.labelEnvironmental.setText(_translate("MainWindow", "Environmental:", None))
        self.boxDepth.setText(_translate("MainWindow", "0.0", None))
        self.labelDepth.setText(_translate("MainWindow", "Depth:", None))
        self.boxTemp.setText(_translate("MainWindow", "0.0", None))
        self.labelTemp.setText(_translate("MainWindow", "Temp:", None))
        self.boxPressure.setText(_translate("MainWindow", "0.0", None))
        self.labeLPressure.setText(_translate("MainWindow", "Pressure:", None))
        self.labelMovement.setText(_translate("MainWindow", "Movement:", None))
        self.labelTrim.setText(_translate("MainWindow", "Trim:", None))
        self.labelTrimHorizontal.setText(_translate("MainWindow", "Horizontal Trim:", None))
        self.labelTrimVertical.setText(_translate("MainWindow", "Vertical Trim:", None))
        self.labelMovementHorizontalRotation.setText(_translate("MainWindow", "Horizontal Rotation:", None))
        self.labelMovementForward.setText(_translate("MainWindow", "Forward/Backward:", None))
        self.labelMovementVerticalRotation.setText(_translate("MainWindow", "Vertical:", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
