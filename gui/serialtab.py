from PyQt5 import QtCore, QtGui, QtWidgets
from gui.serialbox import SerialBox

class SerialTab(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super(SerialTab, self).__init__(parent)

        self.serial_box = SerialBox()

        self.addWidget(self.serial_box)
      
        self._setup_ui()
    
    def _setup_ui(self):
        self.retranslateUi()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
