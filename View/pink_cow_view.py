from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QFormLayout, QWidget

class PinkCowView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Pink Cow Registration")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Form layout
        form_layout = QFormLayout()

        # Cow ID
        self.input_id = QLineEdit()
        form_layout.addRow(QLabel("Cow ID (8 digits):"), self.input_id)

        # Farm ID
        self.input_farm_id = QLineEdit()
        form_layout.addRow(QLabel("Farm ID (1 digit):"), self.input_farm_id)

        # Owner's First Name
        self.input_first_name = QLineEdit()
        form_layout.addRow(QLabel("Owner's First Name:"), self.input_first_name)

        # Owner's Last Name
        self.input_last_name = QLineEdit()
        form_layout.addRow(QLabel("Owner's Last Name:"), self.input_last_name)

        # Error message label
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red")
        form_layout.addRow(self.error_label)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_data)
        form_layout.addWidget(self.submit_button)

        # Set the layout to the central widget
        central_widget.setLayout(form_layout)

    def submit_data(self):
        cow_id = self.input_id.text()
        farm_id = self.input_farm_id.text()
        first_name = self.input_first_name.text()
        last_name = self.input_last_name.text()
        self.controller.submit_pink_cow(cow_id, farm_id, first_name, last_name)

    def show_error_message(self, message):
        self.error_label.setText(message)
