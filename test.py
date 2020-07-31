#!c:/SDK/Anaconda2/python.exe

#import sys
#import qdarkstyle
#import os

#os.environ['QT_API'] = 'pyqt5'

#from qtpy import QtWidgets
#app = QtWidgets.QApplication(sys.argv)
#window = QtWidgets.QMainWindow()
#app.setStyleSheet(qdarkstyle.load_stylesheet())
#window.show()
#app.exec_()


#import sys
##from screenshot import *
#from PyQt5.QtWidgets import QLabel, QDialog, QApplication, QWidget, QVBoxLayout, QScrollArea
##from PyQt5.QtGui import QPixmap
#from PyQt5.QtCore import * 

#class My_Application(QDialog):
    #def __init__(self):
        #super(My_Application, self).__init__()
        ##super(My_Application, self).__init__()
        #self.ui = Ui_screenshot_dialog()
        #self.ui.setupUi(self)

        #self.ui.label.setPixmap(QPixmap('download.png'))
        #self.ui.label.setScaledContents(True)

        #self.ui.label_2.setPixmap(QPixmap('download.png'))
        #self.ui.label_2.setScaledContents(True)

        #self.ui.label_3.setPixmap(QPixmap('download.png'))
        #self.ui.label_3.setScaledContents(True)

        #self.ui.label_4.setPixmap(QPixmap('download.png'))
        #self.ui.label_4.setScaledContents(True)

        #self.ui.label_5.setPixmap(QPixmap('download.png'))
        #self.ui.label_5.setScaledContents(True)

        #self.ui.label_6.setPixmap(QPixmap('download.png'))
        #self.ui.label_6.setScaledContents(True)

        #self.ui.label_7.setPixmap(QPixmap('download.png'))
        #self.ui.label_7.setScaledContents(True)

        #self.ui.label_8.setPixmap(QPixmap('download.png'))
        #self.ui.label_8.setScaledContents(True)

        #self.ui.label_9.setPixmap(QPixmap('download.png'))
        #self.ui.label_9.setScaledContents(True)

        #self.ui.label_10.setPixmap(QPixmap('download.png'))
        #self.ui.label_10.setScaledContents(True)

        #self.ui.scrollArea.setWidgetResizable(True)
        #self.ui.scrollArea.setFixedHeight(400)


#app = QApplication(sys.argv)
##app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#class_instance = My_Application()
#class_instance.show()
#app.exec_()


#from PyQt5 import QtCore, QtGui
#from PyQt5.QtWidgets import QLabel, QDialog, QApplication, QWidget, QVBoxLayout, QScrollArea, QPushButton
##from PyQt5.QtGui import QPixmap
#from PyQt5.QtCore import * 

#class myDialog(QDialog):
    #_buttons = 0

    #def __init__(self, parent=None):
        #super(myDialog, self).__init__(parent)

        #self.lbl = QLabel(self)
        #self.lbl.width = 100
        #self.lbl.height = 600
        #self.lbl.setText("TETSETET")
        #print("width =", self.lbl.width)
        #print("height =", self.lbl.height)

        #self.pushButton = QPushButton(self)
        #self.pushButton.setText("Add Button!")
        #self.pushButton.clicked.connect(self.on_pushButton_clicked)

        #self.scrollArea = QScrollArea(self)
        #self.scrollArea.setWidgetResizable(True)
        #self.scrollAreaWidgetContents = QWidget(self.scrollArea)
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #self.verticalLayout = QVBoxLayout(self)
        #self.verticalLayout.addWidget(self.pushButton)
        #self.verticalLayout.addWidget(self.scrollArea)
        #self.verticalLayout.addWidget(self.lbl)

        #self.verticalLayoutScroll = QVBoxLayout(self.scrollAreaWidgetContents)

    #@QtCore.pyqtSlot()
    #def on_pushButton_clicked(self):
        #self._buttons  += 1
        #pustButtonName = u"Button {0}".format(self._buttons)

        #pushButton = QPushButton(self.scrollAreaWidgetContents)
        #pushButton.setText(pustButtonName)

        #self.verticalLayoutScroll.addWidget(pushButton)


