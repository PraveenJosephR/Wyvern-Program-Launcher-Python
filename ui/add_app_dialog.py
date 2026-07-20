from PySide6.QtWidgets import QDialog


class AddAppDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Application")
        self.resize(400, 250)