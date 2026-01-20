import sys
import string
import secrets

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QCheckBox, QMessageBox, QSpinBox
)
from PyQt5.QtCore import Qt


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✨ Advanced Password Generator ✨")
        self.setGeometry(300, 200, 500, 400)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("🔐 Secure Password Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(title)

        # Length
        length_layout = QHBoxLayout()
        length_label = QLabel("Password Length:")
        length_label.setStyleSheet("color: #E0E0E0; font-size: 14px;")
        length_layout.addWidget(length_label)

        self.length_input = QSpinBox()
        self.length_input.setRange(8, 64)
        self.length_input.setValue(12)
        self.length_input.setStyleSheet("""
            QSpinBox {
                background-color: rgba(255,255,255,0.1);
                color: #FFFFFF;
                border: 1px solid #888;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
            }
        """)
        length_layout.addWidget(self.length_input)
        layout.addLayout(length_layout)

        # Character options
        self.upper_cb = QCheckBox("Uppercase (A-Z)")
        self.lower_cb = QCheckBox("Lowercase (a-z)")
        self.digit_cb = QCheckBox("Digits (0-9)")
        self.symbol_cb = QCheckBox("Symbols (!@#$...)")

        for cb in [self.upper_cb, self.lower_cb, self.digit_cb, self.symbol_cb]:
            cb.setStyleSheet("color: #FFFFFF; font-size: 14px;")
            layout.addWidget(cb)

        self.upper_cb.setChecked(True)
        self.lower_cb.setChecked(True)
        self.digit_cb.setChecked(True)

        # Exclude characters
        exclude_label = QLabel("Exclude Characters:")
        exclude_label.setStyleSheet("color: #E0E0E0; font-size: 14px;")
        layout.addWidget(exclude_label)

        self.exclude_input = QLineEdit()
        self.exclude_input.setPlaceholderText("e.g. O0l1")
        self.exclude_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,0.1);
                color: #00FFAA;
                border-radius: 8px;
                border: 1px solid #888;
                padding: 8px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.exclude_input)

        # Generate button
        self.generate_btn = QPushButton("🚀 Generate Password")
        self.generate_btn.clicked.connect(self.generate_password)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #6B5BFF, stop:1 #8A75FF);
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 12px;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #8A75FF, stop:1 #6B5BFF);
            }
        """)
        layout.addWidget(self.generate_btn)

        # Output
        self.result = QLineEdit()
        self.result.setReadOnly(True)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                font-weight: bold;
                color: #FFD166;
                background-color: rgba(255,255,255,0.05);
                border-radius: 12px;
                border: 1px solid #555;
                padding: 10px;
            }
        """)
        layout.addWidget(self.result)

        # Copy button
        self.copy_btn = QPushButton("📋 Copy to Clipboard")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #4ADE80;
                color: #1E1F28;
                font-size: 16px;
                font-weight: bold;
                border-radius: 12px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #22C55E;
            }
        """)
        layout.addWidget(self.copy_btn)

        # Apply modern background
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #1E1F28, stop:1 #2C2F48);
            }
        """)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def generate_password(self):
        length = self.length_input.value()
        exclude = set(self.exclude_input.text())

        pools = []
        password = []

        if self.upper_cb.isChecked():
            pool = set(string.ascii_uppercase) - exclude
            if pool:
                pools.append(list(pool))
                password.append(secrets.choice(list(pool)))

        if self.lower_cb.isChecked():
            pool = set(string.ascii_lowercase) - exclude
            if pool:
                pools.append(list(pool))
                password.append(secrets.choice(list(pool)))

        if self.digit_cb.isChecked():
            pool = set(string.digits) - exclude
            if pool:
                pools.append(list(pool))
                password.append(secrets.choice(list(pool)))

        if self.symbol_cb.isChecked():
            pool = set(string.punctuation) - exclude
            if pool:
                pools.append(list(pool))
                password.append(secrets.choice(list(pool)))

        if not pools:
            QMessageBox.warning(self, "Error", "Select at least one character type.")
            return

        if length < len(password):
            QMessageBox.warning(self, "Error", "Password length too short for selected rules.")
            return

        all_chars = [c for pool in pools for c in pool]

        while len(password) < length:
            password.append(secrets.choice(all_chars))

        secrets.SystemRandom().shuffle(password)
        self.result.setText("".join(password))

    def copy_to_clipboard(self):
        if self.result.text():
            QApplication.clipboard().setText(self.result.text())
            QMessageBox.information(self, "Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PasswordGenerator()
    win.show()
    sys.exit(app.exec_())
