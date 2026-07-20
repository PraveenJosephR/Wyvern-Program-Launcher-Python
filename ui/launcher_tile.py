from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

from utils.launcher import launch_app


class LauncherTile(QPushButton):

    def __init__(self, title="+", exe_path=""):
        super().__init__(title)

        self.title = title
        self.exe_path = exe_path

        self.setFixedSize(140, 140)
        self.setCursor(Qt.PointingHandCursor)

        self.update_style()

        if self.exe_path:
            self.clicked.connect(self.launch)

    def update_style(self):

        self.setStyleSheet("""
            QPushButton{
                border:2px solid #666;
                border-radius:12px;
                font-size:15px;
                font-weight:bold;
                padding:10px;
                text-align:center;
            }

            QPushButton:hover{
                border:2px solid #3b82f6;
            }
        """)

    def launch(self):
        launch_app(self.exe_path)