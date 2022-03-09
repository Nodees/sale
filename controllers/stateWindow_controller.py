from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.state import Ui_states


class sateWindowController(QWidget, Ui_states):
    def __init__(self, parent=None):
        super(sateWindowController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_state.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_state.text()
        abbreviation = self.abbreviation.text()

        obj = {
            'name': name,
            'abbreviation': abbreviation
        }

        insert_function('state', obj)