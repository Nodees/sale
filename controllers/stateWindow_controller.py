from PyQt5.QtWidgets import QWidget
from views_py.state import Ui_states


class sateWindowController(QWidget, Ui_states):
    def __init__(self, parent=None):
        super(sateWindowController, self).__init__(parent=parent)
        self.setupUi(self)
