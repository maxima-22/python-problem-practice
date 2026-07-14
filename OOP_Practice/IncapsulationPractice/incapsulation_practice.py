from typing import List


class SecretAgent:
    """
    Incapsulation Practice
    """

    MIN_CLEARANCE = 1
    MAX_CLEARANCE = 10
    AUTHORIZATION_CODE = "ALPHA-22"

    def __init__(self, codename: str, real_identity: str, clearance_lvl: int) -> None:
        self.codename = codename
        self.__real_identity = real_identity
        self.clearance_lvl = clearance_lvl
        self._missions: List[str] = []
        self._is_active = True

    @property
    def clearance_lvl(self) -> int:
        return self.__clearance_level

    @clearance_lvl.setter
    def clearance_lvl(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Level can only be int. Your type: {type(value)}")
        if not self.MIN_CLEARANCE <= value <= self.MAX_CLEARANCE:
            raise ValueError(
                f"Level must be between {self.MIN_CLEARANCE} and {self.MAX_CLEARANCE}"
            )
        self.__clearance_level = value

    @property
    def identity(self) -> str:
        name = self.__real_identity
        if len(name) > 4:
            return f"{name[0]}***{name[-1]}"
        return "****"

    @identity.setter
    def identity(self, name: str) -> None:
        if self.clearance_lvl < 7:
            raise PermissionError("Access DENIED! Your clearance level must be higher")
        self.__real_identity = name

    @property
    def status(self) -> str:
        if not self._is_active:
            return "Retired"
        missions = len(self._missions)
        if missions == 0:
            return "Trainee"
        elif missions < 5:
            return "Amateur"
        else:
            return "Veteran"

    @property
    def mission_count(self) -> int:
        return len(self._missions)

    def reveal_identity(self, auth_code: str = None) -> str:
        if not auth_code:
            return "Authorization code is required for this operation."
        if auth_code != self.AUTHORIZATION_CODE:
            raise PermissionError("Access DENIED! Authorization code is wrong.")
        return f"Real name is {self.__real_identity}"

    def complete_mission(self, mission_name: str) -> None:
        if not self._is_active:
            raise RuntimeError("Agent is not available.")
        self._missions.append(mission_name)
        print(
            f"Mission {mission_name} is completed! Overall count: {self.mission_count}"
        )


# ============= ДЕМОНСТРАЦИЯ РАБОТЫ =============
if __name__ == "__main__":
    print("=" * 60)
    print("🕵️‍♂️ ДОБРО ПОЖАЛОВАТЬ В АГЕНТСТВО ТАЙНЫХ АГЕНТОВ 🕵️‍♂️")
    print("=" * 60)
    print()

    # --- 1. СОЗДАЁМ АГЕНТА ---
    print("📌 ШАГ 1: Создаём нового агента")
    print("-" * 40)
    bond = SecretAgent("007", "James Bond", 8)
    print(f"✅ Агент создан!")
    print(f"   Кодовое имя: {bond.codename}")
    print(f"   Уровень допуска: {bond.clearance_lvl}")
    print(f"   Статус: {bond.status}")
    print(f"   Маскированная личность: {bond.identity}")
    print()

    # --- 2. ВЫПОЛНЯЕМ МИССИИ ---
    print("📌 ШАГ 2: Агент выполняет миссии")
    print("-" * 40)

    missions = ["GoldenEye", "Skyfall", "Spectre", "No Time to Die"]

    for mission in missions:
        bond.complete_mission(mission)
    print()
    print(f"📊 Текущий статус: {bond.status}")
    print(f"   Всего миссий: {bond.mission_count}")
    print()

    # --- 3. ПРОВЕРКА ЛИЧНОСТИ ---
    print("📌 ШАГ 3: Проверяем личность (с авторизацией)")
    print("-" * 40)

    print("🔐 Попытка раскрыть личность БЕЗ кода:")
    result = bond.reveal_identity()
    print(f"   Результат: {result}")
    print()

    print("🔐 Попытка раскрыть личность С ПРАВИЛЬНЫМ кодом:")
    result = bond.reveal_identity(SecretAgent.AUTHORIZATION_CODE)
    print(f"   Результат: {result}")
    print()

    print("🔐 Попытка раскрыть личность С НЕПРАВИЛЬНЫМ кодом:")
    try:
        result = bond.reveal_identity("WRONG-CODE")
        print(f"   Результат: {result}")
    except PermissionError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    # --- 4. МЕНЯЕМ ИМЯ (требуется высокий уровень) ---
    print("📌 ШАГ 4: Пытаемся сменить реальное имя")
    print("-" * 40)

    print(f"👤 Текущее маскированное имя: {bond.identity}")
    print(f"🔑 Текущий уровень допуска: {bond.clearance_lvl}")
    print()

    print("🔄 Пытаемся сменить имя на 'Ethan Hunt'...")
    try:
        bond.identity = "Ethan Hunt"
        print(f"✅ Имя успешно изменено!")
        print(f"   Новое маскированное имя: {bond.identity}")
    except PermissionError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    # --- 5. СОЗДАЁМ АГЕНТА С НИЗКИМ УРОВНЕМ ---
    print("📌 ШАГ 5: Создаём агента-новичка")
    print("-" * 40)

    rookie = SecretAgent("Rookie-1", "John Doe", 3)
    print(f"✅ Агент-новичок создан!")
    print(f"   Кодовое имя: {rookie.codename}")
    print(f"   Уровень допуска: {rookie.clearance_lvl}")
    print(f"   Статус: {rookie.status}")
    print(f"   Маскированная личность: {rookie.identity}")
    print()

    print("🔄 Пытаемся сменить имя новичка на 'Jane Doe'...")
    try:
        rookie.identity = "Jane Doe"
        print(f"✅ Имя изменено!")
    except PermissionError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    # --- 6. ПРОВЕРКА ВАЛИДАЦИИ УРОВНЯ ---
    print("📌 ШАГ 6: Проверяем валидацию уровня допуска")
    print("-" * 40)

    print("🔄 Пытаемся установить уровень 99...")
    try:
        bond.clearance_lvl = 99
    except ValueError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    print("🔄 Пытаемся установить уровень 'высокий'...")
    try:
        bond.clearance_lvl = "высокий"
    except TypeError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    # --- 7. СТАТУСЫ АГЕНТОВ ---
    print("📌 ШАГ 7: Сравниваем статусы агентов")
    print("-" * 40)

    print(f"🕵️ {bond.codename}: {bond.status} ({bond.mission_count} миссий)")
    print(f"🕵️ {rookie.codename}: {rookie.status} ({rookie.mission_count} миссий)")
    print()

    # --- 8. УВОЛЬНЕНИЕ АГЕНТА ---
    print("📌 ШАГ 8: Агент уходит на пенсию")
    print("-" * 40)

    bond._is_active = False
    print(f"🔴 Агент {bond.codename} уволен!")
    print(f"   Новый статус: {bond.status}")
    print()

    print("🔄 Пытаемся дать миссию уволенному агенту...")
    try:
        bond.complete_mission("Impossible Mission")
    except RuntimeError as e:
        print(f"   ❌ Ошибка: {e}")
    print()

    # --- ЗАКЛЮЧЕНИЕ ---
    print("=" * 60)
    print("🏁 ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА 🏁")
    print("=" * 60)
