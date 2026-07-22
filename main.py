import sys

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from PySide6.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/app.ico"))
    window = MainWindow()
    window.setWindowIcon(QIcon("resources/app.ico"))
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

    # build call ----> pyinstaller --onefile --windowed --icon=resources/app.ico main.py