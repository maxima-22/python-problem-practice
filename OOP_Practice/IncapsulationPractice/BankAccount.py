from typing import List


class BankAccount:
    LENGTH_PIN = 4

    def __init__(self, owner: str, balance: float, pin: str):
        # 🚨 Всё публично!
        self.owner = owner
        if balance < 0:
            raise ValueError("Balance must be positive.")
        self._balance = balance  # Проблема: прямой доступ - DONE
        self.pin = pin  # Проблема: PIN виден - DONE
        self._transactions = []  # Проблема: можно изменить историю

    # ====== Balance and Transactions ======

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def transactions(self) -> list:
        return self._transactions

    # =============== Pin ===================

    @property
    def pin(self) -> str:
        pin = self.__pin
        return f"{pin[:1]}..."

    @pin.setter
    def pin(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Pin must be str type, given type: {type(value)}")
        if len(value) != self.LENGTH_PIN:
            raise ValueError(f"Pin's length must be: {self.LENGTH_PIN}")
        self.__pin = value

    # ======= Private Methods ===========

    def _log_transaction(self, operation: str, amount: float) -> None:
        self._transactions.append(
            f"Operation: {operation}, amount: {amount}, balance: {self._balance}"
        )

    # =========== Methods ===============

    def deposit(self, amount: float) -> None:
        """Пополнить счёт."""
        amount = float(amount)
        if not isinstance(amount, float):
            raise TypeError(f"Amount must be float type, given type: {type(amount)}")
        if amount <= 0:
            raise ValueError("Deposit's amount must be positive")
        self._balance += amount
        self._log_transaction("Deposit", amount)

    def withdraw(self, amount: float, pin: str) -> None:
        """Снять деньги."""
        amount = float(amount)
        if pin != self.__pin:
            raise PermissionError("Pin is not correct!!")
        if self._balance < amount:
            raise ValueError(
                "You don't have enough money on your card for this operation. :("
            )
        self._balance -= amount
        self._log_transaction("Withdraw", -amount)

    def get_balance(self) -> float:
        """Получить баланс."""
        return self.balance

    def get_transactions(self) -> List[str]:
        return self._transactions.copy()

    def change_pin(self, pin: str, new_pin: str) -> None:
        if pin != self.__pin or not pin.isdigit():
            raise PermissionError("Wrong PIN!")
        self.pin = new_pin
        print("PIN successfully changed!")


if __name__ == "__main__":
    # Создаём счёт
    account = BankAccount("Иван Иванов", 1000.0, "1234")

    print("=== Демонстрация проблем ===\n")

    # 🚨 Проблема 1: PIN виден всем
    print(f"PIN-код (виден!): {account.pin}")

    # 🚨 Проблема 2: Баланс можно изменить напрямую
    print(f"Баланс до взлома: {account.balance}")

    try:
        account.balance = 1000000  # Просто накрутили!
    except AttributeError as e:
        print(f"Error: {e}")
    print(f"Баланс после взлома: {account.balance}")

    # 🚨 Проблема 3: Можно снять больше, чем есть
    try:
        account.withdraw(5000, "1234")  # Баланс станет отрицательным!
    except ValueError as e:
        print(f"Error: {e}")
    print(f"Баланс после снятия 500 из 100: {account.balance}")

    # 🚨 Проблема 4: Можно пополнить на отрицательную сумму
    try:
        account.deposit(-1000)
    except ValueError as e:
        print(f"Error: {e}")
    print(f"Баланс после 'пополнения' на -1000: {account.balance}")

    # 🚨 Проблема 5: Можно изменить историю
    transactions = account.get_transactions()
    print(f"История: {account.get_transactions()}")
    transactions.append("Пополнение: +999999 (подделка!)")
    print(f"История: {account.get_transactions()}")

    print("Changing pin:")
    account.change_pin("1234", "0000")
    print(f"New PIN: {account.pin}")
