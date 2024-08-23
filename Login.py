from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi('Login.ui')

dlg.setFixedSize(1400,900)
dlg.show()
app.exec()
