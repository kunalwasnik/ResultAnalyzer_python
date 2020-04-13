# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    dbname = 'results.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS sem4(
      "sid" INTEGER,
      "name"    TEXT,
      "coa" INTEGER,
      "aoa" INTEGER,
      "am"  INTEGER,
      "cg"  INTEGER,
      "os"  INTEGER

        )''')
    conn.close()

    def add_marks(self , MainWindow):
        dbname = 'results.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        name = self.student_name.toPlainText()
        sid = self.roll_no.toPlainText()
        coa = self.mcoa.toPlainText()
        aoa = self.maoa.toPlainText()
        am = self.mam4.toPlainText()
        cg = self.mcg.toPlainText()
        os = self.mos.toPlainText()

        if(name!= "" and sid != "" and coa!="" and aoa !="" and am!="" and cg!="" and os!="") :


            cur.execute('''
                    INSERT INTO  sem4(sid , name , aoa , coa , am , cg , os) VALUES( ?,?,?,?,?,?,?)

                ''' , (sid ,name ,  aoa , coa , am , cg , os))


            conn.commit()

            conn.close()
            self.message_label.setText("Marks Added")
            self.student_name.setText("")
            self.roll_no.setText("")
            self.mcoa.setText("")
            self.maoa.setText("")
            self.mam4.setText("")
            self.mos.setText("")
            self.mcg.setText("")
        else:
            self.message_label.setText("Fields Empty")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 511, 541))
        self.frame_2.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2b5876, stop:1 #4e4376);\n"
"font: 14pt \"Roboto\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 30, 151, 51))
        self.label.setStyleSheet("background:#474747;\n"
"\n"
"border-radius : 12px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 151, 51))
        self.label_2.setStyleSheet("background: #474747;\n"
"border-radius : 12px;")
        self.label_2.setObjectName("label_2")
        self.student_name = QtWidgets.QTextEdit(self.frame_2)
        self.student_name.setGeometry(QtCore.QRect(220, 30, 241, 51))
        self.student_name.setStyleSheet("border-radius: 12px;\n"
"border: 1px solid white;")
        self.student_name.setObjectName("student_name")
        self.roll_no = QtWidgets.QTextEdit(self.frame_2)
        self.roll_no.setGeometry(QtCore.QRect(220, 100, 241, 51))
        self.roll_no.setStyleSheet("border-radius: 12px;\n"
"border: 1px solid white;")
        self.roll_no.setObjectName("roll_no")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 200, 411, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 81, 41))
        self.label_7.setStyleSheet("background: #243b55;\n"
"border-radius : 12px;")
        self.label_7.setObjectName("label_7")
        self.mcoa = QtWidgets.QTextEdit(self.frame_3)
        self.mcoa.setGeometry(QtCore.QRect(180, 20, 101, 41))
        self.mcoa.setStyleSheet("")
        self.mcoa.setObjectName("mcoa")
        self.maoa = QtWidgets.QTextEdit(self.frame_3)
        self.maoa.setGeometry(QtCore.QRect(180, 80, 101, 41))
        self.maoa.setObjectName("maoa")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(30, 80, 81, 41))
        self.label_9.setStyleSheet("background: #243b55;\n"
"border-radius : 12px;")
        self.label_9.setObjectName("label_9")
        self.mam4 = QtWidgets.QTextEdit(self.frame_3)
        self.mam4.setGeometry(QtCore.QRect(180, 140, 101, 41))
        self.mam4.setObjectName("mam4")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(30, 140, 81, 41))
        self.label_10.setStyleSheet("background: #243b55;\n"
"border-radius : 12px;")
        self.label_10.setObjectName("label_10")
        self.mcg = QtWidgets.QTextEdit(self.frame_3)
        self.mcg.setGeometry(QtCore.QRect(180, 200, 101, 41))
        self.mcg.setObjectName("mcg")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(30, 200, 81, 41))
        self.label_11.setStyleSheet("background: #243b55;\n"
"border-radius : 12px;")
        self.label_11.setObjectName("label_11")
        self.mos = QtWidgets.QTextEdit(self.frame_3)
        self.mos.setGeometry(QtCore.QRect(180, 270, 101, 41))
        self.mos.setObjectName("mos")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(30, 270, 81, 41))
        self.label_12.setStyleSheet("background: #243b55;\n"
"border-radius : 12px;")
        self.label_12.setObjectName("label_12")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(30, 60, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(30, 120, 281, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(30, 180, 281, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_3)
        self.line_5.setGeometry(QtCore.QRect(20, 250, 281, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(510, 0, 211, 541))
        self.frame.setStyleSheet("background:#363636;\n"
"font: 14pt \"Roboto\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 161, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 121, 81))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 121, 61))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 101, 91))
        self.label_8.setStyleSheet("background:  url(:/images/images/admin.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.button_add = QtWidgets.QPushButton(self.frame)
        self.button_add.setGeometry(QtCore.QRect(10, 390, 191, 71))
        self.button_add.setObjectName("button_add")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 260, 131, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.message_label = QtWidgets.QLabel(self.frame)
        self.message_label.setGeometry(QtCore.QRect(20, 480, 171, 41))
        self.message_label.setText("")
        self.message_label.setObjectName("message_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Student Name "))
        self.label_2.setText(_translate("MainWindow", "   Roll no :"))
        self.label_7.setText(_translate("MainWindow", "  COA"))
        self.label_9.setText(_translate("MainWindow", "  AOA"))
        self.label_10.setText(_translate("MainWindow", " AM4"))
        self.label_11.setText(_translate("MainWindow", "   CG"))
        self.label_12.setText(_translate("MainWindow", "   OS"))
        self.label_3.setText(_translate("MainWindow", "ADMIN"))
        self.label_4.setText(_translate("MainWindow", "SEMESTER 4 "))
        self.label_5.setText(_translate("MainWindow", "Computer "))
        self.label_6.setText(_translate("MainWindow", "Engineering"))
        self.button_add.setText(_translate("MainWindow", "Add To Database"))
        self.button_add.clicked.connect(self.add_marks)



import images_rc




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
