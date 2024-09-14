from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cow Registration")
        self.setGeometry(100, 100, 400, 400)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Main layout (vertical)
        layout = QVBoxLayout()

        # Input for cow color
        color_layout = QHBoxLayout()
        self.label = QLabel("Enter Cow Color (white, brown, pink):")
        self.input_color = QLineEdit()
        color_layout.addWidget(self.label)
        color_layout.addWidget(self.input_color)
        layout.addLayout(color_layout)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_color)
        layout.addWidget(self.submit_button)

        # Error message label
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red")
        layout.addWidget(self.error_label)

        # TextEdit for displaying farm summary
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        layout.addWidget(self.summary_text)
        self.summary_text.hide()  # Hidden by default

        # Set the layout to the central widget
        central_widget.setLayout(layout)

    def set_controller(self, controller):
        self.controller = controller

    def submit_color(self):
        color = self.input_color.text()
        self.controller.handle_color_submission(color)

    def show_error_message(self, message):
        self.error_label.setText(message)

    def show_summary(self, summary):
        self.summary_text.setText(summary)
        self.summary_text.show()
        self.error_label.clear()  # Clear error message when showing summary
