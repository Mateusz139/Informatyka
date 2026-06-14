import json
import os

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.passwords = self._load_data()

    def _load_data(self):
        """Wczytuje hasła z pliku JSON. Jeśli pliku nie ma, zwraca pusty słownik."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}

    def _save_data(self):
        """Zapisuje obecne hasła do pliku JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.passwords, file)

    def save_password(self, app_name, password):
        """Dodaje nowe hasło lub aktualizuje istniejące."""
        self.passwords[app_name] = password
        self._save_data()

    def remove_password(self, app_name):
        """Usuwa wybraną aplikację z listy."""
        if app_name in self.passwords:
            del self.passwords[app_name]
            self._save_data()

    def get_password(self, app_name):
        """Pokazuje hasło dla danej aplikacji."""
        return self.passwords.get(app_name)

    def get_all_apps(self):
        """Pokazuje listę samych nazw aplikacji do wyświetlenia na ekranie."""
        return list(self.passwords.keys())