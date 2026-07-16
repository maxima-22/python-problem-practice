from abc import ABC


class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"Name: {self.name}, age: {self.age}"


class Player(Person):
    def __init__(self, name: str, age: int, number: int):
        super().__init__(name, age)
        self.number = number
        self.role = "Player"

    def info(self) -> str:
        return f"{super().info()}, number:{self.number}"


class Goalkeeper(Player):
    def __init__(self, name: str, age: int, number: int):
        super().__init__(name, age, number)
        self.role = "Goalkeeper"

    def info(self) -> str:
        return f"{super().info()}, role:{self.role}"


class Defender(Player):
    def __init__(self, name: str, age: int, number: int):
        super().__init__(name, age, number)
        self.role = "Defender"

    def info(self) -> str:
        return f"{super().info()}, role:{self.role}"


class Forward(Player):
    def __init__(self, name: str, age: int, number: int):
        super().__init__(name, age, number)
        self.role = "Forward"

    def info(self) -> str:
        return f"{super().info()}, role:{self.role}"


class Coach(Player):
    def __init__(self, name: str, age: int, number: int):
        super().__init__(name, age, number)
        self.role = "Coach"

    def info(self) -> str:
        return f"{super().info()}, role:{self.role}"


class Team:
    def __init__(self, name: str, coach: Coach):
        self.name = name
        self.coach = coach
        self.players: list[Player] = []

    def add_player(self, player: Player) -> str:
        self.players.append(player)
        return f"✅ {player.name} добавлен в {self.name}"

    def remove_player(self, number: int) -> str:
        for player in self.players:
            if player.number == number:
                self.players.remove(player)
                return f"❌ {player.name} покинул {self.name}"
        return f"⚠️ Игрок с номером {number} не найден"

    def get_lineup(self) -> dict[str, list[Player]]:
        lineup = {
            "Вратарь": [],
            "Защитник": [],
            "Нападающий": [],
        }
        for player in self.players:
            if player.role in lineup:
                lineup[player.role].append(player)
        return lineup

    def show_roster(self) -> None:
        """Показать состав команды."""
        print(f"\n⚽ {self.name.upper()}")
        print("=" * 50)
        print(f"Тренер: {self.coach.info()}")
        print("-" * 50)

        lineup = self.get_lineup()
        for role, players in lineup.items():
            if players:
                print(f"\n{role}:")
                for player in players:
                    print(f"  {player.info()}")


if __name__ == "__main__":
    print("=" * 60)
    print("⚽ ФУТБОЛЬНАЯ ЛИГА")
    print("=" * 60)

    # Создаём тренера
    coach = Coach("Карло Анчелотти", 65, 30)

    # Создаём команду
    team = Team("Реал Мадрид", coach)

    # Создаём игроков разных позиций
    goalkeeper = Goalkeeper("Тибо Куртуа", 32, 1)
    defender1 = Defender("Давид Алаба", 31, 4)
    defender2 = Defender("Антонио Рюдигер", 30, 22)
    forward1 = Forward("Винисиус Жуниор", 23, 7)
    forward2 = Forward("Килиан Мбаппе", 25, 9)

    # Добавляем в команду
    for player in [
        goalkeeper,
        defender1,
        defender2,
        forward1,
        forward2,
    ]:
        print(team.add_player(player))

    # Показываем состав
    team.show_roster()

    # Проверка иерархии
    print("\n" + "=" * 60)
    print("📊 ИЕРАРХИЯ КЛАССОВ")
    print("=" * 60)
    print(f"  isinstance(forward1, Player): {isinstance(forward1, Player)}")
    print(f"  isinstance(forward1, Person): {isinstance(forward1, Person)}")
    print(f"  isinstance(coach, Person):    {isinstance(coach, Person)}")
    print(f"  isinstance(coach, Player):    {isinstance(coach, Player)}")
    print(f"\n  Forward.__mro__:")
    for cls in Forward.__mro__:
        print(f"    → {cls.__name__}")
