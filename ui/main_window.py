from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QScrollArea,
    QInputDialog,
    QGridLayout,
)

from ui.launcher_tile import LauncherTile


class MainWindow(QMainWindow):

    TILE_COLUMNS = 5

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Software Launcher")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)

        self.build_ui()
        self.add_tab("Home")

    # ----------------------------

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        top = QHBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")

        self.theme_button = QPushButton("🌙")

        self.add_tab_button = QPushButton("+")
        self.add_tab_button.setFixedWidth(40)
        self.add_tab_button.clicked.connect(self.create_new_tab)

        top.addWidget(self.search_bar)
        top.addWidget(self.theme_button)
        top.addWidget(self.add_tab_button)

        layout.addLayout(top)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.remove_tab)

        layout.addWidget(self.tabs)

    # ----------------------------

    def add_tab(self, name):

        page = QWidget()

        page.tiles = []

        page_layout = QVBoxLayout(page)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        page_layout.addWidget(scroll)

        container = QWidget()

        page.grid = QGridLayout(container)
        page.grid.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        page.grid.setHorizontalSpacing(15)
        page.grid.setVerticalSpacing(15)

        scroll.setWidget(container)

        self.tabs.addTab(page, name)

        self.refresh_grid(page)

    # ----------------------------

    def refresh_grid(self, page):

        while page.grid.count():

            item = page.grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        row = 0
        col = 0

        for tile in page.tiles:

            page.grid.addWidget(tile, row, col)

            col += 1

            if col >= self.TILE_COLUMNS:
                col = 0
                row += 1

        plus = LauncherTile("+")
        plus.clicked.connect(lambda: self.add_tile(page))

        page.grid.addWidget(plus, row, col)

    # ----------------------------

    def create_new_tab(self):

        text, ok = QInputDialog.getText(
            self,
            "New Tab",
            "Tab Name:"
        )

        if ok and text.strip():
            self.add_tab(text.strip())

    # ----------------------------

    def remove_tab(self, index):

        if self.tabs.count() == 1:
            return

        self.tabs.removeTab(index)

    # ----------------------------

    def add_tile(self, page):

        from ui.add_app_dialog import AddAppDialog

        dialog = AddAppDialog(self)

        if dialog.exec():

            data = dialog.get_data()

            if not data["title"] or not data["path"]:
                return

            tile = LauncherTile(
                data["title"],
                data["path"]
            )

            page.tiles.append(tile)

            self.refresh_grid(page)