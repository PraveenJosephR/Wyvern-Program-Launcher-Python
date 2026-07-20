from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Software Launcher")
        self.resize(1200, 750)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        title = QLabel("Software Launcher")
        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                padding: 30px;
            }
        """)

        layout.addWidget(title)