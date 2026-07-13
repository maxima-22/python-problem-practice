import yaml
from pathlib import Path
from typing import Union


class FileReader:
    """
    Universal file reader of project files.
    Supports: .txt, .md, .yaml, .yml
    """

    # Supported formats
    SUPPORTED_FORMATS = [".txt", ".md", ".yaml", ".yml"]

    def __init__(self, content: Union[str, dict], source_path: str = None):
        self.content = content
        self.source_path = source_path
        self.is_yaml = isinstance(content, dict)

    # =============== Fabric methods ====================

    @classmethod
    def from_txt(cls, path: str):
        """Create FileReader from text file"""
        file_path = Path(path)

        if not cls.is_valid_ext(file_path):
            raise ValueError(f"Unsupported file type for from_txt: {file_path.suffix}")

        if not cls.file_exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return cls(content=content, source_path=str(file_path))

    @classmethod
    def from_yaml(cls, path: str):
        """Create FileReader from YAML-file"""
        file_path = Path(path)

        if not cls.is_valid_ext(file_path):
            raise ValueError(f"Unsupported file type for from_yaml: {file_path.suffix}")

        if not cls.file_exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            content = yaml.safe_load(file)

        return cls(content, source_path=str(file_path))

    # =============== Static methods ====================

    @staticmethod
    def is_valid_ext(path: Union[Path, str]) -> bool:
        """
        Check if file has valid format.
        Args:
            path: Path to File
        Returns:
            True if format is valid, else False
        """
        if isinstance(path, str):
            path = Path(path)
        return path.suffix.lower() in FileReader.SUPPORTED_FORMATS

    @staticmethod
    def file_exists(path: Union[Path, str]) -> bool:
        """Check file existance"""
        if isinstance(path, str):
            path = Path(path)
        return path.exists() and path.is_file()

    # =============== Instance methods ====================

    def get_lines(self) -> list[str]:
        """Get list of lines (only for text files)"""
        if self.is_yaml:
            raise TypeError("get_lines() only works with txt files")
        return self.content.splitlines()

    def get_word_count(self) -> int:
        if self.is_yaml:
            raise TypeError("get_word_count() only works with txt files")
        return len(self.content.split())

    def get_data(self) -> Union[str, dict]:
        if not self.is_yaml:
            raise TypeError("get_data() only works with YAML files")
        return self.content

    def display_stats(self):
        print(f"\n{'=' * 50}")
        print(f"File: {self.source_path or 'without path'}")
        print(f"\n{'=' * 50}")
        print(f"Type: {'YAML (dict)' if self.is_yaml else 'Text (str)'}")

        if self.is_yaml:
            print(f"Ключей: {len(self.content)}")
        else:
            print(f"Символов: {len(self.content)}")
            print(f"Строк: {len(self.get_lines())}")
            print(f"Слов: {self.get_word_count()}")
        print(f"{'=' * 50}\n")


class TextHelper:
    "Utility class for text formatting."

    @staticmethod
    def clean_string(text: str) -> str:
        if not text:
            return ""
        text = text.strip()
        text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
        while "  " in text:
            text = text.replace("  ", " ")
        return text

    @staticmethod
    def count_words(text: str) -> int:
        if not text:
            return 0
        cleaned = TextHelper.clean_string(text)
        return len(cleaned.split()) if cleaned else 0

    @staticmethod
    def truncante(text: str, max_length: int, suffix: str = "...") -> str:
        if not text or len(text) <= max_length:
            return text
        cut_at = max_length - len(suffix)
        if cut_at <= 0:
            return suffix[:max_length]
        return text[:cut_at] + suffix


# class ContentChunk:
# class ContentLoader:

if __name__ == "__main__":
    print("\n=== FileReader ===\n")

    # Создаём тестовые файлы
    test_txt = "test_document.txt"
    test_content = """# Заголовок документа

Это первая строка.
Это вторая строка.
Это третья строка.

Это последняя строка.
"""

    with open(test_txt, "w", encoding="utf-8") as f:
        f.write(test_content)

    print("=== Чтение текстового файла ===")
    txt_reader = FileReader.from_txt(test_txt)
    txt_reader.display_stats()

    # Показываем строки
    print("Первые 3 строки:")
    for i, line in enumerate(txt_reader.get_lines()[:3], 1):
        print(f"  {i}. {line}")
    print()

    # Чтение YAML
    config_path = Path(__file__).parent / "ai_pipeline.yaml"

    if config_path.exists():
        print("=== Чтение YAML конфига ===")
        yaml_reader = FileReader.from_yaml(str(config_path))
        yaml_reader.display_stats()

        # Получаем данные
        data = yaml_reader.get_data()
        print("Секции конфига:")
        for key in data.keys():
            print(f"  - {key}")
        print()

    # Демонстрация валидации
    print("=== Валидация файлов ===")
    test_files = ["document.txt", "config.yaml", "data.json", "image.png"]

    for filename in test_files:
        is_valid = FileReader.is_valid_ext(filename)
        status = "✅" if is_valid else "❌"
        print(
            f"{status} {filename:20} — {'поддерживается' if is_valid else 'не поддерживается'}"
        )
    print()

    # Демонстрация обработки ошибок
    print("=== Обработка ошибок ===")
    try:
        reader = FileReader.from_txt("nonexistent.txt")
    except FileNotFoundError as e:
        print(f"❌ {e}")

    try:
        reader = FileReader.from_txt("image.png")
    except ValueError as e:
        print(f"❌ {e}")
    print()

    # Удаляем тестовый файл
    Path(test_txt).unlink()
