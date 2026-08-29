from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QCheckBox,
)


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Settings")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        dark_mode = QCheckBox("Dark Mode")

        dark_mode.setEnabled(False)

        information = QLabel("Settings will be implemented later.")

        layout.addWidget(title)
        layout.addWidget(dark_mode)
        layout.addWidget(information)

        layout.addStretch()
