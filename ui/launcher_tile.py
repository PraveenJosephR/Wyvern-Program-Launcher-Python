from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton

from utils.launcher import launch_app


class LauncherTile(QPushButton):

    removeRequested = Signal(object)

    def __init__(self, title="+", exe_path=""):
        super().__init__(title)

        self.title = title
        self.exe_path = exe_path

        self.setFixedSize(140, 140)
        self.setCursor(Qt.PointingHandCursor)

        self.setObjectName("launcherTile")

        if self.exe_path:
            self.clicked.connect(self.launch)

        self.remove_button = QPushButton("×", self)
        self.remove_button.setObjectName("removeButton")
        self.remove_button.setFixedSize(22, 22)
        self.remove_button.move(112, 6)
        self.remove_button.hide()

        self.remove_button.setStyleSheet("""
            QPushButton{
                background:#d9534f;
                color:white;
                border:none;
                border-radius:11px;
                font-size:12px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#c9302c;
            }
        """)

        self.remove_button.clicked.connect(self.remove_tile)

    def enterEvent(self, event):
        if self.exe_path:
            self.remove_button.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.remove_button.hide()
        super().leaveEvent(event)

    def remove_tile(self):
        self.removeRequested.emit(self)

    def launch(self):
        launch_app(self.exe_path)