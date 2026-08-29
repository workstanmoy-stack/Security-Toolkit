from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)

from tools.port_scanner import scan_ports


class PortScannerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        # Title

        title = QLabel("Port Scanner")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        # Target

        target_label = QLabel("Target")

        self.target_input = QLineEdit()

        self.target_input.setPlaceholderText("Your IP address or authorized hostname")

        # Ports

        ports_label = QLabel("Ports")

        self.ports_input = QLineEdit()

        self.ports_input.setPlaceholderText("Example: 22,80,443")

        # Button

        self.scan_button = QPushButton("Scan")

        # Results

        results_label = QLabel("Results")

        self.results = QTextEdit()

        self.results.setReadOnly(True)

        # Layout

        layout.addWidget(title)

        layout.addWidget(target_label)
        layout.addWidget(self.target_input)

        layout.addWidget(ports_label)
        layout.addWidget(self.ports_input)

        layout.addWidget(self.scan_button)

        layout.addWidget(results_label)
        layout.addWidget(self.results)

        # Event

        self.scan_button.clicked.connect(self.start_scan)

    def start_scan(self):

        target = self.target_input.text().strip()

        ports_text = self.ports_input.text().strip()

        if not target:
            self.results.setText("Please enter a target.")

            return

        if not ports_text:
            self.results.setText("Please enter ports.")

            return

        try:
            ports = [int(port.strip()) for port in ports_text.split(",")]

            if any(port < 1 or port > 65535 for port in ports):
                raise ValueError

        except ValueError:
            self.results.setText("Ports must be numbers between 1 and 65535.")

            return

        self.results.setText("Scanning authorized target...")

        results = scan_ports(target, ports)

        output = ""

        for port, status in results:
            output += f"Port {port}: {status}\n"

        self.results.setText(output)
