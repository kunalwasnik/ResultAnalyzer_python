# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

class Ui_student(object):
    global sid
    file = open("sid.txt", "r")
    sid =  file.read()


    def setupUi(self, student):
        student.setObjectName("student")
        student.resize(692, 490)
        self.centralwidget = QtWidgets.QWidget(student)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 201, 491))
        self.frame.setStyleSheet("background: #222629;\n"
"font: 18pt \"Roboto\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 240, 101, 91))
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.roll_no = QtWidgets.QLabel(self.frame)
        self.roll_no.setGeometry(QtCore.QRect(50, 170, 131, 81))
        self.roll_no.setStyleSheet("")
        self.roll_no.setObjectName("roll_no")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 101, 101))
        self.label_2.setStyleSheet("background: url(:/images/images/04.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 310, 121, 81))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 370, 131, 61))
        self.label_8.setObjectName("label_8")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(30, 310, 141, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 0, 511, 491))
        self.frame_2.setStyleSheet("background : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #474866, stop:1 #474866);\n"
"font: 19pt \"Roboto\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_coa = QtWidgets.QLabel(self.frame_2)
        self.label_coa.setGeometry(QtCore.QRect(40, 90, 91, 31))
        self.label_coa.setObjectName("label_coa")
        self.label_aoa = QtWidgets.QLabel(self.frame_2)
        self.label_aoa.setGeometry(QtCore.QRect(40, 150, 56, 31))
        self.label_aoa.setObjectName("label_aoa")
        self.label_am4 = QtWidgets.QLabel(self.frame_2)
        self.label_am4.setGeometry(QtCore.QRect(40, 210, 56, 31))
        self.label_am4.setObjectName("label_am4")
        self.label_cg = QtWidgets.QLabel(self.frame_2)
        self.label_cg.setGeometry(QtCore.QRect(40, 270, 61, 31))
        self.label_cg.setStyleSheet("")
        self.label_cg.setObjectName("label_cg")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 56, 21))
        self.label_6.setObjectName("label_6")
        self.mess_coa = QtWidgets.QProgressBar(self.frame_2)
        self.mess_coa.setGeometry(QtCore.QRect(140, 90, 201, 41))
        self.mess_coa.setProperty("value", 42)
        self.mess_coa.setObjectName("mess_coa")
        self.mess_aoa = QtWidgets.QProgressBar(self.frame_2)
        self.mess_aoa.setGeometry(QtCore.QRect(140, 140, 201, 41))
        self.mess_aoa.setProperty("value", 24)
        self.mess_aoa.setObjectName("mess_aoa")
        self.mess_am4 = QtWidgets.QProgressBar(self.frame_2)
        self.mess_am4.setGeometry(QtCore.QRect(140, 200, 201, 41))
        self.mess_am4.setProperty("value", 24)
        self.mess_am4.setObjectName("mess_am4")
        self.mess_cg = QtWidgets.QProgressBar(self.frame_2)
        self.mess_cg.setGeometry(QtCore.QRect(140, 260, 201, 41))
        self.mess_cg.setProperty("value", 24)
        self.mess_cg.setObjectName("mess_cg")
        self.mess_os = QtWidgets.QProgressBar(self.frame_2)
        self.mess_os.setGeometry(QtCore.QRect(140, 330, 201, 41))
        self.mess_os.setProperty("value", 24)
        self.mess_os.setObjectName("mess_os")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 0, 151, 71))
        self.label.setObjectName("label")
        self.mess_total = QtWidgets.QLabel(self.frame_2)
        self.mess_total.setGeometry(QtCore.QRect(210, 10, 141, 51))
        self.mess_total.setObjectName("mess_total")
        self.button_analyse = QtWidgets.QPushButton(self.frame_2)
        self.button_analyse.setGeometry(QtCore.QRect(170, 400, 121, 51))
        self.button_analyse.setObjectName("button_analyse")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(40, 130, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(40, 180, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(40, 240, 281, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(40, 310, 281, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        student.setCentralWidget(self.centralwidget)

        self.retranslateUi(student)
        QtCore.QMetaObject.connectSlotsByName(student)

        # database
        dbname = 'results.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        print(sid)
        rolltext = "Roll no " + sid
        self.roll_no.setText(rolltext)
        rollno = sid
        a=cur.execute('SELECT * FROM sem4 WHERE sid=(?)',(rollno,))


        rows = cur.fetchall()
                #print(rows)
            #name = (rows[0][1])
        global coa , aoa , am , cg , os , total
        global tcoa , taoa , tam , tcg , tos
        coa = int(rows[0][2])
        aoa = int(rows[0][3])
        am = int(rows[0][4])
        cg = int(rows[0][5])
        os =int (rows[0][6])
        total = (coa + aoa + am + cg + os)
            #self.mess_os.delete(1.0,"end-1c")

        self.mess_coa.setProperty("value", coa)
        self.mess_coa.setFormat("%v")
        self.mess_aoa.setProperty("value", aoa)
        self.mess_aoa.setFormat("%v")
        self.mess_am4.setProperty("value", am)
        self.mess_am4.setFormat("%v")
        self.mess_cg.setProperty("value", cg)
        self.mess_cg.setFormat("%v")
        self.mess_os.setProperty("value", os)
        self.mess_os.setFormat("%v")

        self.mess_total.setText(str(total))

        conn.close()
        self.button_analyse.clicked.connect(self.plot_compare)
        #self.roll_no.setText(sid)

    def plot_compare(self):
        dbname = 'results.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        rollno = 1
        a=cur.execute('SELECT * FROM sem4 ')

        avg_coa = 0
        avg_aoa = 0
        avg_am = 0
        avg_cg = 0
        avg_os = 0
        rows = cur.fetchall()
        count = 0
        for r in rows:
            avg_coa = avg_coa + int(r[2])
            avg_aoa = avg_aoa + int(r[3])
            avg_am = avg_am + int(r[4])
            avg_cg = avg_cg + int(r[5])
            avg_os = avg_os + int(r[6])
            count = count+1

        avg_coa =int( avg_coa /count)
        avg_aoa = int(avg_coa /count)
        avg_am = int(avg_coa /count)
        avg_cg = int(avg_coa /count)
        avg_os =int( avg_coa /count)



        #Subject Topper
        a=cur.execute('SELECT MAX(coa) FROM sem4')
        rows = cur.fetchall()
        tcoa = int(rows[0][0])

        a=cur.execute('SELECT MAX(aoa) FROM sem4')
        rows = cur.fetchall()
        taoa = int(rows[0][0])

        a=cur.execute('SELECT MAX(os) FROM sem4')
        rows = cur.fetchall()
        tos = int(rows[0][0])

        a=cur.execute('SELECT MAX(am) FROM sem4')
        rows = cur.fetchall()
        tam = int(rows[0][0])

        a=cur.execute('SELECT MAX(cg) FROM sem4')
        rows = cur.fetchall()
        tcg = int(rows[0][0])


        import numpy as np
        import matplotlib.pyplot as plt

        # data to plot

        n_groups = 5
        means_class = (avg_coa, avg_aoa, avg_am , avg_cg ,avg_os)
        means_your = (coa, aoa, am, cg,os)
        means_topper = (tcoa , taoa , tam , tcg , tos)
        print(coa)
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.25
        opacity = 0.8

        rects1 = plt.bar(index, means_class , bar_width,
        alpha=opacity,
        color='b',
        label='Class Average')

        rects2 = plt.bar(index + bar_width,means_your , bar_width,
        alpha=opacity,
        color='g',
        label='Your Score')

        rects3 = plt.bar(index +2* bar_width,means_topper , bar_width,
        alpha=opacity,
        color='r',
        label='Subject Topper')

        def autolabel(rects):


            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)

        plt.xlabel('Subjects')
        plt.ylabel('Scores')
        plt.title('Semester Marks Analysis')
        plt.xticks(index + bar_width, ('COA', 'AOA', 'AMIV', 'CG' , 'OS'))
        plt.legend()

        plt.tight_layout()
        plt.show()
        conn.close()
        print("HELLo")


        
    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "MainWindow"))
        self.label_5.setText(_translate("student", "SEM 4"))
        self.roll_no.setText(_translate("student", "Roll No"))
        self.label_7.setText(_translate("student", "Computer "))
        self.label_8.setText(_translate("student", "Engineering"))
        self.label_coa.setText(_translate("student", "COA"))
        self.label_aoa.setText(_translate("student", "AOA"))
        self.label_am4.setText(_translate("student", "AM4"))
        self.label_cg.setText(_translate("student", "CG"))
        self.label_6.setText(_translate("student", "OS"))
        self.label.setText(_translate("student", "Total Marks"))
        self.mess_total.setText(_translate("student", "20"))
        self.button_analyse.setText(_translate("student", "Analyze"))



import images_rc


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    student = QtWidgets.QMainWindow()
    ui = Ui_student()
    ui.setupUi(student)
    student.show()
    sys.exit(app.exec_())
