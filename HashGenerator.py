from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QTextEdit, QRadioButton, QButtonGroup
)
from PySide6.QtGui import QFont
from qdarkstyle import load_stylesheet_pyside6
from PySide6.QtCore import Qt
import sys
import hashlib

class HashGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Generator")
        self.setMinimumSize(500, 400)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        central.setLayout(main_layout)

        card = QWidget()
        card_layout = QVBoxLayout()
        card_layout.setSpacing(18)
        card_layout.setContentsMargins(32, 32, 32, 32)
        card.setLayout(card_layout)
        card.setObjectName("card")

        title = QLabel("Hash Generator")
        title.setFont(QFont("Segoe UI", 26, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")
        card_layout.addWidget(title)

        radio_layout = QHBoxLayout()
        radio_layout.setSpacing(16)
        radio_layout.setAlignment(Qt.AlignCenter)
        self.file_radio = QRadioButton("File")
        self.string_radio = QRadioButton("String")
        self.string_radio.setChecked(True)
        radio_layout.addWidget(self.file_radio)
        radio_layout.addWidget(self.string_radio)
        card_layout.addLayout(radio_layout)

        file_layout = QHBoxLayout()
        file_layout.setSpacing(8)
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Select file...")
        self.file_input.setEnabled(False)
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.setEnabled(False)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(self.browse_btn)
        card_layout.addLayout(file_layout)

        self.string_input = QLineEdit()
        self.string_input.setPlaceholderText("Enter text to hash...")
        card_layout.addWidget(self.string_input)

        algo_layout = QHBoxLayout()
        algo_layout.setSpacing(8)
        algo_layout.setAlignment(Qt.AlignCenter)
        algo_label = QLabel("Algorithm:")
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(["md5", "sha1", "sha224", "sha256", "sha384", "sha512"])
        algo_layout.addWidget(algo_label)
        algo_layout.addWidget(self.algo_combo)
        card_layout.addLayout(algo_layout)

        self.hash_btn = QPushButton("Generate Hash")
        self.hash_btn.setMinimumHeight(36)
        self.hash_btn.setObjectName("hashBtn")
        card_layout.addWidget(self.hash_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setMinimumHeight(60)
        self.output.setObjectName("outputBox")
        card_layout.addWidget(self.output)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)

        self.file_radio.toggled.connect(self.toggle_input)
        self.browse_btn.clicked.connect(self.browse_file)
        self.hash_btn.clicked.connect(self.generate_hash)

        self.setStyleSheet('''
            #card {
                background: #23272e;
                border-radius: 18px;
                border: 1.5px solid #3a3f4b;
                box-shadow: 0 4px 24px 0 rgba(0,0,0,0.18);
            }
            #title {
                color: #6cb4ff;
                letter-spacing: 1px;
            }
            QLineEdit, QComboBox, QTextEdit {
                border-radius: 8px;
                border: 1.2px solid #3a3f4b;
                padding: 7px 10px;
                background: #23272e;
                color: #e0e0e0;
                font-size: 15px;
            }
            QLineEdit:disabled {
                background: #181a1f;
                color: #888;
            }
            QRadioButton {
                font-size: 15px;
                color: #b0b8c1;
            }
            #hashBtn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6cb4ff, stop:1 #4f8cff);
                color: white;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 8px;
            }
            #hashBtn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4f8cff, stop:1 #6cb4ff);
            }
            #outputBox {
                background: #181a1f;
                color: #6cb4ff;
                font-size: 16px;
                border-radius: 8px;
                border: 1.2px solid #3a3f4b;
            }
        ''')

    def toggle_input(self):
        if self.file_radio.isChecked():
            self.file_input.setEnabled(True)
            self.browse_btn.setEnabled(True)
            self.string_input.setEnabled(False)
        else:
            self.file_input.setEnabled(False)
            self.browse_btn.setEnabled(False)
            self.string_input.setEnabled(True)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_input.setText(file_path)

    def generate_hash(self):
        algo = self.algo_combo.currentText()
        if self.file_radio.isChecked():
            file_path = self.file_input.text()
            if not file_path:
                self.output.setText("Please select a file.")
                return
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
            except Exception as e:
                self.output.setText(f"Error: {e}")
                return
        else:
            data = self.string_input.text().encode()
            if not data:
                self.output.setText("Please enter text.")
                return
        try:
            hash_func = getattr(hashlib, algo)
            hash_value = hash_func(data).hexdigest()
            self.output.setText(hash_value)
        except Exception as e:
            self.output.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet_pyside6())
    window = HashGeneratorUI()
    window.show()
    sys.exit(app.exec())
