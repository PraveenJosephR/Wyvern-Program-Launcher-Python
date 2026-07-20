from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class LauncherTile(QPushButton):
    def __init__(self, text="+"):
        super().__init__(text)

        self.setFixedSize(140, 140)
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                border: 2px dashed gray;
                border-radius: 12px;
                font-size: 36px;
                background-color: transparent;
            }

            QPushButton:hover {
                border: 2px solid #3b82f6;
            }
        """)