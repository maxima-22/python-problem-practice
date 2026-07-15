from functools import total_ordering


class CartItem:
    def __init__(self, name: str, price: float, quantity: int = 1) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"CartItem('{self.name}', {self.price}₽ x{self.quantity})"

    def __str__(self) -> str:
        total = self.price * self.quantity
        return f"{self.name}: {self.quantity} x {self.price}₽ = {total}₽"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CartItem):
            return self.name == other.name
        if isinstance(other, str):
            return self.name == other
        return NotImplemented

    @property
    def total(self) -> float:
        return self.quantity * self.price


@total_ordering
class ShoppingCart:
    def __init__(self, name: str = "Cart") -> None:
        self.name = name
        self.items: list[CartItem] = []

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(CartItem(name, price, quantity))

    @property
    def total(self) -> float:
        return sum(item.total for item in self.items)

    def __str__(self) -> str:
        if not self.items:
            return "Shopping cart is empty."
        lines = [f"{self.name}:"]
        for item in self.items:
            lines.append(f"- {item}")
        lines.append("--------")
        lines.append(f"Total: {self.total}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        items = [item.name for item in self.items]
        return f"ShoppingCart('{self.name}', {items}, total={self.total}₽)"

    def __len__(self):
        return sum(item.quantity for item in self.items)

    def __bool__(self):
        return len(self.items) > 0

    def __contains__(self, item):
        if isinstance(item, str):
            return any(i.name == item for i in self.items)
        if isinstance(item, CartItem):
            return item in self.items
        return False

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        if isinstance(value, ShoppingCart):
            self.items[key] = value

    def __iter__(self):
        return iter(self.items)

    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        new_cart = ShoppingCart(f"{self.name} + {other.name}")
        for item in self.items:
            new_cart.add(item.name, item.price, item.quantity)
        for item in other.items:
            new_cart.add(item.name, item.price, item.quantity)
        return new_cart

    def __eq__(self, other: object) -> bool:
        """Сравнение по сумме."""
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return self.total == other.total

    def __lt__(self, other: object) -> bool:
        """Меньше по сумме."""
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return self.total < other.total


if __name__ == "__main__":
    print("=" * 60)
    print("ShoppingCart with dunder-methods")
    print("=" * 60)
    print()

    cart = ShoppingCart("Мои покупки")
    cart.add("Молоко", 80)
    cart.add("Хлеб", 50, 2)
    cart.add("Сыр", 200)

    # __str__: просто print()!
    print("=== print(cart) ===")
    print(cart)
    print()

    # __repr__
    print("=== repr(cart) ===")
    print(repr(cart))
    print()

    # __len__
    print("=== len(cart) ===")
    print(f"len(cart) = {len(cart)} единиц товара")
    print()

    # __bool__
    print("=== bool() ===")
    empty = ShoppingCart("Пустая")
    print(f"if cart: {bool(cart)}")
    print(f"if empty: {bool(empty)}")
    print()

    # __contains__
    print("=== in ===")
    print(f'"Молоко" in cart: {"Молоко" in cart}')
    print(f'"Бананы" in cart: {"Бананы" in cart}')
    print()

    # __iter__
    print("=== for item in cart ===")
    for item in cart:
        print(f"  {item.name}: {item.quantity} шт.")
    print()

    # __getitem__
    print("=== cart[0] ===")
    print(f"cart[0] = {cart[0]}")
    print(f"cart[-1] = {cart[-1]}")
    print()

    # __add__
    print("=== cart1 + cart2 ===")
    cart2 = ShoppingCart("Дополнительно")
    cart2.add("Яблоки", 100, 3)
    cart2.add("Молоко", 80, 2)  # То же молоко — увеличится количество!

    combined = cart + cart2
    print(combined)
    print()

    # __eq__ / __lt__
    print("=== Сравнение ===")
    print(f"cart.total = {cart.total}₽")
    print(f"cart2.total = {cart2.total}₽")
    print(f"cart > cart2: {cart > cart2}")
