from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class AddAppDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Application")
        self.setFixedWidth(500)

        self.title_edit = QLineEdit()

        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)

        browse_button = QPushButton("Browse...")
        browse_button.clicked.connect(self.browse)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(browse_button)

        form = QFormLayout()
        form.addRow("Title", self.title_edit)
        form.addRow("Executable", path_layout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(cancel_button)
        buttons.addWidget(save_button)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(buttons)

    def browse(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Executable",
            "",
            "Applications (*.exe)"
        )

        if path:
            self.path_edit.setText(path)

    def get_data(self):

        return {
            "title": self.title_edit.text().strip(),
            "path": self.path_edit.text().strip(),
        }