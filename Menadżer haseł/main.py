from PyQt6.QtWidgets import QApplication
from ui import PasswordManagerUI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerUI()
    window.show()
    sys.exit(app.exec())