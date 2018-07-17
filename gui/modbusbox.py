import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo
from gui.ui_modbusbox import Ui_ModbusBox
from app.kmodbus import KModbus

class ModbusBox(QtWidgets.QGroupBox):
    """ Modbus box """
    def __init__(self, parent=None):
        super(ModbusBox, self).__init__(parent)

        self.modbus = KModbus()
        #self.modbus.openFinishSig.connect(self.openStatus)

        self.ui = Ui_ModbusBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        self.model = QtGui.QStandardItemModel(1, 3, self)
        self.table = QtWidgets.QTableView(self)
        self.model.setHorizontalHeaderLabels(['registers', 'Hi byte', 'Low byte'])
        self.model.setItem(0,0, QtGui.QStandardItem('0x101'))
        self.model.setItem(0,1, QtGui.QStandardItem('01'))
        self.model.setItem(0,2, QtGui.QStandardItem('00'))
        self.table.setModel(self.model)
        self.ui.value_area.addWidget(self.table, 1, 0, 1, 2)

        self.setComboBox()
    
    def setComboBox(self):
        modes = ['TCP', 'RTU']
        for mode in modes:
            self.ui.mode_comboBox.insertItem(0, mode)
        
        port_list = QSerialPortInfo.availablePorts()
        for port in port_list:
            self.ui.port_comboBox.insertItem(0, port.portName())

        baudrates = ['300', '1200', '2400', '9600', '19200', '115200']
        for baudrate in baudrates:
            self.ui.baudrate_comboBox.insertItem(0, baudrate)
        self.ui.baudrate_comboBox.setCurrentIndex(2)
        
        data_bits = ['5', '6', '7', '8']
        for bit in data_bits:
            self.ui.dataBits_comboBox.insertItem(0, bit)
        self.ui.dataBits_comboBox.setCurrentIndex(0)

        stop_bits = ['1', '1.5', '2']
        for bit in stop_bits:
            self.ui.stopBits_comboBox.insertItem(0, bit)
        self.ui.stopBits_comboBox.setCurrentIndex(0)

        paritys = ['N', 'EVEN', 'ODD', 'MARK', 'SPACE']
        for parity in paritys:
            self.ui.parity_comboBox.insertItem(0, parity)
        self.ui.parity_comboBox.setCurrentIndex(4)

        slave_id = ['1', '2', '3']
        for id in slave_id:
            self.ui.slaveID_comboBox.insertItem(0, id)
        self.ui.slaveID_comboBox.setCurrentIndex(2)

    def open(self):
        mode = self.ui.mode_comboBox.currentText()
        port = os.path.join("/dev", self.ui.port_comboBox.currentText())
        baudrate = int(self.ui.baudrate_comboBox.currentText())
        bytesize = int(self.ui.dataBits_comboBox.currentText())
        stopbits = int(self.ui.stopBits_comboBox.currentText())
        parity = self.ui.parity_comboBox.currentText()
        print(port, baudrate, bytesize)

        self.modbus.openSerial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize,
            stopbits=stopbits,
            parity=parity
        )
    
    def send(self):
        function_code = 0x10
        start_address = int(self.model.data(self.model.index(0, 0)), 16)
        hi_byte = self.model.data(self.model.index(0, 1))
        low_byte = self.model.data(self.model.index(0, 2))
        output_value = [int(hi_byte+low_byte, 16)]
        slave_id = int(self.ui.slaveID_comboBox.currentText())
        print('Start Address:', hex(start_address))
        print('Bytes: ', hi_byte, low_byte, ' -> ', output_value)

        address_bytes = start_address.to_bytes(2, 'big')
        address_bytes = ['{:02x}'.format(x) for x in address_bytes]

        self.modbus.writeData(
            function_code=function_code,
            start_address=start_address,
            output_value=output_value,
            slave_id=slave_id
        )
        
    '''
    def close(self):
        #self.port.closeSerial()
        pass
   
    def clear(self):
        self.ui.recvTextBrowser.clear()
    
    def write(self):
        data = self.ui.sendTextEdit.toPlainText()
        self.modbus.writeData()
    
    def read(self):
        
        data = self.port.readData()
        self.ui.recvTextBrowser.insertPlainText(data)
        self.ui.recvTextBrowser.insertPlainText("\n")
        
        pass
    
    def autoScroll(self):
        text_cursor = self.ui.recvTextBrowser.textCursor()
        text_cursor.movePosition(QtGui.QTextCursor.End)
        self.ui.recvTextBrowser.setTextCursor(text_cursor)
    '''
