from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QComboBox,
    QPushButton,
)

from tools.hash_tool import generate_hash


class HashToolPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        # Title

        title = QLabel("Hash Tool")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        # Input

        input_label = QLabel("Text")

        self.input_text = QTextEdit()

        self.input_text.setPlaceholderText("Enter text...")

        # Algorithm

        algorithm_label = QLabel("Algorithm")

        self.algorithm = QComboBox()

        self.algorithm.addItems(
            [
                "md5",
                "sha1",
                "sha224",
                "sha256",
                "sha384",
                "sha512",
            ]
        )

        # Button

        self.generate_button = QPushButton("Generate Hash")

        # Result

        result_label = QLabel("Result")

        self.result = QTextEdit()

        self.result.setReadOnly(True)

        # Layout

        layout.addWidget(title)

        layout.addWidget(input_label)
        layout.addWidget(self.input_text)

        layout.addWidget(algorithm_label)
        layout.addWidget(self.algorithm)

        layout.addWidget(self.generate_button)

        layout.addWidget(result_label)
        layout.addWidget(self.result)

        layout.addStretch()

        # Event

        self.generate_button.clicked.connect(self.generate)

    def generate(self):

        text = self.input_text.toPlainText()

        algorithm = self.algorithm.currentText()

        if not text:
            self.result.setText("Please enter some text.")

            return

        hash_value = generate_hash(text, algorithm)

        if hash_value is None:
            self.result.setText("Invalid algorithm.")

            return

        self.result.setText(hash_value)
