from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from src.adb import Adb

class Gui(QWidget):
    def __init__(self, adb: Adb):
        super().__init__()

        self.adb = adb
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.adb.ip)
        self.setGeometry(100, 100, 300, 300)

        button_layout = self.init_buttons()
        custom_link_layout = self.init_custom_link()
        button_layout.addLayout(custom_link_layout)

        self.setLayout(button_layout)
        self.show()

    def init_buttons(self) -> QVBoxLayout:
        button_layout = QVBoxLayout()
        with open ("links.conf", "r") as links_file:
            links = links_file.readlines()
            for link in links:
                parts = link.split(": ")
                button_layout.addWidget(QPushButton(parts[0].strip(), self, clicked=lambda _, p=parts[1]: self.send_link(p.strip())))
        return button_layout
        

    def init_custom_link(self) -> QHBoxLayout:
        custom_link_layout = QHBoxLayout()
        custom_link_edit = QLineEdit(self)
        custom_link_button = QPushButton("Send Custom Link", self)
        custom_link_button.clicked.connect(lambda: self.send_link(custom_link_edit.text()))
        custom_link_layout.addWidget(custom_link_edit)
        custom_link_layout.addWidget(custom_link_button)
        return custom_link_layout

 
    def send_link(self, link: str) -> None:
        self.adb.send_link(link)
        print(f"Sent link: {link}")
