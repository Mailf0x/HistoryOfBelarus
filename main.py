from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
MAIN_WINDOW_TITLE = "(НАЗВАНИЕ ПРОЕКТА)"
LINE_EDIT_MAIN_WINDOW_PLACEHOLDER = "Искать..."
PUSH_BUTTON_TICKETS_LIST_TEXT = "Список билетов"
TEXT = "TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT TEXT "
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wBackground = QWidget()

        self.vbBackground = QVBoxLayout()
        self.wHeader = QWidget()
        self.saBody = QScrollArea()
        self.pbTicketsList = QPushButton(PUSH_BUTTON_TICKETS_LIST_TEXT)
        self.vbBackground.addWidget(self.wHeader, stretch=1)
        self.vbBackground.addWidget(self.saBody, stretch=8)
        self.vbBackground.addWidget(self.pbTicketsList, stretch=1)
        self.vbBackground.setSpacing(0)
        self.wBackground.setLayout(self.vbBackground)

        self.hbHeader = QHBoxLayout()
        self.pbMenu = QPushButton()
        self.leSearch = QLineEdit()
        self.pbProfile = QPushButton()
        self.hbHeader.addWidget(self.pbMenu, stretch=1)
        self.hbHeader.addWidget(self.leSearch, stretch=8)
        self.hbHeader.addWidget(self.pbProfile, stretch=1)
        self.wHeader.setLayout(self.hbHeader)

        self.wBody = QWidget()
        self.vbBody = QVBoxLayout()
        self.lBodyHeader = QLabel("Это интересно")
        self.wFacts = list()
        for i in range(3):
            wFact = QWidget()
            wFact.setStyleSheet("border-top: 3px solid black;")
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
            lFactImage.setPixmap(QPixmap("images\\fact_1.png"))
            lFactImage.setStyleSheet("border: none;")
            self.lFactImages.append(lFactImage)
            lFactText = QLabel(TEXT)
            lFactText.setWordWrap(True)
            lFactText.setStyleSheet("border: none; font-size: 20px;")
            self.lFactTexts.append(lFactText)
            if i % 2 == 0:
                self.hbFacts[i].addWidget(self.lFactImages[i], stretch=1)
                self.hbFacts[i].addWidget(self.lFactTexts[i], stretch=9, alignment=Qt.AlignTop)
            else:
                self.hbFacts[i].addWidget(self.lFactTexts[i], stretch=9, alignment=Qt.AlignTop)
                self.hbFacts[i].addWidget(self.lFactImages[i], stretch=1)
            self.wFacts[i].setLayout(self.hbFacts[i])

        self.lBodyHeader.setStyleSheet("font-size: 60px;")
        self.lBodyHeader.setAlignment(Qt.AlignCenter)
        self.wHeader.setStyleSheet("border-bottom: 3px solid black; background-color: gray;")
        self.pbMenu.setStyleSheet("background-color: dimGray; border: 3px solid black; border-radius: 30px; height: 60px; width: 60px;")
        self.leSearch.setStyleSheet("background-color: darkGray; border: 3px solid black; border-radius: 30px; font-size: 30px; height: 60px; padding-left: 20px")
        self.leSearch.setPlaceholderText(LINE_EDIT_MAIN_WINDOW_PLACEHOLDER)
        self.pbProfile.setStyleSheet("background-color: dimGray; border: 3px solid black; border-radius: 30px; height: 60px; width: 60px;")
        self.pbTicketsList.setStyleSheet("background-color: white; border-top: 3px solid black; height: 60px; width: 60px; font-size: 60px;")
        self.resize(1200, 900)
        self.setMaximumWidth(1200)
        self.setMaximumHeight(900)
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setCentralWidget(self.wBackground)
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
