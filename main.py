# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QFileDialog
from PyQt5.QtGui import *
from pyCode import Ui_pyCode
import os
import sys
import re
import string
import gettext
import barcode
import random
from barcode.writer import ImageWriter
from barcode.codex import Code39, Code128
from PIL import Image, ImageDraw, ImageFont, ImageWin, ImageQt


class MainWindow(QtWidgets.QMainWindow, Ui_pyCode):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 預設暫無圖片
        self.pm = QPixmap(filepath + "\\temp\\unnamed.jpg")
        self.image.setPixmap(self.pm)

        # 切分狀態欄為兩條
        self.hintmsg = QtWidgets.QLabel()
        self.alertmsg = QtWidgets.QLabel()
        self.statusbar.addPermanentWidget(self.hintmsg, stretch=1)
        self.statusbar.addPermanentWidget(self.alertmsg, stretch=1)
        # 左提示 | 右警告 公平分

        # 針對
        # header_item = QTableWidgetItem("員工姓名")
        # header_item.setBackground(QtCore.Qt.red) # 헤더 배경색 설정 --> app.setStyle() 설정해야만 작동한다.
        # self.s_gen.setHorizontalHeaderItem(1, header_item)

        # self.setgenheader()

        # 針對單身表格設置
        # self.s_gen.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.s_gen.verticalHeader().setVisible(False)
        # self.s_gen.horizontalHeader().setVisible(False)

        # 程式初始化
        # self.detail_init()
        self.hintmsg.setText('開啟完畢')
        self.code39.setChecked(True)
        self.code39.toggled.connect(lambda: self.btnstate(self.code39))
        self.code128.toggled.connect(lambda: self.btnstate(self.code128))
        # 設定查詢按鈕功能
        # self.query.triggered.connect(lambda: self.whichbtn(self.query, 'cl'))
        # self.exporttoexcel.triggered.connect(lambda: self.writeExcel())
        # self.statusbar.showMessage('查詢完畢!',5000)
        # self.query.triggered.connect(self.refresh_data)
        # self.Title.setText("hello Python")
        # self.World.clicked.connect(self.onWorldClicked)
        # self.China.clicked.connect(self.onChinaClicked)
        # self.lineEdit.textChanged.connect(self.onlineEditTextChanged)
        # self.query.triggered.connect(self.refresh_data)
        # self.generate.clicked.connect(self.barcode_gen(code39, self.codeword))
        # 用不到按鈕關閉
        self.editcopy.setEnabled(False)
        self.editcut.setEnabled(False)
        self.insert.setEnabled(False)
        self.modify.setEnabled(False)
        self.delete_2.setEnabled(False)
        self.reproduce.setEnabled(False)
        self.invalid.setEnabled(False)

        # 產生按鈕
        self.generate.clicked.connect(self.barcode_gen)
        # 儲存按鈕
        self.download.clicked.connect(self.barcode_save)

        # 離開按鈕
        self.exit.triggered.connect(self.closeEvent)
        self.exit2.triggered.connect(self.closeEvent)
        # Show widget
        self.show()

    def btnstate(self, btn):
        # if btn.text() == "Code39":
        #     if btn.isChecked() == True:
        #         print(btn.text() + " is selected")
        #     else:
        #         print(btn.text() + " is deselected")

        # if btn.text() == "Code128":
        #     if btn.isChecked() == True:
        #         print(btn.text() + " is selected")
        #     else:
        #         print(btn.text() + " is deselected")

        self.hintmsg.setText('選擇'+btn.text())
        print(self.code39.isChecked())
        print(self.code128.isChecked())
        self.barcode_gen()

    def detail_init(self):
        g_rec_b = 0
        self.cnt.setAlignment(QtCore.Qt.AlignRight)
        # self.cnt.setText(str(g_rec_b))

    def closeEvent(self, event):
        QApplication.closeAllWindows()

    def barcode_gen(self):

        # if self.codeword.text() == '':
        #    return

        if self.code39.isChecked():
            barcode_type = "Code39"
        else:
            barcode_type = "Code128"

        #print("code type:"+str(barcode_type))
        barcode_to_png(barcode_type, self.codeword.text(),
                       filepath + "\\"+barcode_type+"\\"+self.codeword.text())

        self.pm = QPixmap(filepath + "\\temp\\image.png")
        self.image.setPixmap(QPixmap(""))
        self.image.setPixmap(self.pm)

    def barcode_save(self):

        if self.code39.isChecked():
            barcode_type = "Code39"
        else:
            barcode_type = "Code128"

        # file = QFileDialog(self.parent()).getSaveFileName(
        #   self, "存放圖片位置", os.curdir, "PNG Files (*.png)")
        image = ImageQt.fromqpixmap(self.image.pixmap())
        if barcode_type == 'Code39':
            filesave = filepath+"\\code39\\"+self.codeword.text()+".png"
            print(filesave)
            image.save(filesave)
        elif barcode_type == 'Code128':
            filesave = filepath+"\\code128\\"+self.codeword.text()+".png"
            image.save(filesave)
        self.alertmsg.setText('檔案存放到 '+filesave)
        # 生成一维码，参数:码类型、码内容、文件名(文件名后缀自动加.png)


def barcode_to_png(barcode_type, text_str, filename):
    print(type(text_str))
    print("gencode string="+text_str)

    if text_str == "":
        print("empty")
        return

    imagewriter = ImageWriter()
    # add_checksum : Boolean   Add the checksum to code or not (default: True)

    try:
        if barcode_type == 'Code39':
            bfile = Code39(text_str, writer=imagewriter, add_checksum=False)
        elif barcode_type == 'Code128':
            bfile = Code128(text_str, writer=imagewriter)
        else:
            self.alertmsg.setText("沒有支援該方式!!")
    except Exception as e:
        print(f'An Error occurred: {e}')
        return

    # 不需要写后缀，ImageWriter初始化方法中默认self.format = 'PNG'
    bfile.save(filepath+"\\temp\\image")


def myRemovePic(self):
    self.image.setPixmap(QPixmap(""))


def myAddPic(self):
    self.image.setPixmap(self.pm)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # 當前目錄下建立兩個資料夾
    filepath = os.path.abspath(os.path.dirname(__file__))
    os.system("mkdir "+filepath+"\\code128")
    os.system("mkdir "+filepath+"\\code39")
    os.system("mkdir "+filepath+"\\temp")

    mainWindow = MainWindow()
    # mainWindow.show()
    sys.exit(app.exec_())
