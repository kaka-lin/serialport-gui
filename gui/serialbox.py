import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo
from gui.ui_serialbox import Ui_SerialBox
from app.serialport import SerialPort

class SerialBox(QtWidgets.QGroupBox):
    """ Serial number edit box """
    def __init__(self, parent=None):
        super(SerialBox, self).__init__(parent)

        self.port = SerialPort()
        self.port.serial.readyRead.connect(self.read)

        self.ui = Ui_SerialBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
        self.serialPortInfo()
    
    def serialPortInfo(self):
        port_list = QSerialPortInfo.availablePorts()
        
        for port in port_list:
            self.ui.portNamComboBox.insertItem(0, port.portName()) 
    
    def open(self):
        port_name = self.ui.portNamComboBox.currentText()
        print("open port:", port_name)

        self.port.openSerial(port_name)

    def close(self):
        self.port.closeSerial()
    
    def clear(self):
        self.ui.recvTextBrowser.clear()
    
    def write(self):
        data = self.ui.sendTextEdit.toPlainText()
        self.port.writeData(data)
    
    def read(self):
        data = self.port.readData()
        self.ui.recvTextBrowser.insertPlainText(data)
        self.ui.recvTextBrowser.insertPlainText("\n")
    
    def autoScroll(self):
        text_cursor = self.ui.recvTextBrowser.textCursor()
        text_cursor.movePosition(QtGui.QTextCursor.End)
        self.ui.recvTextBrowser.setTextCursor(text_cursor)
