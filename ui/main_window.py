from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Software Launcher")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)

        self.build_ui()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # ----------------------------
        # Top Bar
        # ----------------------------

        top_bar = QHBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")

        self.theme_button = QPushButton("🌙")

        top_bar.addWidget(self.search_bar)
        top_bar.addWidget(self.theme_button)

        main_layout.addLayout(top_bar)

        # ----------------------------
        # Tabs
        # ----------------------------

        self.tabs = QTabWidget()

        home_page = QWidget()
        self.tabs.addTab(home_page, "Home")

        main_layout.addWidget(self.tabs)

        # ----------------------------
        # Home Layout
        # ----------------------------

        home_layout = QVBoxLayout(home_page)
        home_layout.setContentsMargins(10, 10, 10, 10)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        home_layout.addWidget(self.scroll)

        container = QWidget()
        self.scroll.setWidget(container)

        self.tile_layout = QHBoxLayout(container)
        self.tile_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tile_layout.setSpacing(15)

        # Temporary placeholder tile
        placeholder = QLabel("➕")
        placeholder.setFixedSize(140, 140)
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("""
            QLabel{
                border:2px dashed gray;
                border-radius:12px;
                font-size:36px;
            }
        """)

        self.tile_layout.addWidget(placeholder)