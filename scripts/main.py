from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFontDatabase, QIcon, QPixmap
from PyQt5.QtWidgets import *
import json
ICON_MAIN_MENU = "data\\icons\\main_menu.png"
ICON_MAIN_PROFILE = "data\\icons\\main_profile.png"
MAIN_WINDOW_TITLE = "(НАЗВАНИЕ ПРОЕКТА)"
LABEL_BODY_HEADER_TEXT = "Это интересно"
LINE_EDIT_MAIN_WINDOW_PLACEHOLDER = "Искать..."
PUSH_BUTTON_TICKETS_LIST_TEXT = "Список Билетов"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont("data\\fonts\\Evolventa.otf")
        QFontDatabase.addApplicationFont("data\\fonts\\Lumberjack.otf")
        with open("data\\json\\main.json", "r") as f:
            self.strings = json.loads(f.read())
        self.wBackground = QWidget()
        self.wBackground.setProperty("class", "Background")

        self.vbBackground = QVBoxLayout()
        self.vbBackground.setContentsMargins(0, 0, 0, 0)
        self.wHeader = QWidget()
        self.saBody = QScrollArea()
        self.saBody.setProperty("class", "saBody")
        self.pbTicketsList = QPushButton(PUSH_BUTTON_TICKETS_LIST_TEXT)
        self.pbTicketsList.setProperty("class", "TicketsList")
        self.vbBackground.addWidget(self.wHeader, stretch=1)
        self.vbBackground.addWidget(self.saBody, stretch=8)
        self.vbBackground.addWidget(self.pbTicketsList, stretch=1)
        self.vbBackground.setSpacing(0)
        self.wBackground.setLayout(self.vbBackground)

        self.hbHeader = QHBoxLayout()
        self.pbProfile = QPushButton()
        self.pbProfile.setProperty("class", "Profile")
        self.pbProfile.setIcon(QIcon(ICON_MAIN_PROFILE))
        self.pbProfile.setIconSize(QSize(60, 60))
        self.pbMenu = QPushButton()
        self.pbMenu.setProperty("class", "Menu")
        self.pbMenu.setIcon(QIcon(ICON_MAIN_MENU))
        self.pbMenu.setIconSize(QSize(60, 60))
        self.leSearch = QLineEdit()
        self.leSearch.setProperty("class", "Search")
        self.hbHeader.addWidget(self.pbProfile, stretch=1)
        self.hbHeader.addWidget(self.pbMenu, stretch=1)
        self.hbHeader.addWidget(self.leSearch, stretch=8)
        self.wHeader.setLayout(self.hbHeader)

        self.wBody = QWidget()
        self.wBody.setProperty("class", "wBody")
        self.vbBody = QVBoxLayout()
        self.vbBody.setContentsMargins(0, 0, 0, 0)
        self.lBodyHeader = QLabel(LABEL_BODY_HEADER_TEXT)
        self.lBodyHeader.setProperty("class", "BodyHeader")
        self.wFacts = list()
        for i in range(3):
            wFact = QWidget()
            if i < 2:
                wFact.setProperty("class", "Fact")
            self.wFacts.append(wFact)
        self.vbBody.addWidget(self.lBodyHeader)
        for i in range(3):
            self.vbBody.addWidget(self.wFacts[i])
        self.vbBody.setSpacing(0)
        self.wBody.setLayout(self.vbBody)
        self.saBody.setWidgetResizable(True)
        self.saBody.setWidget(self.wBody)

        self.hbFacts = list()
        self.lFactImages = list()
        self.lFactTexts = list()
        for i in range(3):
            self.hbFacts.append(QHBoxLayout())
            lFactImage = QLabel()
            lFactImage.setPixmap(QPixmap("data\\images\\fact_{}.png".format(i + 1)))
            self.lFactImages.append(lFactImage)
            lFactText = QLabel(self.strings["fact_{}_text".format(i + 1)])
            lFactText.setProperty("class", "FactText")
            lFactText.setWordWrap(True)
            self.lFactTexts.append(lFactText)
            if i % 2 == 0:
                self.hbFacts[i].addWidget(self.lFactImages[i], stretch=1)
                self.hbFacts[i].addWidget(self.lFactTexts[i], stretch=9, alignment=Qt.AlignTop)
            else:
                self.hbFacts[i].addWidget(self.lFactTexts[i], stretch=9, alignment=Qt.AlignTop)
                self.hbFacts[i].addWidget(self.lFactImages[i], stretch=1)
            self.wFacts[i].setLayout(self.hbFacts[i])

        self.leSearch.setPlaceholderText(LINE_EDIT_MAIN_WINDOW_PLACEHOLDER)
        self.resize(1200, 900)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(900)
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setCentralWidget(self.wBackground)
        with open("scripts\\main.css", "r") as f:
            self.setStyleSheet(f.read())
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
