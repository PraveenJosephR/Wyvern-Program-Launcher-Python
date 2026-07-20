import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, setTheme, Theme
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    # Use dark theme for now
    setTheme(Theme.DARK)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()