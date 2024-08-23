# Import the generated UI class
from login_ui import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Connect login button click to the function
        self.ui.pushButton_2.clicked.connect(self.handle_login)

    def handle_login(self):
        # Retrieve the text from the line edits
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Implement your login logic
        if username == "test" and password == "test":
            print("Login successful!")
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)  # Set the type of message box (Critical for errors)
            msg_box.setWindowTitle("Login Error")  # Title for the message box
            msg_box.setText("Invalid username or password.")  # Main message to display
            msg_box.setStandardButtons(QMessageBox.Ok)  # Button(s) to show
            msg_box.exec_()

# Instantiate the app and show the window
app = QtWidgets.QApplication([])
window = LoginApp()
window.show()
app.exec_()
