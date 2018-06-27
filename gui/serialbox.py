import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui.ui_serialbox import Ui_SerialBox

class SerialBox(QtWidgets.QGroupBox):
    """ Serial number edit box """
    def __init__(self, parent=None):
        super(SerialBox, self).__init__(parent)

        self.ui = Ui_SerialBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
