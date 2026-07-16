from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.is_hungry = True
        self.energy = 100

    def eat(self, food: str):
        if self.is_hungry:
            self.is_hungry = False
            self.energy += 20
            return f"{self.name} съел {food}. Энергия: {self.energy}"
        else:
            return f"{self.name} не голоден!"

    def sleep(self, hours: int):
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100
        return f"{self.name} поспал {hours} часов. Энергия: {self.energy}"

    def play(self) -> str:
        if self.energy < 20:
            return f"{self.name} слишком устал для игры!"
        self.energy -= 20
        self.is_hungry = True
        return f"{self.name} играет. Энергия: {self.energy}"

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def info(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.age} лет"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def play(self):
        result = super().play()
        if "играет" in result:
            return result.replace("играет", "играет с мячом")
        return result

    def make_sound(self) -> str:
        return f"{self.name} гавкает!"

    def info(self) -> str:
        return f"{super().info()}, порода: {self.breed}"

    def make_roll(self) -> str:
        if self.energy < 10:
            return f"{self.name} слишком устал"
        else:
            self.energy -= 10
            return f"{self.name} делает кувырок"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    def play(self):
        result = super().play()
        if "играет" in result:
            return result.replace("играет", "играет с клубком")
        return result

    def make_sound(self) -> str:
        return f"{self.name} мяукает!"

    def info(self) -> str:
        return f"{super().info()}, цвет: {self.color}"

    def jump(self) -> str:
        if self.energy < 10:
            return f"{self.name} слишком устал"
        else:
            self.energy -= 10
            return f"{self.name} прыгает на стол"


class Bird(Animal):
    def __init__(self, name: str, age: int, wingspan: float) -> None:
        super().__init__(name, age)
        self.wingspan = wingspan

    def play(self):
        result = super().play()
        if "играет" in result:
            return result.replace("играет", "играет с зеркальцем")
        return result

    def make_sound(self) -> str:
        return f"{self.name} пищит!"

    def info(self) -> str:
        return f"{super().info()}, размах крыльев: {self.wingspan}"

    def sing(self) -> str:
        if self.energy < 10:
            return f"{self.name} слишком устал"
        else:
            self.energy -= 10
            return f"{self.name} поет мелодию"


def manage_shelter(animals: list[Animal]) -> None:
    print("\n🏠 ПРИЮТ ДЛЯ ЖИВОТНЫХ")
    print("=" * 40)

    for animal in animals:
        print(animal.info())
        print(f"  {animal.make_sound()}")
        print(f"  {animal.eat('корм')}")
        print()


if __name__ == "__main__":
    # Создаём животных
    dog = Dog("Бобик", 3, "Дворняга")
    cat = Cat("Мурка", 2, "Рыжий")
    bird = Bird("Кеша", 1, 0.3)

    # Типизированный список!
    animals: list[Animal] = [dog, cat, bird]
    manage_shelter(animals)

    # Демонстрация специфических методов
    print("🐕 СПЕЦИФИЧЕСКИЕ МЕТОДЫ СОБАКИ:")
    print("-" * 40)
    print(dog.make_roll())

    print("\n🐱 СПЕЦИФИЧЕСКИЕ МЕТОДЫ КОШКИ:")
    print("-" * 40)
    print(cat.jump())

    print("\n🐦 СПЕЦИФИЧЕСКИЕ МЕТОДЫ ПТИЦЫ:")
    print("-" * 40)
    print(bird.sing())

    # Проверка иерархии
    print("\n📊 ПРОВЕРКА ИЕРАРХИИ:")
    print("-" * 40)
    print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
    print(f"  isinstance(cat, Animal): {isinstance(cat, Animal)}")
    print(f"  isinstance(bird, Animal): {isinstance(bird, Animal)}")
    print(f"  issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
