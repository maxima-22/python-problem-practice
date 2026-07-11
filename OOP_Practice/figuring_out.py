class Monkey:
    """ "Попытка смоделировать обезьяну"""

    def __init__(self, name, age, type=None, color=None) -> None:
        """Инициализирую аттрибуты: имя, возраст, вид, цвет"""
        self.name = name
        self.age = age
        self.type = type
        self.color = color

    def jump(self):
        """Сиумуляция прыжка обезьяны в ответ на команду"""
        print(self.name.title() + " is now jumping.")

    def sit(self):
        """Симуляция сиденья обезьянки в ответ на команду"""
        print(self.name.title() + " is now sitting.")


my_monkey = Monkey("Danya", 24)
print("My monkey's name is " + my_monkey.name.title() + ".")
print("He is " + str(my_monkey.age) + " years old.")

my_monkey.jump()
my_monkey.sit()


class ATM:
    def __init__(
        self,
        location: str,
        cash_balance: int,
        is_online: bool,
        bank_name: str,
        receipt_paper_left: int,
        atm_num: int,
    ) -> None:
        self.location = location
        self.cash_balance = cash_balance
        self.is_online = is_online
        self.bank_name = bank_name
        self.receipt_paper_left = receipt_paper_left
        self.atm_num = atm_num

    def withdraw(self, amount):
        if not self._is_available():
            return
        if amount <= 0:
            print("Invalid amount!")
            return
        if self.cash_balance - amount >= 0:
            self.cash_balance -= amount
            print("Withdraw successfully completed!")
            self.print_receipt()
        else:
            print("ATM's balance is not enough to fulfil your withdraw")
            return

    def deposit(self, amount):
        if not self._is_available():
            return
        if amount <= 0:
            print("Invalid amount!")
            return
        self.cash_balance += amount
        print(f"Deposited {amount}. New balance: {self.cash_balance}")

    def check_balance(self):
        if not self._is_available():
            return
        print(f"Current balance: {self.cash_balance}")

    def print_receipt(self):
        if self.receipt_paper_left > 0:
            self.receipt_paper_left -= 1
            print("Receipt is printed. Don't forget to take it!")
            return
        else:
            print("No paper left to print receipt, it will be available online!")
            return

    def _is_available(self):
        """Проверяет, онлайн ли банкомат."""
        if not self.is_online:
            print("ATM is offline! Try again later.")
            return False
        return True


# 1. Создаём банкомат
atm = ATM(
    location="Moscow",
    cash_balance=10000,
    is_online=True,
    bank_name="Sberbank",
    receipt_paper_left=3,
    atm_num=101,
)

# 2. Проверяем баланс
atm.check_balance()  # Current balance: 10000

# 3. Снимаем деньги (корректно)
atm.withdraw(500)  # Withdraw successfully completed! Receipt is printed.

# 4. Проверяем баланс после снятия
atm.check_balance()  # Current balance: 9500

# 5. Снимаем больше, чем есть
atm.withdraw(10000)  # ATM's balance is not enough to fulfil your withdraw

# 6. Снимаем отрицательную сумму
atm.withdraw(-100)  # Invalid amount!

# 7. Пополняем счёт
atm.deposit(2000)  # Deposited 2000. New balance: 11500

# 8. Проверяем баланс после пополнения
atm.check_balance()  # Current balance: 11500

# 9. Снимаем всю сумму
atm.withdraw(11500)  # Withdraw successfully completed! Receipt is printed.

# 10. Проверяем баланс (должен быть 0)
atm.check_balance()  # Current balance: 0

# 11. Отключаем банкомат
atm.is_online = False

# 12. Пробуем снять деньги
atm.withdraw(100)  # ATM is offline! Try again later.

# 13. Пробуем проверить баланс
atm.check_balance()  # ATM is offline! Try again later.

# 14. Включаем обратно и проверяем чек
atm.is_online = True

atm.deposit(500)
# 15. Снимаем деньги, чтобы проверить печать чека
atm.withdraw(100)  # Receipt is printed.
atm.withdraw(100)  # No paper left to print receipt, it will be available online!
