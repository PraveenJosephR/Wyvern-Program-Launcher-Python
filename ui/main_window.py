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
    QMessageBox
)
import math
from ui.launcher_tile import LauncherTile
from ui.add_app_dialog import AddAppDialog
from storage.json_storage import load_data, save_data
from assets.themes.themes import DARK, LIGHT
import json
import os

class MainWindow(QMainWindow):

    TILE_COLUMNS = 5

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wyvern")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)

        self.data = load_data()

        self.build_ui()
        self.load_theme()
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

        self.theme_button = QPushButton()
        self.theme_button.setFixedWidth(75)
        self.theme_button.clicked.connect(self.toggle_theme)

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
        page.scroll = scroll
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

            tile = LauncherTile(
                app["title"],
                app["path"]
            )

            tile.removeRequested.connect(
                lambda t, p=page: self.remove_tile(p, t)
            )

            page.tiles.append(tile)

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

        viewport_width = page.scroll.viewport().width()

        tile_width = 140
        spacing = page.grid.horizontalSpacing()

        columns = max(
            1,
            math.floor(
                (viewport_width + spacing) /
                (tile_width + spacing)
            )
        )

        for tile in page.tiles:

            page.grid.addWidget(tile, row, col)

            col += 1

            if col >= columns:
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

        tab_name = self.tabs.tabText(index)

        reply = QMessageBox.question(
            self,
            "Delete Tab",
            f"Delete tab '{tab_name}' and all its tiles?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
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

            tile = LauncherTile(
                data["title"],
                data["path"]
            )

            tile.removeRequested.connect(
                lambda t, p=page: self.remove_tile(p, t)
            )

            page.tiles.append(tile)

            self.refresh_grid(page)

            self.save()

    def remove_tile(self, page, tile):

        reply = QMessageBox.question(
            self,
            "Delete Tile",
            f"Delete '{tile.title}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        if tile in page.tiles:

            page.tiles.remove(tile)

            self.refresh_grid(page)

            self.save()

    def resizeEvent(self, event):

        super().resizeEvent(event)

        for i in range(self.tabs.count()):

            page = self.tabs.widget(i)

            self.refresh_grid(page)

    def refresh_all_grids(self):

        for i in range(self.tabs.count()):

            page = self.tabs.widget(i)

            self.refresh_grid(page)

    def showEvent(self, event):

        super().showEvent(event)

        self.refresh_all_grids()

    def load_theme(self):

        settings_file = "data/settings.json"

        if os.path.exists(settings_file):

            with open(settings_file, "r", encoding="utf-8") as f:
                settings = json.load(f)

        else:

            settings = {"theme": "dark"}

        self.current_theme = settings.get("theme", "dark")

        self.apply_theme()


    def apply_theme(self):

        if self.current_theme == "dark":

            self.setStyleSheet(DARK)
            self.theme_button.setText("☀")

        else:

            self.setStyleSheet(LIGHT)
            self.theme_button.setText("🌙")


    def toggle_theme(self):

        self.current_theme = (
            "light"
            if self.current_theme == "dark"
            else "dark"
        )

        self.apply_theme()

        settings_file = "data/settings.json"

        if os.path.exists(settings_file):

            with open(settings_file, "r", encoding="utf-8") as f:
                settings = json.load(f)

        else:

            settings = {}

        settings["theme"] = self.current_theme

        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)