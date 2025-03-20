from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QLabel, QApplication, QVBoxLayout, QWidget
import sys
from audio_processing import process_audio, verify_audio

class AudioIntegrityCheckerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Integrity Checker")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Select an audio file:", self)
        layout.addWidget(self.label)

        self.select_button = QPushButton("Browse", self)
        self.select_button.clicked.connect(self.load_audio)
        layout.addWidget(self.select_button)

        self.process_button = QPushButton("Process & Store", self)  # New Button
        self.process_button.clicked.connect(self.process_audio)
        layout.addWidget(self.process_button)

        self.verify_button = QPushButton("Verify Integrity", self)
        self.verify_button.clicked.connect(self.verify_audio)
        layout.addWidget(self.verify_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.file_path = None  # Initialize file_path attribute

    def load_audio(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "samples/", "Audio Files (*.wav *.mp3)")
        if file_path:
            self.file_path = file_path
            self.label.setText(f"Loaded: {file_path}")

    def process_audio(self):
        """Process and store hash of selected audio file"""
        if self.file_path:
            process_audio(self.file_path)
            self.label.setText("Audio processed and stored!")
        else:
            self.label.setText("No file selected.")

    def verify_audio(self):
        """Verify audio integrity by comparing stored hash"""
        if self.file_path:
            is_valid = verify_audio(self.file_path)
            self.label.setText("Audio is Valid" if is_valid else "Integrity Check Failed")
        else:
            self.label.setText("No file selected.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioIntegrityCheckerGUI()
    window.show()
    sys.exit(app.exec())
