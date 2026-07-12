import yaml
from pathlib import Path


def load_and_parse_yaml():
    config_path = Path(__file__).parent / "heroes_presets.yaml"
    if not config_path.exists():
        print("No heroes_presets.yaml file found. Please create one")
        return None
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    print(f"{config_path.name} readed successfully.")
    return config


class Hero:
    """Hero from some RPG-game with YAML presets"""

    CREATED_COUNT = 0
    MAX_LEVEL = 99
    VALID_CLASSES = ["Warrior", "Mage", "Rogue"]

    def __init__(
        self,
        name: str,
        hp: int,
        mana: int,
        main_stat: str,
        strength: int,
        dexterity: int,
        intelligence: int,
        weapon: str,
        armor_type: str,
    ) -> None:
        self.name = name
        self.hp = hp
        self.mana = mana
        self.main_stat = main_stat
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.weapon = weapon
        self.armor_type = armor_type
        Hero.CREATED_COUNT += 1  # Counting number of Heroes

    @classmethod  # Creating hero from config.yaml
    def create_from_config(cls, name: str, config: dict):
        """Create hero from your config."""
        return cls(name=name, **config)

    def __str__(self) -> str:  # __str__ dunder-method for object description
        return f"{self.name} has {self.hp} HP and {self.mana} MP.\n Main stat is {self.main_stat}, stats are S: {self.strength}, D: {self.dexterity}, I: {self.intelligence}.\n He uses {self.weapon} and wears {self.armor_type}."


# -------------------------------------------------------------------------------------------------------
"""These are old functions that are not working properly right now due to the lack of attributes. Functions now work from config file.
    @classmethod
    def create_from_preset(cls, name: str, hero_class: str):
        "Hero Class choice"
        if hero_class not in cls.VALID_CLASSES:
            raise ValueError(
                f"\nThis hero class is unavailable: {hero_class}.\n"
                f"Available classes: {', '.join(cls.VALID_CLASSES)}."
            )
        if hero_class == "Warrior":
            return cls.create_warrior(name)
        if hero_class == "Mage":
            return cls.create_mage(name)
        if hero_class == "Rogue":
            return cls.create_rogue(name)

    @classmethod
    def create_warrior(cls, name: str) -> "Hero":
        "Creating Warrior"
        if not isinstance(name, str):  # Valid name check
            raise TypeError(f"Name must be a string! Given type: {type(name)}")
        if not name.strip():
            raise ValueError("Name must NOT be empty.")
        print(f"Hero {name}, class: Warrior created succefully!")
        return cls(
            name=name, hp=120, main_stat="STR", weapon="Sword", armor_type="Plate"
        )

    @classmethod
    def create_mage(cls, name: str) -> "Hero":
        "Creating Mage"
        if not isinstance(name, str):
            raise TypeError(f"Name must be a string! Given type: {type(name)}")
        if not name.strip():
            raise ValueError("Name must NOT be empty.")
        print(f"Hero {name}, class: Mage created succefully!")
        return cls(
            name=name, hp=80, main_stat="INT", weapon="Sceptre", armor_type="Cloth"
        )

    @classmethod
    def create_rogue(cls, name: str) -> "Hero":
        "Creating Rogue"
        if not isinstance(name, str):
            raise TypeError(f"Name must be a string! Given type: {type(name)}")
        if not name.strip():
            raise ValueError("Name must NOT be empty.")
        print(f"Hero {name}, class: Rogue created succefully!")
        return cls(
            name=name, hp=100, main_stat="DEX", weapon="Bow", armor_type="Leather"
        )  """
# ------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    config = load_and_parse_yaml()

    warrior_data = config["hero_presets"]["warrior"]
    mage_data = config["hero_presets"]["mage"]
    rogue_data = config["hero_presets"]["rogue"]

    max = Hero.create_from_config("Max", warrior_data)
    danya = Hero.create_from_config("Danya", rogue_data)
    dasha = Hero.create_from_config("Dasha", mage_data)

"""
max = Hero.create_from_preset("Max", "Warrior")
danya = Hero.create_from_preset("Danya", "Rogue")
dasha = Hero.create_mage("Dasha")
nastya = Hero.create_from_preset("Nastya", "Necromancer")
"""

print(f"Герой 1:\n {max}")
print(f"Герой 2:\n {danya}")
print(f"Герой 3:\n {dasha}")
# print(f"Герой 4: {nastya}")

print(f"I have created {Hero.CREATED_COUNT} heroes!")


""" #Old info about heroes before defining __str__(self)
print(
    f"{max.name} has {max.hp} HP and deal damage with {max.weapon} while wearing {max.armor_type}."
)
print(
    f"{danya.name} has {danya.hp} HP and deal damage with {danya.weapon} while wearing {danya.armor_type}."
)
print(
    f"{dasha.name} has {dasha.hp} HP and deal damage with {dasha.weapon} while wearing {dasha.armor_type}."
)
"""
