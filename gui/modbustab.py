from PyQt5 import QtCore, QtGui, QtWidgets
from gui.modbusbox import ModbusBox

class ModbusTab(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super(ModbusTab, self).__init__(parent)

        self.modbus_box = ModbusBox()

        self.addWidget(self.modbus_box)
      
        self._setup_ui()
    
    def _setup_ui(self):
        self.retranslateUi()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
