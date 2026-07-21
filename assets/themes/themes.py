DARK = """
QMainWindow, QWidget {
    background-color: #202124;
    color: white;
}

/* Search */

QLineEdit {
    background: #2b2d31;
    border: 1px solid #4b4b4b;
    border-radius: 8px;
    padding: 6px;
    color: white;
}

/* Normal Buttons */

QPushButton {
    background: #2b2d31;
    border: 1px solid #555;
    border-radius: 8px;
    padding: 6px;
    color: white;
}

QPushButton:hover {
    background: #3a3d42;
}

/* Launcher Tiles */

QPushButton#launcherTile {
    background: #2b2d31;
    border: 2px solid #555;
    border-radius: 12px;
    font-size: 15px;
    font-weight: bold;
    padding: 10px;
    text-align: center;
}

QPushButton#launcherTile:hover {
    border: 2px solid #4da3ff;
}

/* Remove Button */

QPushButton#removeButton {
    background: #d9534f;
    color: white;
    border: none;
    border-radius: 11px;
    font-size: 12px;
    font-weight: bold;
}

QPushButton#removeButton:hover {
    background: #c9302c;
}

/* Tabs */

QTabWidget::pane {
    border: none;
}

QTabBar::tab {
    background: #2b2d31;
    border: 1px solid #555;
    padding: 8px 16px;
    margin-right: 2px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

QTabBar::tab:selected {
    background: #3a3d42;
}

QScrollArea {
    border: none;
}
"""


LIGHT = """
QMainWindow, QWidget {
    background-color: #f4f4f4;
    color: black;
}

/* Search */

QLineEdit {
    background: white;
    border: 1px solid #bfbfbf;
    border-radius: 8px;
    padding: 6px;
    color: black;
}

/* Normal Buttons */

QPushButton {
    background: white;
    border: 1px solid #bfbfbf;
    border-radius: 8px;
    padding: 6px;
    color: black;
}

QPushButton:hover {
    background: #e8e8e8;
}

/* Launcher Tiles */

QPushButton#launcherTile {
    background: white;
    border: 2px solid #bfbfbf;
    border-radius: 12px;
    font-size: 15px;
    font-weight: bold;
    padding: 10px;
    text-align: center;
}

QPushButton#launcherTile:hover {
    border: 2px solid #2196f3;
}

/* Remove Button */

QPushButton#removeButton {
    background: #d9534f;
    color: white;
    border: none;
    border-radius: 11px;
    font-size: 12px;
    font-weight: bold;
}

QPushButton#removeButton:hover {
    background: #c9302c;
}

/* Tabs */

QTabWidget::pane {
    border: none;
}

QTabBar::tab {
    background: #dddddd;
    border: 1px solid #bfbfbf;
    padding: 8px 16px;
    margin-right: 2px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

QTabBar::tab:selected {
    background: white;
}

QScrollArea {
    border: none;
}
"""