# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
from admin import Ui_MainWindow
from student_login import Ui_student_login


class Ui_Dialog(object):

    def call_admin(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()

        #os.system('python admin.py')

    def call_student(self):
        #os.system('python student_login.py')
        self.window =  QtWidgets.QMainWindow()
        self.ui =Ui_student_login()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 451)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.admin_button = QtWidgets.QPushButton(Dialog)
        self.admin_button.setGeometry(QtCore.QRect(40, 150, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Colus")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.admin_button.setFont(font)
        self.admin_button.setAutoFillBackground(False)
        self.admin_button.setStyleSheet("background: #eb3349;\n"
"font: 18pt \"Colus\";\n"
"color : white;")
        self.admin_button.setFlat(True)
        self.admin_button.setObjectName("admin_button")
        self.admin_button.clicked.connect(self.call_admin)




        self.student_button = QtWidgets.QPushButton(Dialog)
        self.student_button.setGeometry(QtCore.QRect(510, 350, 171, 71))
        self.student_button.setAutoFillBackground(False)
        self.student_button.setStyleSheet("background: #111111;\n"
"font: 18pt \"Colus\";\n"
"color : #E0170D,;")
        self.student_button.clicked.connect(self.call_student)
        self.student_button.setAutoDefault(True)
        self.student_button.setDefault(False)
        self.student_button.setFlat(True)
        self.student_button.setObjectName("student_button")
        self.topic = QtWidgets.QLabel(Dialog)
        self.topic.setGeometry(QtCore.QRect(170, 180, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Colus")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.topic.setFont(font)
        self.topic.setStyleSheet("font: 22pt \"Colus\";\n"
"color : white;\n"
"")
        self.topic.setObjectName("topic")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 741, 451))
        self.label_2.setStyleSheet("\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:99.2, stop:0.498783 #E0170D, stop:0.497561 #141414);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.admin_label = QtWidgets.QLabel(Dialog)
        self.admin_label.setGeometry(QtCore.QRect(40, 150, 171, 71))
        self.admin_label.setStyleSheet("background: #E0170D;\n"
"border: 1px solid white;\n"
"")
        self.admin_label.setText("")
        self.admin_label.setObjectName("admin_label")
        self.student_label = QtWidgets.QLabel(Dialog)
        self.student_label.setGeometry(QtCore.QRect(510, 350, 171, 71))
        self.student_label.setStyleSheet("background : #141414;\n"
"border: 1px solid white;")
        self.student_label.setText("")
        self.student_label.setObjectName("student_label")
        self.admin_icon = QtWidgets.QLabel(Dialog)
        self.admin_icon.setGeometry(QtCore.QRect(80, 30, 111, 111))
        self.admin_icon.setStyleSheet("background : url(:/images/images/admin.png) no-repeat;")
        self.admin_icon.setText("")
        self.admin_icon.setObjectName("admin_icon")
        self.student_icon = QtWidgets.QLabel(Dialog)
        self.student_icon.setGeometry(QtCore.QRect(550, 250, 91, 81))
        self.student_icon.setStyleSheet("background : url(:/images/images/student.png) no-repeat;")
        self.student_icon.setText("")
        self.student_icon.setObjectName("student_icon")
        self.label_2.raise_()
        self.admin_label.raise_()
        self.student_label.raise_()
        self.student_button.raise_()
        self.admin_button.raise_()
        self.topic.raise_()
        self.admin_icon.raise_()
        self.student_icon.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.admin_button.setText(_translate("Dialog", "Admin"))
        self.student_button.setText(_translate("Dialog", "Student"))
        self.topic.setText(_translate("Dialog", "           Result Analyzer"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
