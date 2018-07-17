import platform

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

class KModbus(QObject):
    openFinishSig = pyqtSignal(str)

    def __init__(self, parent=None):
        super(KModbus, self).__init__(parent)

        self.cst = cst
        self.error =  modbus_tk.modbus.ModbusError

        self.master = None
    
    def openSerial(self, port=None, baudrate=9600, bytesize=8, parity='N', stopbits=2, xonxoff=0):
        if port == None:
            if platform.system() == "Linux":
                self.port = "/dev/ttyAMA0"
        else:
            self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.xonxoff = xonxoff

        self.master =  modbus_rtu.RtuMaster(
            serial.Serial(
                port=self.port, 
                baudrate=self.baudrate,
                bytesize=self.bytesize,
                parity=self.parity,
                stopbits=self.stopbits,
                xonxoff=self.xonxoff
            )
        )

        self.master.set_timeout(5.0)
        self.master.set_verbose(True)
        logger.info("connected")
        self.openFinishSig.emit("Connected!")

    def writeData(self, function_code=0x10, start_address=0x101, output_value=1, slave_id=1):
        self.master.execute(slave_id, function_code, start_address, output_value=output_value)
