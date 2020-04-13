# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

global sid
class Ui_student_login(object):
    def call_student(self ):
        sid = self.user_id.toPlainText()
        f = open("sid.txt", "w")
        f.write(sid)
        f.close()
        os.system("python student.py")




        #student_login.hide()

    def setupUi(self, student_login):
        student_login.setObjectName("student_login")
        student_login.resize(620, 336)
        self.centralwidget = QtWidgets.QWidget(student_login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-90, -10, 731, 461))
        self.frame.setStyleSheet("background: #185a9d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.user_id = QtWidgets.QTextEdit(self.frame)
        self.user_id.setGeometry(QtCore.QRect(520, 110, 131, 41))
        self.user_id.setObjectName("user_id")
        self.label_userid = QtWidgets.QLabel(self.frame)
        self.label_userid.setGeometry(QtCore.QRect(520, 60, 101, 51))
        self.label_userid.setStyleSheet("font-size : 24px;\n"
"color : white;")
        self.label_userid.setObjectName("label_userid")
        self.button_analyze = QtWidgets.QPushButton(self.frame)
        self.button_analyze.setGeometry(QtCore.QRect(520, 160, 131, 51))
        self.button_analyze.setStyleSheet("background: white;\n"
"color : black;")
        self.button_analyze.setObjectName("button_analyze")
        self.button_analyze.clicked.connect(self.call_student)


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 411, 331))
        self.label_2.setStyleSheet("background-image: url(:/images/images/29985.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        student_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(student_login)
        QtCore.QMetaObject.connectSlotsByName(student_login)

    def retranslateUi(self, student_login):
        _translate = QtCore.QCoreApplication.translate
        student_login.setWindowTitle(_translate("student_login", "MainWindow"))
        self.user_id.setHtml(_translate("student_login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_userid.setText(_translate("student_login", "USER ID"))
        self.button_analyze.setText(_translate("student_login", "ANALYZE"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_login = QtWidgets.QMainWindow()
    ui = Ui_student_login()
    ui.setupUi(student_login)
    student_login.show()
    sys.exit(app.exec_())
