from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QLabel
from logic import PasswordManager

class PasswordManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menedżer Haseł")
        self.setGeometry(100, 100, 400, 450)

        self.password_manager = PasswordManager()
        self.layout = QVBoxLayout()

        # Etykiety i pola tekstowe
        self.layout.addWidget(QLabel("Nazwa aplikacji / strony:"))
        self.app_input = QLineEdit()
        self.app_input.setPlaceholderText("Np. Facebook...")
        self.layout.addWidget(self.app_input)

        self.layout.addWidget(QLabel("Hasło:"))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Wpisz hasło...")
        self.layout.addWidget(self.password_input)

        # Przyciski akcji
        self.add_button = QPushButton("Zapisz / Aktualizuj Hasło")
        self.add_button.clicked.connect(self.save_password)
        self.layout.addWidget(self.add_button)

        self.show_button = QPushButton("Pokaż Wybrane Hasło")
        self.show_button.clicked.connect(self.show_password)
        self.layout.addWidget(self.show_button)

        self.remove_button = QPushButton("Usuń Wybrane Hasło")
        self.remove_button.clicked.connect(self.remove_password)
        self.layout.addWidget(self.remove_button)

        # Lista zapisanych aplikacji
        self.layout.addWidget(QLabel("Zapisane aplikacje:"))
        self.app_list = QListWidget()
        self.app_list.itemClicked.connect(self.on_list_click)
        self.layout.addWidget(self.app_list)

        self.setLayout(self.layout)

        # Aktualizacja listy przy uruchomieniu
        self.update_app_list()

    def save_password(self):
        app_name = self.app_input.text().strip()
        password = self.password_input.text().strip()

        if app_name and password:
            self.password_manager.save_password(app_name, password)
            self.app_input.clear()
            self.password_input.clear()
            self.update_app_list()
            QMessageBox.information(self, "Sukces", "Zapisano hasło")
        else:
            QMessageBox.warning(self, "Błąd", "Nazwa aplikacji i hasło nie mogą być puste")

    def show_password(self):
        app_name = self.app_input.text().strip()
        if app_name:
            password = self.password_manager.get_password(app_name)
            if password:
                self.password_input.setText(password)
            else:
                QMessageBox.warning(self, "Błąd", "Brak hasła dla tej aplikacji")
        else:
            QMessageBox.warning(self, "Błąd", "Wpisz lub wybierz z listy nazwę aplikacji")

    def remove_password(self):
        selected_item = self.app_list.currentItem()
        if selected_item:
            app_name = selected_item.text()
            self.password_manager.remove_password(app_name)
            self.app_input.clear()
            self.password_input.clear()
            self.update_app_list()
        else:
            QMessageBox.warning(self, "Błąd", "Najpierw wybierz aplikację z listy poniżej")

    def on_list_click(self, item):
        self.app_input.setText(item.text())
        self.password_input.clear()

    def update_app_list(self):
        """Aktualizuje widok listy aplikacji."""
        self.app_list.clear()
        self.app_list.addItems(self.password_manager.get_all_apps())