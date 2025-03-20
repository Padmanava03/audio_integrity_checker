from gui import AudioIntegrityCheckerGUI
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioIntegrityCheckerGUI()
    window.show()
    sys.exit(app.exec())
