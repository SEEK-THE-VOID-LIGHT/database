from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QApplication, QWidget, QLineEdit, QTextEdit
import sqlite3
import os.path
import os
import shutil
import subprocess

conn = sqlite3.connect('manDB.db')
cursor = conn.cursor()
currentid = 0
lastword = ""


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1111, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 10, 971, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Cond")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(990, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 321, 251))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.add = QtWidgets.QPushButton(self.groupBox_2)
        self.add.setGeometry(QtCore.QRect(10, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.list = QtWidgets.QPushButton(self.groupBox_2)
        self.list.setGeometry(QtCore.QRect(10, 70, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.list.setFont(font)
        self.list.setObjectName("list")
        self.delete_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_2.setGeometry(QtCore.QRect(10, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.delete_2.setFont(font)
        self.delete_2.setObjectName("delete_2")
        self.search = QtWidgets.QPushButton(self.groupBox_2)
        self.search.setGeometry(QtCore.QRect(10, 190, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(340, 120, 471, 251))
        self.image.setObjectName("image")
        self.edit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.edit1.setGeometry(QtCore.QRect(20, 430, 251, 271))
        self.edit1.setObjectName("edit1")
        self.edit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.edit2.setGeometry(QtCore.QRect(300, 430, 251, 271))
        self.edit2.setObjectName("edit2")
        self.edit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.edit3.setGeometry(QtCore.QRect(580, 430, 251, 271))
        self.edit3.setObjectName("edit3")
        self.edit4 = QtWidgets.QTextEdit(self.centralwidget)
        self.edit4.setGeometry(QtCore.QRect(860, 430, 251, 271))
        self.edit4.setObjectName("edit4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(930, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.imageurl = QtWidgets.QLineEdit(self.centralwidget)
        self.imageurl.setGeometry(QtCore.QRect(830, 120, 291, 41))
        self.imageurl.setObjectName("imageurl")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(830, 200, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(830, 290, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFILE.addAction(self.actionSave)
        self.menuFILE.addAction(self.actionClose)
        self.menubar.addAction(self.menuFILE.menuAction())

        self.list.clicked.connect(self.create_new)
        self.actionClose.triggered.connect(self.exit)
        self.search.clicked.connect(self.refresh)
        self.add.clicked.connect(self.operate)
        self.image.setPixmap(QtGui.QPixmap('baseimage.jpg'))
        self.actionSave.triggered.connect(self.saveword)
        self.delete_2.clicked.connect(self.delete_confirmation)
        self.open.clicked.connect(self.openexplorer)
        self.copy.setEnabled(False)
        self.imageurl.setPlaceholderText("<content>")
        self.imageurl.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def refresh(self):
        global currentid
        self.saveword()
        cursor.execute("SELECT rowid, * FROM dictionary")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == currentid:
                array = row
        try:
            currentid = array[0]
            self.label.setText(array[1])
            self.edit1.setText(array[2])
            self.edit2.setText(array[3])
            self.edit3.setText(array[4])
            self.edit4.setText(array[5])
            cursor.execute('SELECT * FROM images')
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == currentid:
                    tmpimg = []
                    for root, dirs, files in os.walk(f"./{array[1]}"):
                        for filename in files:
                            tmpimg.append(filename)
                    try:
                        url = f"{row[1]}{tmpimg[0]}"
                        pixmap = QtGui.QPixmap(url)
                        pixmap_resized = pixmap.scaled(700, 300, QtCore.Qt.KeepAspectRatio)
                        self.image.setPixmap(pixmap_resized)
                    except:
                        print("no image")
        except:
            pass

    def openexplorer(self):
        cursor.execute("SELECT * FROM images")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == currentid:
                newpath = row[1].replace("/", "")
                path = f"{newpath}"
                print(row)
                subprocess.call(["explorer", f"{path}"])

    def delete_confirmation(self):
        array = self.defsearch()
        if array == 11:
            return
        if array != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"Wollen Sie das Wort <<{array[1]}>> wirklich löschen?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            #msg.buttonClicked.connect(lambda: self.delete_execute(array, i))
            msg.setWindowTitle("NEU?")
            x = msg.exec_()
            if x == 1024:
                self.delete_execute(array)

    def delete_execute(self, array):
        sql_id = array[0]
        cursor.execute("SELECT * from images")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == sql_id:
                path = row[1]
                break
        shutil.rmtree(path, ignore_errors=True)
        sql = [sql_id]
        cursor.execute("DELETE from dictionary WHERE rowid=?", sql)
        conn.commit()
        cursor.execute("DELETE from images WHERE ID=?", sql)
        conn.commit()

    def getid(self, word):
        cursor.execute("SELECT rowid, * FROM dictionary")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == word:
                return row[0]

    def saveword(self):
        if currentid != 0:
            descr1 = self.edit1.toPlainText()
            descr2 = self.edit2.toPlainText()
            descr3 = self.edit3.toPlainText()
            descr4 = self.edit4.toPlainText()
            mainword = self.label.text()
            savearray = [mainword, descr1, descr2, descr3, descr4, currentid]
            sql = """UPDATE dictionary
                    SET Wort = ? ,
                        desc1 = ? ,
                        desc2 = ? ,
                        desc3 = ? ,
                        desc4 = ?
                    WHERE rowid = ?"""
            cursor.execute(sql, savearray)
            conn.commit()
            #msg = QMessageBox()
            #msg.setWindowTitle("SUCCESS")
            #msg.setText("Speichern erfolgreich!")

    '''def deflist(self):
        cursor.execute('SELECT * FROM dictionary')
        rows = cursor.fetchall()
        newarray = []
        for row in rows:
            newarray.append(row[0])
        newstring = '\n'.join(newarray)
        msg = QMessageBox()
        msg.setText(newstring)
        msg.setWindowTitle("ALLE")
        msg.exec_()'''

    def defsearch(self):
        self.saveword()
        text, ok = QInputDialog.getText(self.dialog, "SEARCH", "Name zum Suchen:\n\nPS: auf Groß- /Kleinschreibung achten\nund vollständiges Wort eingeben")
        if ok:
            cursor.execute('SELECT rowid, * FROM dictionary')
            rows = cursor.fetchall()
            for row in rows:
                text_array = row[1].split(" ")
                for i in text_array:
                    print(i)
                    if i == text:
                        msg = QMessageBox()
                        msg.setText(f"Das Wort <<{row[1]}>> existiert in der Datenbank")
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("SUCCESS")
                        msg.exec_()
                        return row
            msg = QMessageBox()
            msg.setText(f"Das Wort <<{text}>> existiert NICHT in der Datenbank")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERROR")
            msg.exec_()
            return 0
        else:
            return 11

    def search_certain_text(self, text):
        cursor.execute('SELECT rowid, * FROM dictionary')
        rows = cursor.fetchall()
        for row in rows:
            text_array = row[1].split(" ")
            for i in text_array:
                print(i)
                if i == text:
                    return row

    def operate(self):
        global currentid
        array = self.defsearch()
        if array == 11:
            return
        if array != 0:
            currentid = array[0]
            self.label.setText(array[1])
            self.edit1.setText(array[2])
            self.edit2.setText(array[3])
            self.edit3.setText(array[4])
            self.edit4.setText(array[5])
            cursor.execute('SELECT * FROM images')
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == currentid:
                    tmpimg = []
                    for root, dirs, files in os.walk(f"./{array[1]}"):
                        for filename in files:
                            tmpimg.append(filename)
                    try:
                        url = f"{row[1]}{tmpimg[0]}"
                        pixmap = QtGui.QPixmap(url)
                        pixmap_resized = pixmap.scaled(700, 300, QtCore.Qt.KeepAspectRatio)
                        self.image.setPixmap(pixmap_resized)
                    except:
                        print("no image")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Das Wort existiert nicht\nWollen sie ein neues Wort erstellen?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(self.operate_new)
            msg.setWindowTitle("NEU?")
            msg.exec_()
    
    def create_new(self):
        global lastword
        text, ok = QInputDialog.getText(self.dialog,"NEU", "Neues Wort hinzufügen:")
        if ok:
            text = text.replace("\n", "")
            lastword = text
            path = f"./{text}"
            path1 = f"{text}/"
            try:
                os.mkdir(path)
            except OSError:
                msg = QMessageBox()
                msg.setText("Error 6: OSError")
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("ERROR")
                msg.exec_()
            sql = [(text, None, None, None, None)]
            cursor.executemany("INSERT into dictionary values (?,?,?,?,?)",sql)
            conn.commit()
            sqlimage = [(self.getid(text), path1)]
            cursor.executemany("INSERT into images values (?,?)", sqlimage)
            conn.commit()

            array = self.search_certain_text(text)

            global currentid
            if array == 11:
                return
            if array != 0:
                currentid = array[0]
                self.label.setText(array[1])
                self.edit1.setText(array[2])
                self.edit2.setText(array[3])
                self.edit3.setText(array[4])
                self.edit4.setText(array[5])
                cursor.execute('SELECT * FROM images')
                rows = cursor.fetchall()
                for row in rows:
                    if row[0] == currentid:
                        tmpimg = []
                        for root, dirs, files in os.walk(f"./{array[1]}"):
                            for filename in files:
                                tmpimg.append(filename)
                        try:
                            url = f"{row[1]}{tmpimg[0]}"
                            pixmap = QtGui.QPixmap(url)
                            pixmap_resized = pixmap.scaled(700, 300, QtCore.Qt.KeepAspectRatio)
                            self.image.setPixmap(pixmap_resized)
                        except:
                            print("no image")


    def operate_new(self, i):
        if i.text() == "OK":
            text, ok = QInputDialog.getText(self.dialog,"NEU", "Neues Wort hinzufügen:")
            if ok:
                path = f"./{text}"
                path1 = f"{text}/"
                try:
                    os.mkdir(path)
                except OSError:
                    msg = QMessageBox()
                    msg.setText("Error 6: OSError")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle("ERROR")
                    msg.exec_()
                sql = [(text, None, None, None, None)]
                cursor.executemany("INSERT into dictionary values (?,?,?,?,?)",sql)
                conn.commit()
                sqlimage = [(self.getid(text), path1)]
                cursor.executemany("INSERT into images values (?,?)", sqlimage)
                conn.commit()
        else:
            return



    def exit(self):
        self.saveword()
        exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MMM"))
        self.label.setText(_translate("MainWindow", "Datenbankbank V.1.0.2"))
        self.label_2.setText(_translate("MainWindow", "von VoidLight"))
        self.add.setText(_translate("MainWindow", "ÖFFNEN"))
        self.list.setText(_translate("MainWindow", "NEU"))
        self.delete_2.setText(_translate("MainWindow", "LÖSCHEN"))
        self.search.setText(_translate("MainWindow", "NEU LADEN"))
        self.image.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Erklärung 1"))
        self.label_4.setText(_translate("MainWindow", "Erklärung 2"))
        self.label_5.setText(_translate("MainWindow", "Erklärung 3"))
        self.label_6.setText(_translate("MainWindow", "Erklärung 4"))
        self.open.setText(_translate("MainWindow", "ORDNER ÖFFNEN"))
        self.copy.setText(_translate("MainWindow", "<content>"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.actionSave.setText(_translate("MainWindow", "Speichern"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClose.setText(_translate("MainWindow", "Beenden"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys

    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
