from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
)

from ui.dashboard_page import DashboardPage
from ui.port_scanner_page import PortScannerPage
from ui.hash_tool_page import HashToolPage
from ui.ip_lookup_page import IPLookupPage
from ui.settings_page import SettingsPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Security Toolkit")
        self.resize(1100, 700)

        self.setup_ui()

    def setup_ui(self):

        main_layout = QHBoxLayout(self)

        # =========================
        # Sidebar
        # =========================

        sidebar = QVBoxLayout()

        title = QLabel("🛡 Security Toolkit")

        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            padding: 15px;
        """)

        self.dashboard_button = QPushButton("Dashboard")
        self.port_button = QPushButton("Port Scanner")
        self.hash_button = QPushButton("Hash Tool")
        self.ip_button = QPushButton("IP Lookup")
        self.settings_button = QPushButton("Settings")

        sidebar.addWidget(title)

        sidebar.addWidget(self.dashboard_button)
        sidebar.addWidget(self.port_button)
        sidebar.addWidget(self.hash_button)
        sidebar.addWidget(self.ip_button)

        sidebar.addStretch()

        sidebar.addWidget(self.settings_button)

        # =========================
        # Pages
        # =========================

        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.port_page = PortScannerPage()
        self.hash_page = HashToolPage()
        self.ip_page = IPLookupPage()
        self.settings_page = SettingsPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.port_page)
        self.pages.addWidget(self.hash_page)
        self.pages.addWidget(self.ip_page)
        self.pages.addWidget(self.settings_page)

        # =========================
        # Navigation
        # =========================

        self.dashboard_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.dashboard_page)
        )

        self.port_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.port_page)
        )

        self.hash_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.hash_page)
        )

        self.ip_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.ip_page)
        )

        self.settings_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.settings_page)
        )

        # =========================
        # Layout
        # =========================

        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.pages, 4)
