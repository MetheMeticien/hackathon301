# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nFrame3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(600, 350)
        Dialog3.setWindowOpacity(1.0)
        Dialog3.setAutoFillBackground(False)
        self.widget = QtWidgets.QWidget(Dialog3)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 77, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 77, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 77, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 77, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("STCaiyun")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(Dialog3)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 600, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_2.setPalette(palette)
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 591, 51))
        self.label_2.setStyleSheet("font: 8pt \"STHupo\";")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.pushbutton3 = QtWidgets.QPushButton(self.widget_2)
        self.pushbutton3.setGeometry(QtCore.QRect(250, 250, 100, 40))
        self.pushbutton3.setObjectName("pushbutton3")
        self.desbox2 = QtWidgets.QLineEdit(self.widget_2)
        self.desbox2.setGeometry(QtCore.QRect(190, 190, 401, 51))
        self.desbox2.setObjectName("desbox2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 161, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 161, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 221, 31))
        self.label_5.setObjectName("label_5")
        self.degreebox = QtWidgets.QTextEdit(self.widget_2)
        self.degreebox.setGeometry(QtCore.QRect(190, 70, 300, 31))
        self.degreebox.setObjectName("degreebox")
        self.unibox = QtWidgets.QTextBrowser(self.widget_2)
        self.unibox.setGeometry(QtCore.QRect(190, 110, 300, 30))
        self.unibox.setObjectName("unibox")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 161, 31))
        self.label_6.setObjectName("label_6")
        self.gradbox = QtWidgets.QDateEdit(self.widget_2)
        self.gradbox.setGeometry(QtCore.QRect(270, 150, 141, 31))
        self.gradbox.setObjectName("gradbox")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "TalentMap"))
        self.label.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ffffff;\">TalentMap</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:22pt; color:#314da8;\">Enter Educational Qualification</span></p></body></html>"))
        self.pushbutton3.setText(_translate("Dialog3", "Next"))
        self.label_3.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">Description :</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">Degree :</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">Graduation Date :</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog3", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#314da8;\">University  :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())