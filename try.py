import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class PayrollSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payroll System")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.label = QLabel("Employee Name:", self)
        self.label.move(20, 20)

        self.name_input = QLineEdit(self)
        self.name_input.move(150, 20)

        self.add_button = QPushButton("Add Employee", self)
        self.add_button.move(300, 20)
        self.add_button.clicked.connect(self.add_employee)

        self.table = QTableWidget(self)
        self.table.setGeometry(20, 80, 760, 480)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Salary"])

    def add_employee(self):
        name = self.name_input.text()
        # Add logic to save employee data to database or list
        # For now, just add a row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, QTableWidgetItem("$5000"))
    
    def delete_employee(self):
        pass
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PayrollSystemApp()
    window.show()
    sys.exit(app.exec_())
