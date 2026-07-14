from typing import Tuple, List
import re


class SecureVault:
    MIN_LENGTH = 8
    UPPER_CASE = True
    LOWER_CASE = True
    CONT_DIGITS = True
    CONT_SPECIALS = True
    SPECIALS = "!@#$%^&*()-_=+{}[];:'\",<>./?\\|/"

    def __init__(self, master_password: str) -> None:
        self.master_password = master_password

        self.__passwords = {}

    # ==== Master Password =====

    @property
    def master_password(self) -> str:
        return self.__master_password

    @master_password.setter
    def master_password(self, password: str) -> None:
        is_strong, message = self._get_strong_password(password)
        if not is_strong:
            raise ValueError(f"Password is not strong because: {message}")
        self.__master_password = password

    # ===== Properties ======

    @property
    def service_count(self) -> int:
        return len(self.__passwords)

    @property
    def services(self) -> List[str]:
        return list(self.__passwords.keys())

    # ======== Private methods ================

    def _get_strong_password(self, password: str) -> Tuple[bool, str]:
        if len(password) < self.MIN_LENGTH:
            return False, "Password is too short!"
        if self.UPPER_CASE and not re.search(r"[A-Z]", password):
            return False, "Must contain an uppercase symbol."
        if self.LOWER_CASE and not re.search(r"[a-z]", password):
            return False, "Must contain a lowercase symbol."
        if self.CONT_DIGITS and not re.search(r"\d", password):
            return False, "Must contain a digit."
        if self.CONT_SPECIALS and not any(c in self.SPECIALS for c in password):
            return False, f"Must contain a special symbol like: {self.SPECIALS}."
        return True, "Password is strong enough!"

    def _log_password(self, service, password) -> None:
        if not service:
            raise ValueError("Services cant be empty.")
        self.__passwords[service] = password

    def _permission_check(self, master: str) -> None:
        if master != self.__master_password:
            raise PermissionError("Master Password is wrong!")

    # ======== Public methods ================

    def change_master_password(self, master: str, new_master: str) -> str:
        self._permission_check(master)
        is_strong, message = self._get_strong_password(new_master)
        if not is_strong:
            raise ValueError(f"Password is not strong because: {message}")
        self.__master_password = new_master
        return "Master password successfully changed!"

    def add_password(self, service: str, password: str, master: str) -> None:
        self._permission_check(master)
        is_strong, message = self._get_strong_password(password)
        if not is_strong:
            raise ValueError(f"Password was not added because: {message}")
        self._log_password(service, password)
        print("Password was successfully added to the vault.")

    def delete_password(self, service: str, master: str) -> None:
        self._permission_check(master)
        if service not in self.__passwords:
            raise AttributeError(f"Service: {service} is not in the vault.")
        del self.__passwords[service]
        print(f"{service} password was succesfully deleted!")

    def get_password(self, service: str, master: str) -> str:
        self._permission_check(master)
        if service not in self.__passwords:
            raise AttributeError(f"Service: {service} is not in the vault.")
        return f"{service}: {self.__passwords[service]}"

    def get_masked_passwords(self):
        for service, password in self.__passwords.items():
            yield f"{service:<10}: {str(password)[:2]}***{str(password)[-2:]}"


if __name__ == "__main__":
    print("=" * 60)
    print("SECURE VAULT — Безопасное хранилище паролей")
    print("=" * 60)

    # === Создание хранилища ===
    print("\n🔐 Создание хранилища:")

    # Слабый мастер-пароль не пройдёт
    try:
        vault = SecureVault("123")
    except ValueError as e:
        print(f"❌ Ошибка: {e}")

    # Сильный мастер-пароль
    vault = SecureVault("MyStr0ng!Pass")
    print("✅ Хранилище создано")

    # === Добавление паролей ===
    print("\n📝 Добавление паролей:")

    vault.add_password("github", "GitH@b2024!", "MyStr0ng!Pass")
    vault.add_password("gmail", "Gm@il!Secure1", "MyStr0ng!Pass")
    vault.add_password("netflix", "N3tflix#Pass!", "MyStr0ng!Pass")

    # Слабый пароль не пройдёт
    try:
        vault.add_password("twitter", "weak", "MyStr0ng!Pass")
    except ValueError as e:
        print(f"❌ Ошибка: {e}")

    # === Просмотр паролей (маскированные) ===
    print("\n👀 Маскированные пароли:")
    for password in vault.get_masked_passwords():
        print(password)

    # === Получение пароля ===
    print("\n🔑 Получение пароля:")

    # Неверный мастер-пароль
    try:
        vault.get_password("github", "wrong")
    except PermissionError as e:
        print(f"❌ Ошибка: {e}")

    # Правильный мастер-пароль
    password = vault.get_password("github", "MyStr0ng!Pass")
    print(f"✅ Пароль GitHub: {password}")

    # === Удаление пароля ===
    print("\n🗑️ Удаление пароля:")
    vault.delete_password("netflix", "MyStr0ng!Pass")
    print(f"Осталось паролей: {vault.service_count}")

    # === Смена мастер-пароля ===
    print("\n🔄 Смена мастер-пароля:")
    vault.change_master_password("MyStr0ng!Pass", "NewM@ster2024!")

    # Старый мастер-пароль больше не работает
    try:
        vault.get_password("gmail", "MyStr0ng!Pass")
    except PermissionError as e:
        print(f"❌ Старый мастер не работает: {e}")

    # Новый работает
    print(f"✅ Gmail: {vault.get_password('gmail', 'NewM@ster2024!')}")
