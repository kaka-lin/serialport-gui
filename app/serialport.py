import re
import time
import platform
from PyQt5.QtCore import QObject, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPort

class SerialPort(QObject):
    def __init__(self, port_name=None, parent=None):
        super(SerialPort, self).__init__(parent)

        self.serial = QSerialPort()

        self.port_name = port_name
        self.baud_rate = 9600
        self.data_bits = QSerialPort.Data8
        self.parity = QSerialPort.NoParity
        self.stop_bits = QSerialPort.OneStop
        self.flow_control = QSerialPort.NoFlowControl
    
    def openSerial(self, port_name=None, baud_rate=None):
        if port_name:
            self.port_name = port_name
        
        if baud_rate:
            self.baud_rate = baud_rate

        self.serial.setPortName(self.port_name)
        self.serial.setBaudRate(self.baud_rate)
        self.serial.setDataBits(self.data_bits)
        self.serial.setParity(self.parity)
        self.serial.setStopBits(self.stop_bits)
        self.serial.setFlowControl(self.flow_control)

        if self.serial.open(QIODevice.ReadWrite):
            print("serial open success")
            return True
        else:
            print("serial open fail")
            return False
        
    def closeSerial(self):
        if self.serial.isOpen:
            self.serial.close()

        print("serial close")
    
    def writeData(self, data):
        print("="*50)
        fram_data = bytearray(data, encoding="utf-8")
        print("Write: {}".format(data))
        self.serial.write(fram_data)
        return self.serial.waitForBytesWritten(3000)
    
    def readData(self):
        print("="*50)

        '''
        frame_data = b''
        frame_data = QByteArray(frame_data)
        
        if self.serial.waitForReadyRead(300):
            frame_data = self.serial.readAll()
            print("wait: {}".format(frame_data))
            while self.serial.waitForReadyRead(300):
                frame_data += self.serial.readAll()
                print("while_wait: {}".format(frame_data))
        '''
        
        frame_data = self.serial.readAll()
        frame_data = str(bytes(frame_data.data()), 'utf-8').strip()

        data_list = re.split(r'(?:[\r\n= >])', frame_data)
        data = ''.join(data_list).strip()
        
        print("Read: {}".format(data))
        
        return data
