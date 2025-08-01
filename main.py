from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QCheckBox, QDialog, QVBoxLayout, QComboBox, QMainWindow, QStackedWidget, QListWidget
from PySide6.QtCore import QSettings
import sys

class Language:
    
    SPRACHEN = {0: "Englisch", 1: "Deutsch"}

    woerter = {
        0: ["Calendar", "Tasks"],
        1: ["Kalender", "Aufgaben"]
    }

    def __init__(self):
        self.curr_lang = 0 # Standard English
    
    def set_lang(self, sprach_id: int):
        if sprach_id in self.SPRACHEN:
            self.curr_lang = sprach_id
        else:
            print("Unknown ID!")

    def word(self, index: int):
        return self.woerter[self.curr_lang][index]

    # print(Language.word(0)) # Use language
    # Language.set_lang(1) # Switch language
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendo")
        
        central_widget = QWidget()
        self.layout = QGridLayout()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        TaskButton = QPushButton(language.word(1))
        self.layout.addWidget(TaskButton, 0, 0)
        CalendarButton = QPushButton(language.word(0))
        self.layout.addWidget(CalendarButton, 0, 1)
        SettingsButton = QPushButton("⚙")
        self.layout.addWidget(SettingsButton, 0, 2)

        self.stacked = QStackedWidget()
        self.layout.addWidget(self.stacked, 1, 0, 1, 3)

        # Task View

        self.task_view = QListWidget()
        self.task_view.addItems(["Task 1", "Task 2", "Task 3"])
        
        # Calendar View

        self.calendar_view = QLabel("Calendar View")

        # Settings View

        self.settings_view = QLabel("Settings View")

        self.stacked.addWidget(self.task_view)
        self.stacked.addWidget(self.calendar_view)
        self.stacked.addWidget(self.settings_view)

        TaskButton.clicked.connect(lambda: self.stacked.setCurrentWidget(self.task_view))
        CalendarButton.clicked.connect(lambda: self.stacked.setCurrentWidget(self.calendar_view))
        SettingsButton.clicked.connect(lambda: self.stacked.setCurrentWidget(self.settings_view))


language = Language()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
