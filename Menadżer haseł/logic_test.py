import pytest
import os
from logic import PasswordManager


@pytest.fixture
def password_manager():
    """Tworzy czystą bazę na pliku testowym dla każdego testu."""
    test_file = "test_passwords.json"
    pm = PasswordManager(test_file)
    pm.passwords = {}
    pm._save_data()

    yield pm

    if os.path.exists(test_file):
        os.remove(test_file)


def test_save_and_get_password(password_manager):
    password_manager.save_password("Facebook", "haslo123")
    assert password_manager.get_password("Facebook") == "haslo123"


def test_update_password(password_manager):
    password_manager.save_password("Instagram", "stare")
    password_manager.save_password("Instagram", "nowe")
    assert password_manager.get_password("Instagram") == "nowe"


def test_remove_password(password_manager):
    password_manager.save_password("Google", "12345")
    password_manager.remove_password("Google")
    assert password_manager.get_password("Google") is None


def test_get_all_apps(password_manager):
    password_manager.save_password("App1", "pass1")
    password_manager.save_password("App2", "pass2")
    apps = password_manager.get_all_apps()
    assert "App1" in apps
    assert "App2" in apps
    assert len(apps) == 2