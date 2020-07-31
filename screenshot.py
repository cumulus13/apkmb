# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenshot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screenshot_dialog(object):
    def setupUi(self, screenshot_dialog):
        screenshot_dialog.setObjectName("screenshot_dialog")
        screenshot_dialog.resize(633, 651)
        self.scrollArea = QtWidgets.QScrollArea(screenshot_dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 481, 631))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 629))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(screenshot_dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(500, 10, 121, 631))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 119, 629))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(screenshot_dialog)
        QtCore.QMetaObject.connectSlotsByName(screenshot_dialog)

    def retranslateUi(self, screenshot_dialog):
        _translate = QtCore.QCoreApplication.translate
        screenshot_dialog.setWindowTitle(_translate("screenshot_dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screenshot_dialog = QtWidgets.QDialog()
    ui = Ui_screenshot_dialog()
    ui.setupUi(screenshot_dialog)
    screenshot_dialog.show()
    sys.exit(app.exec_())