#if __name__ == "__main__":
    #import sys

    #app = QApplication(sys.argv)
    #app.setApplicationName('myDialog')

    #main = myDialog()
    #main.show()

    #sys.exit(app.exec_())



from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__(*args, **kwargs)
        self.setFixedWidth(300)
        self.setFixedHeight(30)
        self.clicked.connect(self.animate)
        return

    #def animate(self):
        #self.anim = QPropertyAnimation(self, b'position')
        #self.anim.setDuration(3000)
        #self.anim.setStartValue(QPointF(self.pos().x(), self.pos().y()))
        #self.anim.setEndValue(QPointF(self.pos().x() + 200, self.pos().y() - 20))
        #self.anim.start()
        #return
        
    #def animate(self):
        #self.anim = QPropertyAnimation(self, b'position')
        #self.anim.setDuration(3000)
        #startpoint = self.mapToGlobal(self.pos())
        #endpoint = self.mapToGlobal(QPoint(self.pos().x() + 200, self.pos().y() - 20))
        #self.setWindowFlags(Qt.Popup)
        #self.show()
        #self.anim.setStartValue(QPointF(startpoint.x(), startpoint.y()))
        #self.anim.setEndValue(QPointF(endpoint.x(), endpoint.y()))
        #self.anim.start()
        #QTimer.singleShot(1000, self.hide)
        #return
        
    #def animate(self):
        #startpoint = self.mapToGlobal(QPoint())
        #self.setWindowFlags(Qt.Popup)
        #self.show()
        #anim = QPropertyAnimation(
            #self,
            #b"pos",
            #self,
            #duration=3000,
            #startValue=startpoint,
            #endValue=startpoint + QPoint(200, -20),
            #finished=self.deleteLater,
        #)
        #anim.start()
        
    def animate(self):
        startpoint = self.window().mapFromGlobal(self.mapToGlobal(QPoint()))
        self.setParent(self.window())
        anim = QPropertyAnimation(
            self,
            b"pos",
            self,
            duration=3000,
            startValue=startpoint,
            endValue=startpoint + QPoint(200, -20),
            finished=self.deleteLater,
        )
        anim.start()
        self.show()    

    def _set_pos_(self, pos):
        self.move(pos.x(), pos.y())
        return

    position = pyqtProperty(QPointF, fset=_set_pos_)


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("ANIMATION TEST")

        # OUTER FRAME
        # ============
        self.frm = QFrame()
        self.frm.setStyleSheet("""
            QFrame {
                background: #d3d7cf;
                border: none;
            }
        """)
        self.lyt = QHBoxLayout()
        self.frm.setLayout(self.lyt)
        self.setCentralWidget(self.frm)

        # BUTTON FRAME
        # =============
        self.btn_frm = QFrame()
        self.btn_frm.setStyleSheet("""
            QFrame {
                background: #ffffff;
                border: none;
            }
        """)
        self.btn_frm.setFixedWidth(400)
        self.btn_frm.setFixedHeight(200)
        self.btn_lyt = QVBoxLayout()
        self.btn_lyt.setAlignment(Qt.AlignTop)
        self.btn_lyt.setSpacing(5)
        self.btn_frm.setLayout(self.btn_lyt)

        # SCROLL AREA
        # ============
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border-style: solid;
                border-width: 1px;
            }
        """)
        self.scrollArea.setWidget(self.btn_frm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedWidth(400)
        self.scrollArea.setFixedHeight(150)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.lyt.addWidget(self.scrollArea)

        # ADD BUTTONS TO BTN_LAYOUT
        # ==========================
        self.btn_lyt.addWidget(MyButton("Foo"))
        self.btn_lyt.addWidget(MyButton("Bar"))
        self.btn_lyt.addWidget(MyButton("Baz"))
        self.btn_lyt.addWidget(MyButton("Qux"))
        self.show()
        return

if __name__== '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()
    sys.exit(app.exec_())