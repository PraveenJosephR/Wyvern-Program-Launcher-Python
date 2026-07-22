import base64
import io

from PIL import Image

from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)


class AddAppDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Application")
        self.setFixedWidth(500)

        self.image_data = ""

        self.title_edit = QLineEdit()

        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)

        exe_button = QPushButton("Browse...")
        exe_button.clicked.connect(self.browse_exe)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(exe_button)

        self.image_edit = QLineEdit()
        self.image_edit.setReadOnly(True)

        image_button = QPushButton("Browse...")
        image_button.clicked.connect(self.browse_image)

        image_layout = QHBoxLayout()
        image_layout.addWidget(self.image_edit)
        image_layout.addWidget(image_button)

        note = QLabel(
            "Please upload a square image.\n"
            "Recommended: 512×512 or larger."
        )

        form = QFormLayout()
        form.addRow("Title", self.title_edit)
        form.addRow("Executable", path_layout)
        form.addRow("Thumbnail", image_layout)
        form.addRow("", note)

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

    def browse_exe(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Executable",
            "",
            "Applications (*.exe)"
        )

        if path:
            self.path_edit.setText(path)

    def browse_image(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Thumbnail",
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )

        if not path:
            return

        image = Image.open(path)

        if image.width != image.height:

            QMessageBox.warning(
                self,
                "Invalid Image",
                "Please select a square image."
            )

            return

        image = image.resize((256, 256), Image.Resampling.LANCZOS)

        buffer = io.BytesIO()

        image.save(buffer, format="PNG")

        self.image_data = base64.b64encode(
            buffer.getvalue()
        ).decode("utf-8")

        self.image_edit.setText(path)

    def get_data(self):

        return {
            "title": self.title_edit.text().strip(),
            "path": self.path_edit.text().strip(),
            "image": self.image_data,
        }