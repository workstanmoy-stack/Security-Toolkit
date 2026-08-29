from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        description = QLabel("Welcome to your security and developer toolkit.")

        description.setStyleSheet("""
            font-size: 17px;
        """)

        tools = QLabel(
            """
            Available Tools:

            • Port Scanner
            • Hash Generator
            • IP Lookup

            More tools will be added later.
            """
        )

        tools.setStyleSheet("""
            font-size: 16px;
            padding-top: 20px;
        """)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(tools)

        layout.addStretch()
