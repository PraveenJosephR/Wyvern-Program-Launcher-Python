import base64

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QIcon

from PySide6.QtWidgets import QPushButton

from utils.launcher import launch_app


class LauncherTile(QPushButton):

    removeRequested = Signal(object)

    def __init__(self, title="+", exe_path="", image_data=""):
        super().__init__()

        self.title = title
        self.exe_path = exe_path
        self.image_data = image_data

        self.setObjectName("launcherTile")

        self.setFixedSize(140, 140)
        self.setCursor(Qt.PointingHandCursor)

        if image_data:

            pixmap = QPixmap()
            pixmap.loadFromData(base64.b64decode(image_data))

            self.setIcon(QIcon(pixmap))
            self.setIconSize(self.size())
            self.setText("")

        else:

            self.setText(title)

        if self.exe_path:
            self.clicked.connect(self.launch)

        self.remove_button = QPushButton("×", self)
        self.remove_button.setObjectName("removeButton")
        self.remove_button.setFixedSize(22, 22)
        self.remove_button.move(112, 6)
        self.remove_button.hide()

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