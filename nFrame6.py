# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nFrame6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog6")
        Dialog6.resize(1000, 600)
        Dialog6.setWindowOpacity(1.0)
        Dialog6.setAutoFillBackground(False)
        self.widget = QtWidgets.QWidget(Dialog6)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1000, 50))
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
        self.widget_2 = QtWidgets.QWidget(Dialog6)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 1000, 550))
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
        self.label_2.setGeometry(QtCore.QRect(20, -10, 391, 101))
        self.label_2.setStyleSheet("font: 8pt \"STHupo\";")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.pushButton6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton6.setGeometry(QtCore.QRect(430, 480, 100, 40))
        self.pushButton6.setObjectName("pushButton6")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 291, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 161, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 171, 31))
        self.label_5.setObjectName("label_5")
        self.Phonebox6 = QtWidgets.QTextEdit(self.widget_2)
        self.Phonebox6.setGeometry(QtCore.QRect(340, 70, 300, 41))
        self.Phonebox6.setObjectName("Phonebox6")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 301, 91))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(30, 370, 231, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(30, 420, 221, 31))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setGeometry(QtCore.QRect(340, 120, 311, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 170, 531, 87))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 270, 531, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 370, 531, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_5.setGeometry(QtCore.QRect(340, 420, 531, 51))
        self.textEdit_5.setObjectName("textEdit_5")

        self.retranslateUi(Dialog6)
        QtCore.QMetaObject.connectSlotsByName(Dialog6)
        self.pushButton6.clicked.connect(self.seventhFrame)

    def seventhFrame(self):
        # connect 2nd frame

        f = open("Phonenum.txt", 'w')
        f.write(self.Phonebox6.toPlainText())
        f.close()
        f = open("email.txt", 'w')
        f.write(self.textEdit.toPlainText())
        f.close()
        f = open("PresentAdd.txt", 'w')
        f.write(self.textEdit_2.toPlainText())
        f.close()
        f = open("PermaAdd.txt", 'w')
        f.write(self.textEdit_3.toPlainText())
        f.close()
        f = open("Instagram.txt", 'w')
        f.write(self.textEdit_4.toPlainText())
        f.close()
        f = open("facebook.txt", 'w')
        f.write(self.textEdit_5.toPlainText())
        f.close()

    def retranslateUi(self, Dialog6):
        _translate = QtCore.QCoreApplication.translate
        Dialog6.setWindowTitle(_translate("Dialog6", "TalentMap"))
        self.label.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ffffff;\">TalentMap</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#314da8;\">Communication</span></p></body></html>"))
        self.pushButton6.setText(_translate("Dialog6", "Next"))
        self.label_3.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Address(Present) :</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Phone no :</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Email :</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Address</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">(Permanent) :</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Instagram ID :</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog6", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#314da8;\">Facebook ID:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog6 = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog6)
    Dialog6.show()
    sys.exit(app.exec_())
