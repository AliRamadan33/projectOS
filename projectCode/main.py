
# Created by: PyQt5 UI code generator 5.6

from PyQt5 import QtCore, QtGui, QtWidgets
from FCFS import Ui_FCFS
from SJF_preem import Ui_SJF_preem
from SJF_non import Ui_SJF_non_preem
from RR import Ui_RR
from priority_preem import Ui_priority_preem
from priority_non_preem import Ui_priority_non_preem


class Ui_first(object):
    # the following functions is called based on user choice for a scheduling type
    # each function opens a new window to ask user for required information according to the scheduler type
    def open_FCFS_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FCFS_info()
        self.ui.setupUi(self.window)
        #first.hide() # if desired to hide the main window when the new one appears
        self.window.show()

    def open_SJF_preem_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SJF_preem_info()
        self.ui.setupUi(self.window)
        #first.hide() 
        self.window.show()

    def open_SJF_non_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SJF_non_info()
        self.ui.setupUi(self.window)
        #first.hide() 
        self.window.show()
    
    def open_RR_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RR_info()
        self.ui.setupUi(self.window)
        #first.hide() 
        self.window.show()
        
    def open_Priority_preem_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_priority_preem_info()
        self.ui.setupUi(self.window)
        #first.hide() 
        self.window.show()
        
    def open_Priority_non_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_priority_non_info()
        self.ui.setupUi(self.window)
        #first.hide() 
        self.window.show()
        
    def setupUi(self, first):
        
        first.setObjectName("first")
        first.resize(520, 485)
        self.centralwidget = QtWidgets.QWidget(first)
        self.centralwidget.setObjectName("centralwidget")
        self.FCFS_but = QtWidgets.QPushButton(self.centralwidget)
        self.FCFS_but.setGeometry(QtCore.QRect(140, 50, 121, 31))
        self.FCFS_but.setObjectName("FCFS_but")

        self.FCFS_but.clicked.connect(self.open_FCFS_info)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 41))
        self.label.setObjectName("label")
        self.SJFpreem_but = QtWidgets.QPushButton(self.centralwidget)
        self.SJFpreem_but.setGeometry(QtCore.QRect(140, 100, 121, 31))
        self.SJFpreem_but.setObjectName("SJFpreem_but")

        self.SJFpreem_but.clicked.connect(self.open_SJF_preem_info)
        
        self.SJFnon_but = QtWidgets.QPushButton(self.centralwidget)
        self.SJFnon_but.setGeometry(QtCore.QRect(140, 150, 121, 31))
        self.SJFnon_but.setObjectName("SJFnon_but")

        self.SJFnon_but.clicked.connect(self.open_SJF_non_info)

        
        self.RR_but = QtWidgets.QPushButton(self.centralwidget)
        self.RR_but.setGeometry(QtCore.QRect(140, 200, 121, 31))
        self.RR_but.setObjectName("RR_but")

        self.RR_but.clicked.connect(self.open_RR_info)
        
        self.Prioritypreem_but = QtWidgets.QPushButton(self.centralwidget)
        self.Prioritypreem_but.setGeometry(QtCore.QRect(140, 250, 121, 31))
        self.Prioritypreem_but.setObjectName("Prioritypreem_but")

        self.Prioritypreem_but.clicked.connect(self.open_Priority_preem_info)

        
        self.Prioritynon_but = QtWidgets.QPushButton(self.centralwidget)
        self.Prioritynon_but.setGeometry(QtCore.QRect(140, 300, 121, 31))
        self.Prioritynon_but.setObjectName("Prioritynon_but")

        self.Prioritynon_but.clicked.connect(self.open_Priority_non_info)
        
        first.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(first)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        first.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(first)
        self.statusbar.setObjectName("statusbar")
        first.setStatusBar(self.statusbar)

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "CPU Scheduler"))
        self.FCFS_but.setText(_translate("first", "FCFS"))
        self.label.setText(_translate("first", "Scheduling type:"))
        self.SJFpreem_but.setText(_translate("first", "SJF Preemptive"))
        self.SJFnon_but.setText(_translate("first", "SJF NonPreemptive"))
        self.RR_but.setText(_translate("first", "Round Robin"))
        self.Prioritypreem_but.setText(_translate("first", "Priority Preemptive"))
        self.Prioritynon_but.setText(_translate("first", "Priority NonPreemptive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    first = QtWidgets.QMainWindow()
    ui = Ui_first()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())
