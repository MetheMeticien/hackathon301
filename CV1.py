# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CV1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from nFrame1 import Ui_Dialog1
import source1_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 854)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 931))
        self.label.setStyleSheet("background-image: url(:/newPrefix/cvf.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Name = QtWidgets.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(20, 270, 231, 81))
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.Occupation = QtWidgets.QLabel(Dialog)
        self.Occupation.setGeometry(QtCore.QRect(60, 370, 151, 31))
        self.Occupation.setText("")
        self.Occupation.setObjectName("Occupation")
        self.Phonenumber = QtWidgets.QLabel(Dialog)
        self.Phonenumber.setGeometry(QtCore.QRect(100, 470, 141, 16))
        self.Phonenumber.setText("")
        self.Phonenumber.setObjectName("Phonenumber")
        self.Email = QtWidgets.QLabel(Dialog)
        self.Email.setGeometry(QtCore.QRect(100, 490, 141, 20))
        self.Email.setText("")
        self.Email.setObjectName("Email")
        self.Linkedin = QtWidgets.QLabel(Dialog)
        self.Linkedin.setGeometry(QtCore.QRect(100, 520, 141, 16))
        self.Linkedin.setText("")
        self.Linkedin.setObjectName("Linkedin")
        self.Address = QtWidgets.QLabel(Dialog)
        self.Address.setGeometry(QtCore.QRect(100, 540, 151, 51))
        self.Address.setText("")
        self.Address.setObjectName("Address")
        self.Profile = QtWidgets.QLabel(Dialog)
        self.Profile.setGeometry(QtCore.QRect(20, 630, 221, 151))
        self.Profile.setText("")
        self.Profile.setObjectName("Profile")
        self.Workexperience1 = QtWidgets.QLabel(Dialog)
        self.Workexperience1.setGeometry(QtCore.QRect(300, 110, 231, 141))
        self.Workexperience1.setText("")
        self.Workexperience1.setObjectName("Workexperience1")
        self.Workexperience2 = QtWidgets.QLabel(Dialog)
        self.Workexperience2.setGeometry(QtCore.QRect(300, 280, 231, 151))
        self.Workexperience2.setText("")
        self.Workexperience2.setObjectName("Workexperience2")
        self.Education1 = QtWidgets.QLabel(Dialog)
        self.Education1.setGeometry(QtCore.QRect(300, 490, 211, 91))
        self.Education1.setText("")
        self.Education1.setObjectName("Education1")
        self.Education2 = QtWidgets.QLabel(Dialog)
        self.Education2.setGeometry(QtCore.QRect(300, 600, 231, 91))
        self.Education2.setText("")
        self.Education2.setObjectName("Education2")
        self.Languages = QtWidgets.QLabel(Dialog)
        self.Languages.setGeometry(QtCore.QRect(290, 740, 241, 91))
        self.Languages.setText("")
        self.Languages.setObjectName("Languages")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    
    def secFrame(self):
        #connect 2nd frame
        f = open("Occupation.txt", 'r')
        with open('extractiontest.txt', 'r') as file:
            print(file.readline())
        f.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
