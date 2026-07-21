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
from ui.add_app_dialog import AddAppDialog
from storage.json_storage import load_data, save_data


class MainWindow(QMainWindow):

    TILE_COLUMNS = 5

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Software Launcher")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)

        self.data = load_data()

        self.build_ui()

        if self.data["tabs"]:

            for tab in self.data["tabs"]:
                self.add_tab(tab["name"], tab["tiles"])

        else:

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

    def add_tab(self, name, tiles_data=None):

        if tiles_data is None:
            tiles_data = []

        page = QWidget()

        page.tiles = []

        page_layout = QVBoxLayout(page)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        page_layout.addWidget(scroll)

        container = QWidget()

        page.grid = QGridLayout(container)
        page.grid.setAlignment(
            Qt.AlignmentFlag.AlignTop |
            Qt.AlignmentFlag.AlignLeft
        )

        page.grid.setHorizontalSpacing(15)
        page.grid.setVerticalSpacing(15)

        scroll.setWidget(container)

        for app in tiles_data:

            page.tiles.append(
                LauncherTile(
                    app["title"],
                    app["path"]
                )
            )

        self.tabs.addTab(page, name)

        self.refresh_grid(page)
        
    def save(self):

        tabs = []

        for i in range(self.tabs.count()):

            page = self.tabs.widget(i)

            tiles = []

            for tile in page.tiles:

                tiles.append({
                    "title": tile.title,
                    "path": tile.exe_path
                })

            tabs.append({
                "name": self.tabs.tabText(i),
                "tiles": tiles
            })

        save_data({
            "tabs": tabs
        })

    # ----------------------------

    def refresh_grid(self, page):

        while page.grid.count():

            item = page.grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.setParent(None)

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

            self.save()

    # ----------------------------

    def remove_tab(self, index):

        if self.tabs.count() == 1:
            return

        self.tabs.removeTab(index)

        self.save()

    # ----------------------------

    def add_tile(self, page):

        dialog = AddAppDialog(self)

        if dialog.exec():

            data = dialog.get_data()

            if not data["title"] or not data["path"]:
                return

            page.tiles.append(
                LauncherTile(
                    data["title"],
                    data["path"]
                )
            )

            self.refresh_grid(page)

            self.save()