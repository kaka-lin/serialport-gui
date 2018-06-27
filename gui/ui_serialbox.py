from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy

class Ui_SerialBox(object):
    def setupUi(self, serialBox):
        serialBox.setObjectName("serialBox")

        self.centralWidget = QtWidgets.QWidget(serialBox)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(470, 50, 61, 31))
        self.label.setObjectName("label")
        self.portNamComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.portNamComboBox.setGeometry(QtCore.QRect(520, 50, 181, 31))
        self.portNamComboBox.setObjectName("portNamComboBox")
        self.openPortBtn = QtWidgets.QPushButton(self.centralWidget)
        self.openPortBtn.setGeometry(QtCore.QRect(510, 110, 101, 41))
        self.openPortBtn.setObjectName("openPortBtn")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 360, 91, 16))
        self.label_2.setObjectName("label_2")
        self.sendTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.sendTextEdit.setGeometry(QtCore.QRect(150, 340, 301, 81))
        self.sendTextEdit.setObjectName("sendTextEdit")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.label_3.setObjectName("label_3")
        self.recvTextBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.recvTextBrowser.setGeometry(QtCore.QRect(150, 40, 301, 221))
        self.recvTextBrowser.setMouseTracking(False)
        self.recvTextBrowser.setObjectName("recvTextBrowser")
        self.sendTextButton = QtWidgets.QPushButton(self.centralWidget)
        self.sendTextButton.setGeometry(QtCore.QRect(500, 360, 93, 28))
        self.sendTextButton.setObjectName("sendTextButton")
        self.statusLabel = QtWidgets.QLabel(self.centralWidget)
        self.statusLabel.setGeometry(QtCore.QRect(470, 210, 151, 21))
        self.statusLabel.setObjectName("statusLabel")
        self.closePortBtn = QtWidgets.QPushButton(self.centralWidget)
        self.closePortBtn.setGeometry(QtCore.QRect(620, 110, 101, 41))
        self.closePortBtn.setObjectName("closePortBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralWidget)
        self.clearBtn.setGeometry(QtCore.QRect(20, 70, 101, 41))
        self.clearBtn.setObjectName("clearBtn")
        
        self.retranslateUi(serialBox)

        #self.open_button.clicked.connect(plotBox.openFile)
        #self.plot_button.clicked.connect(plotBox.plotData)
        #self.model.itemChanged.connect(plotBox.onItemChanged)

    def retranslateUi(self, serialBox):
        _translate = QtCore.QCoreApplication.translate
        serialBox.setTitle(_translate("SerialBox", "Serial Box"))
        self.label.setText(_translate("SerialBox", "Port: "))
        self.openPortBtn.setText(_translate("SerialBox", "Open"))
        self.label_2.setText(_translate("SerialBox", "SendBuffer:"))
        self.label_3.setText(_translate("SerialBox", "RecvBuffer:"))
        self.sendTextButton.setText(_translate("SerialBox", "Send"))
        self.statusLabel.setText(_translate("SerialBox", "Status: not  connect"))
        self.closePortBtn.setText(_translate("SerialBox", "Close"))
        self.clearBtn.setText(_translate("SerialBox", "Clear"))
    