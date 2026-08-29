from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)

from tools.ip_lookup import lookup_ip


class IPLookupPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        # Title

        title = QLabel("IP Lookup")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        # Hostname

        hostname_label = QLabel("Hostname")

        self.hostname_input = QLineEdit()

        self.hostname_input.setPlaceholderText("Example: example.com")

        # Button

        self.lookup_button = QPushButton("Lookup")

        # Result

        result_label = QLabel("Result")

        self.result = QTextEdit()

        self.result.setReadOnly(True)

        # Layout

        layout.addWidget(title)

        layout.addWidget(hostname_label)
        layout.addWidget(self.hostname_input)

        layout.addWidget(self.lookup_button)

        layout.addWidget(result_label)
        layout.addWidget(self.result)

        layout.addStretch()

        # Event

        self.lookup_button.clicked.connect(self.lookup)

    def lookup(self):

        hostname = self.hostname_input.text().strip()

        if not hostname:
            self.result.setText("Please enter a hostname.")

            return

        ip = lookup_ip(hostname)

        if ip is None:
            self.result.setText("Could not resolve hostname.")

            return

        self.result.setText(f"Hostname: {hostname}\nIP Address: {ip}")
