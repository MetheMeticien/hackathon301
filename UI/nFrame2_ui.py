# Form implementation generated from reading ui file 'f:\1-2 semester\hackathonimproved\hackathonImprovised\UI\nFrame2.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1011, 50))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(49, 77, 168, 255));")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("STCaiyun")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 351, 61))
        font = QtGui.QFont()
        font.setFamily("STHupo")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Namebox = QtWidgets.QTextEdit(Dialog)
        self.Namebox.setGeometry(QtCore.QRect(250, 170, 341, 31))
        self.Namebox.setObjectName("Namebox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 481, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Descriptionbox = QtWidgets.QTextEdit(Dialog)
        self.Descriptionbox.setGeometry(QtCore.QRect(20, 310, 561, 81))
        self.Descriptionbox.setObjectName("Descriptionbox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 420, 100, 40))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">TalentMap</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#314da8;\">Enter Your Details</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">Enter Your Name:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">Enter Short Description About Yourself:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Next"))