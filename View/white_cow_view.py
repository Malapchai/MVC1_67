from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QFormLayout, QWidget

class WhiteCowView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("White Cow Registration")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()

        self.input_id = QLineEdit()
        form_layout.addRow(QLabel("Cow ID (8 digits):"), self.input_id)

        self.input_farm_id = QLineEdit()
        form_layout.addRow(QLabel("Farm ID (1 digit):"), self.input_farm_id)

        self.input_years = QLineEdit()
        form_layout.addRow(QLabel("Age (Years):"), self.input_years)

        self.input_months = QLineEdit()
        form_layout.addRow(QLabel("Age (Months):"), self.input_months)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red")
        form_layout.addRow(self.error_label)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_data)
        form_layout.addWidget(self.submit_button)

        central_widget.setLayout(form_layout)

    def submit_data(self):
        cow_id = self.input_id.text()
        farm_id = self.input_farm_id.text()
        years = self.input_years.text()
        months = self.input_months.text()
        self.controller.submit_white_cow(cow_id, farm_id, years, months)

    def show_error_message(self, message):
        self.error_label.setText(message)