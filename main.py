import sys
import os

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)

# Load stylesheet
style_path = resource_path("styles/theme.qss")

with open(style_path, "r", encoding="utf-8") as file:
    app.setStyleSheet(file.read())


# Create main window
window = MainWindow()
window.show()


# Tell PyInstaller splash screen to close
if getattr(sys, "frozen", False):
    import pyi_splash

    pyi_splash.close()


sys.exit(app.exec())
