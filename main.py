from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
MAIN_WINDOW_TITLE = "(НАЗВАНИЕ ПРОЕКТА)"
LINE_EDIT_MAIN_WINDOW_PLACEHOLDER = "Искать..."
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        leSearch = QLineEdit()
        lhHeading = QHBoxLayout()
        lvBackground = QVBoxLayout()
        pbMenu = QPushButton()
        wBackground = QWidget()
        wBottom = QWidget()
        wHeading = QWidget()
        lvBackground.addWidget(wHeading)
        lvBackground.addWidget(wBottom)
        lvBackground.setSpacing(0)
        wBackground.setLayout(lvBackground)
        lhHeading.addWidget(pbMenu, alignment=Qt.AlignTop)
        lhHeading.addWidget(leSearch, alignment=Qt.AlignTop)
        wHeading.setLayout(lhHeading)
        self.resize(1200, 900)
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setCentralWidget(wBackground)
        wHeading.setStyleSheet("border-bottom: 3px solid black; background-color: gray;")
        wBottom.setStyleSheet("background-color: darkGray;")
        pbMenu.setStyleSheet("background-color: dimGray; border: 3px solid black; border-radius: 40px; height: 80px; width: 80px;")
        leSearch.setStyleSheet("background-color: darkGray; border: 3px solid black; border-radius: 40px; font-size: 64px; height: 80px; padding-left: 20px")
        leSearch.setPlaceholderText(LINE_EDIT_MAIN_WINDOW_PLACEHOLDER)
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
