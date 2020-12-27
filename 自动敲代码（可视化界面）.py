# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from sys import exit as sexit, argv
from pykeyboard import PyKeyboard
from pyperclip import copy, paste
from time import sleep, time, strftime, gmtime
from string import ascii_lowercase, printable
from random import randint, uniform
from base64 import b64decode
import test2
from re import findall
class Ui_MainWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):

    def logic (self):
        self.running = False
        self.stop = False
        self.fileDirectory = "无"
        self.topHint = False
        self.autoSelf = False
        self.fileContains = None
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.hidden1)
        self.doubleSpinBox_2.setRange(0, self.doubleSpinBox_3.value())
        self.doubleSpinBox_3.setRange(self.doubleSpinBox_2.value(), 99.99)
        self.doubleSpinBox_2.valueChanged.connect(self.setRange)
        self.doubleSpinBox_3.valueChanged.connect(self.setRange)
        self.label_4.setHidden(True)
        self.doubleSpinBox_2.setHidden(True)
        self.label_5.setHidden(True)
        self.doubleSpinBox_3.setHidden(True)
        self.radioButton_2.toggled.connect(self.hidden2)
        self.pushButton_3.setStyleSheet("color:red;font-weight:bold;")
        self.pushButton.clicked.connect(self.findDirectory)
        self.pushButton_2.clicked.connect(self.run)
        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(b64decode(test2.stop))
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(b64decode(test2.windowIcon))
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.pushButton_3.clicked.connect(self.changeStop)
        self.pushButton_4.clicked.connect(self.changeTopHint)
        self.textBrowser_3.setText("无")
        editorFill = self.menubar.addMenu("编辑器自动补全")
        action1 = QtWidgets.QAction('方法参数中的self', self, checkable=True)
        action1.setStatusTip('方法参数中的self')
        action1.setChecked(False)
        action1.triggered.connect(self.changeAutoSelf)
        editorFill.addAction(action1)

    def setupUi (self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 360, 500, 195))
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(90, 110, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 160, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 135, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 50, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 160, 50, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 50, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 212, 54, 16))
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(240, 105, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(240, 155, 70, 30))
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 0.1)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(380, 155, 70, 30))
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 0.1)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 205, 50, 30))
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(600, 400, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 340, 54, 12))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 260, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(715, 30, 60, 12))
        self.label_9.setObjectName("label_9")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(520, 50, 450, 300))
        self.textBrowser_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(540, 415, 50, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(540, 480, 70, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(760, 480, 70, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(760, 530, 70, 20))
        self.label_13.setObjectName("label_13")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(610, 525, 100, 30))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 530, 70, 20))
        self.label_14.setObjectName("label_14")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(830, 525, 100, 30))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(830, 475, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(610, 475, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 275, 250, 20))
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(210, 35, 300, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser_3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 400, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 200, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.logic()

    def retranslateUi (self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动敲代码"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.radioButton.setText(_translate("MainWindow", "固定速度"))
        self.radioButton_2.setText(_translate("MainWindow", "随机速度"))
        self.label_2.setText(_translate("MainWindow", "打字速度："))
        self.label_3.setText(_translate("MainWindow", "速度："))
        self.label_4.setText(_translate("MainWindow", "下限："))
        self.label_5.setText(_translate("MainWindow", "上限："))
        self.label_6.setText(_translate("MainWindow", "错误率："))
        self.doubleSpinBox.setSuffix(_translate("MainWindow", "秒"))
        self.doubleSpinBox_2.setSuffix(_translate("MainWindow", "秒"))
        self.doubleSpinBox_3.setSuffix(_translate("MainWindow", "秒"))
        self.spinBox.setSuffix(_translate("MainWindow", "%"))
        self.label_7.setText(_translate("MainWindow", "进度："))
        self.pushButton_2.setText(_translate("MainWindow", "开始敲代码"))
        self.label_9.setText(_translate("MainWindow", "代码预览："))
        self.label_10.setText(_translate("MainWindow", "进度条："))
        self.label_11.setText(_translate("MainWindow", "已用时间："))
        self.label_12.setText(_translate("MainWindow", "预计时间："))
        self.label_13.setText(_translate("MainWindow", "全部字符："))
        self.label_14.setText(_translate("MainWindow", "已敲完字符："))
        self.lineEdit_5.setText(_translate("MainWindow", "敲代码未开始"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))
        self.pushButton_4.setText(_translate("MainWindow", "窗口置顶"))

    def findDirectory (self):
        if self.topHint:
            MainWindow.setWindowFlags(QtCore.Qt.Widget)
            MainWindow.show()
        get_filename_path, ok = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            "C:/",
                                                            "All Files (*);")
        if ok:
            try :
                file1 = open(str(get_filename_path), encoding="utf-8")
                file1.read()
                file1.close()
            except :
                try :
                    file1.close()
                except :
                    pass
                self.messageDialog("该文件无法打开！")
                return
            self.fileDirectory = str(get_filename_path)
            file1 = open(self.fileDirectory, encoding="utf-8")
            self.code = file1.read()
            file1.close()
            self.textBrowser_2.setText(self.code)
        self.textBrowser_3.setText(self.fileDirectory)
        if self.topHint:
            MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            MainWindow.show()

    def hidden1 (self):
        if self.radioButton.isChecked():
            self.label_3.setHidden(False)
            self.doubleSpinBox.setHidden(False)
        else:
            self.label_3.setHidden(True)
            self.doubleSpinBox.setHidden(True)

    def hidden2 (self):
        if self.radioButton_2.isChecked() :
            self.label_4.setHidden(False)
            self.doubleSpinBox_2.setHidden(False)
            self.label_5.setHidden(False)
            self.doubleSpinBox_3.setHidden(False)
        else :
            self.label_4.setHidden(True)
            self.doubleSpinBox_2.setHidden(True)
            self.label_5.setHidden(True)
            self.doubleSpinBox_3.setHidden(True)

    def setRange (self):
        if self.sender() == self.doubleSpinBox_2 :
            self.doubleSpinBox_3.setRange(self.doubleSpinBox_2.value(), 99.99)
        else:
            self.doubleSpinBox_2.setRange(0, self.doubleSpinBox_3.value())

    def run (self):
        def testIfIn(listNowNow, itemNowNow) :
            for itemNow in listNowNow :
                if itemNow in itemNowNow :
                    return True
            return False
        self.stop = False
        print("ok")
        self.textBrowser.clear()
        QtWidgets.QApplication.processEvents()
        if self.running :
            print("no")
            if self.topHint:
                MainWindow.setWindowFlags(QtCore.Qt.Widget)
                MainWindow.show()
            self.messageDialog("不要在敲代码时把鼠标点到该窗口上")
            self.lineEdit_5.setText("敲代码中止")
            self.progressBar.setValue(0)
            self.textBrowser.clear()
            self.lcdNumber_3.display(0)
            self.lcdNumber_4.display(0)
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.stop = True
            if self.topHint:
                MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                MainWindow.show()
            return
        self.running = True
        if self.fileDirectory == "无" :
            self.running = False
            if self.topHint:
                MainWindow.setWindowFlags(QtCore.Qt.Widget)
                MainWindow.show()
            self.messageDialog("没有导入需要敲的代码")
            if self.topHint:
                MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                MainWindow.show()
            return
        checked = self.radioButton.isChecked()
        if checked:
            speed = self.doubleSpinBox.value()
        else:
            speed = [self.doubleSpinBox_2.value(), self.doubleSpinBox_3.value()]
        error = int(self.spinBox.value()) / 100
        board = PyKeyboard()
        clipBefore = paste()
        characterSet = ascii_lowercase
        indexoferrors = []
        charoferrors = []
        for i in range(int(len(self.code) * error)):
            rand = randint(0, len(self.code) - 1)
            rand2 = randint(0, len(characterSet) - 1)
            indexoferrors.append(rand)
            charoferrors.append(characterSet[rand2])
        self.codes = self.code.split("\n")
        self.lineEdit_5.setHidden(False)
        for i in range(5):
            self.lineEdit_5.setText("%d秒后开始敲代码，请快速移到敲代码的位置" % (5 - i))
            QtWidgets.QApplication.processEvents()
            sleep(1)
            if self.stop:
                self.stop = False
                self.lineEdit_5.setText("敲代码中止")
                self.running = False
                self.progressBar.setValue(0)
                self.textBrowser.clear()
                self.lcdNumber_3.display(0)
                self.lcdNumber_4.display(0)
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                copy(clipBefore)
                QtWidgets.QApplication.processEvents()
                return
        time1 = time()
        self.lineEdit_5.setText("正在敲代码")
        QtWidgets.QApplication.processEvents()
        count = 0
        for i in self.codes:
            i = i.replace("\n", "")
            for j in i:
                if j == " " or j == "\t":
                    board.tap_key(j)
                    self.textBrowser.setText(self.textBrowser.toPlainText() + j)
                    QtWidgets.QApplication.processEvents()
                elif j in printable:
                    board.tap_key(j)
                    self.textBrowser.setText(self.textBrowser.toPlainText() + j)
                    QtWidgets.QApplication.processEvents()
                    if checked :
                        sleep(speed)
                    else :
                        sleep(uniform(speed[0], speed[1]))
                else:
                    self.textBrowser.setText(self.textBrowser.toPlainText() + j)
                    QtWidgets.QApplication.processEvents()
                    copy(j)
                    board.press_key(board.control_key)
                    board.tap_key('v')
                    board.release_key(board.control_key)
                    if checked :
                        sleep(speed)
                    else :
                        sleep(uniform(speed[0], speed[1]))
                for k in range(len(charoferrors)):
                    if indexoferrors[k] == count:
                        charnow = charoferrors[k]
                        self.textBrowser.setText(self.textBrowser.toPlainText() + charnow)
                        QtWidgets.QApplication.processEvents()
                        board.tap_key(charnow)
                        if checked:
                            sleep(speed)
                        else:
                            sleep(uniform(speed[0], speed[1]))
                        board.tap_key(board.backspace_key)
                        self.textBrowser.setText(self.textBrowser.toPlainText() [:-1])
                        QtWidgets.QApplication.processEvents()
                        if checked:
                            sleep(speed)
                        else:
                            sleep(uniform(speed[0], speed[1]))
                count += 1
                if self.stop :
                    self.stop = False
                    self.lineEdit_5.setText("敲代码中止")
                    self.running = False
                    self.progressBar.setValue(0)
                    self.textBrowser.clear()
                    self.lcdNumber_3.display(0)
                    self.lcdNumber_4.display(0)
                    self.lineEdit_3.clear()
                    self.lineEdit_4.clear()
                    copy(clipBefore)
                    return
                progressnow = count / len(self.code)
                self.progressBar.setValue(progressnow * 100)
                self.lcdNumber_3.display(count)
                self.lcdNumber_4.display(len(self.code))
                timenow = time() - time1
                timeanother = timenow
                timenow = gmtime(timenow)
                timenowm = strftime("%M", timenow)
                timenows = strftime("%S", timenow)
                timenowh = int((timeanother - int(timenowm) * 60 - int(timenows)) / 3600)
                prophesy = int(timeanother / progressnow)
                prophesyanother = prophesy
                prophesy = gmtime(prophesy)
                prophesym = strftime("%M", prophesy)
                prophesys = strftime("%S", prophesy)
                prophesyh = int((prophesyanother - int(prophesym) * 60 - int(prophesys)) / 3600)
                if timenowh == 0 :
                    if timenowm == "00" :
                        self.lineEdit_4.setText("%s秒" % timenows)
                    else :
                        self.lineEdit_4.setText("%s分%s秒" % (timenowm, timenows))
                else :
                    self.lineEdit_4.setText("%d时%s分%s秒" % (timenowh, timenowm, timenows))
                if prophesyh == 0 :
                    if prophesym == "00" :
                        self.lineEdit_3.setText("%s秒" % prophesys)
                    else :
                        self.lineEdit_3.setText("%s分%s秒" % (prophesym, prophesys))
                else :
                    self.lineEdit_3.setText("%d时%s分%s秒" % (prophesyh, prophesym, prophesys))
                QtWidgets.QApplication.processEvents()
            if count < len(self.code) :
                count += 1
                copy("\n")
                self.textBrowser.setText(self.textBrowser.toPlainText() + "\n")
                progressnow = count / len(self.code)
                self.progressBar.setValue(progressnow * 100)
                self.lcdNumber_3.display(count)
                self.lcdNumber_4.display(len(self.code))
                timenow = time() - time1
                timeanother = timenow
                timenow = gmtime(timenow)
                timenowm = strftime("%M", timenow)
                timenows = strftime("%S", timenow)
                timenowh = int((timeanother - int(timenowm) * 60 - int(timenows)) / 3600)
                prophesy = int(timeanother / progressnow)
                prophesyanother = prophesy
                prophesy = gmtime(prophesy)
                prophesym = strftime("%M", prophesy)
                prophesys = strftime("%S", prophesy)
                prophesyh = int((prophesyanother - int(prophesym) * 60 - int(prophesys)) / 3600)
                if timenowh == 0:
                    if timenowm == "00":
                        self.lineEdit_4.setText("%s秒" % timenows)
                    else:
                        self.lineEdit_4.setText("%s分%s秒" % (timenowm, timenows))
                else:
                    self.lineEdit_4.setText("%d时%s分%s秒" % (timenowh, timenowm, timenows))
                if prophesyh == 0:
                    if prophesym == "00":
                        self.lineEdit_3.setText("%s秒" % prophesys)
                    else:
                        self.lineEdit_3.setText("%s分%s秒" % (prophesym, prophesys))
                else:
                    self.lineEdit_3.setText("%d时%s分%s秒" % (prophesyh, prophesym, prophesys))
                QtWidgets.QApplication.processEvents()
                board.press_key(board.control_key)
                board.tap_key('v')
                board.release_key(board.control_key)
                if checked:
                    sleep(speed)
                else:
                    sleep(uniform(speed[0], speed[1]))
        copy(clipBefore)
        self.lineEdit_5.setText("敲代码结束")
        self.running = False

    def changeStop (self):
        self.stop = True

    def messageDialog (self, content):
        QtWidgets.QMessageBox.critical(self, '错误', content)

    def changeTopHint (self):
        if self.topHint :
            MainWindow.setWindowFlags(QtCore.Qt.Widget)
            self.pushButton_4.setText("窗口置顶")
            self.topHint = False
        else :
            MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.pushButton_4.setText("取消置顶")
            self.topHint = True
        MainWindow.show()

    def changeAutoSelf (self):
        if self.autoSelf :
            self.autoSelf = False
        else :
            self.autoSelf = True
app = QtWidgets.QApplication(argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sexit(app.exec_())
# pyinstaller -F -i xxx.ico D:\丁敬轩\我的编程\Python\python 程序1\实践\自动敲代码\自动敲代码（可视化界面）.py D:\丁敬轩\我的编程\Python\python 程序1\实践\自动敲代码\test2.py