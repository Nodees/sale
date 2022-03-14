import sys

from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import QApplication


from controllers.mainWindow_controller import MainWindowController

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

app = QApplication(sys.argv)

main = MainWindowController()
main.show()

sys.exit(app.exec_())
