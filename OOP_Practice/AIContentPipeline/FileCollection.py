from FileReader import FileReader
from functools import total_ordering
import fnmatch


@total_ordering
class FileCollection:
    def __init__(self, name: str) -> None:
        self.name = name
        self._files: list[FileReader] = []
        self._processing = False

    def add(self, file: FileReader) -> None:
        """Add file to collection"""
        self._files.append(file)

    def __str__(self) -> str:
        """User description"""
        return f"Collection '{self.name}' ({len(self)} file(s))"

    def __repr__(self) -> str:
        files = [f.filename for f in self._files]
        return f"FileCollection('{self.name}', {files})"

    def __bool__(self) -> bool:
        """Empty collection = False."""
        return len(self._files) > 0

    def __len__(self) -> int:
        """Quantity of files."""
        return len(self._files)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FileCollection):
            return NotImplemented
        return {f.source_path for f in self._files} == {
            f.source_path for f in other._files
        }

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, FileCollection):
            return NotImplemented
        return len(self) < len(other)

    def __add__(self, other: object) -> "FileCollection":
        """Creating NEW collection"""
        if not isinstance(other, FileCollection):
            return NotImplemented
        new_collection = FileCollection(f"{self.name} + {other.name}")
        for f in self._files:
            new_collection.add(f)
        for f in other._files:
            new_collection.add(f)
        return new_collection

    def __iadd__(self, other: object) -> "FileCollection":
        """In-place: modifying current"""
        if not isinstance(other, FileCollection):
            return NotImplemented
        for f in other._files:
            self._files.append(f)
        return self

    def __getitem__(self, index):
        """Index search: collection[0], collection[1:3]."""
        return self._files[index]

    def __setitem__(self, index: int, file: FileReader) -> None:
        """Change by index"""
        if not isinstance(file, FileReader):
            raise TypeError("Can only add FileReader!")
        self._files[index] = file

    def __contains__(self, item) -> bool:
        """Check if item exists"""
        if isinstance(item, FileReader):
            return any(f.source_path == item.source_path for f in self._files)
        if isinstance(item, str):
            if item.startswith("."):
                return any(f.extension == item for f in self._files)
            return any(f.filename == item for f in self._files)
        return False

    def __iter__(self):
        return iter(self._files)

    def __call__(self, pattern: str = None, extension: str = None) -> list[FileReader]:
        """File search: collection('*.py'), collection(extension='.yaml')"""
        results = self._files.copy()
        if pattern:
            results = [f for f in results if fnmatch.fnmatch(f.filename, pattern)]
        if extension:
            ext = extension if extension.startswith(".") else f".{extension}"
            results = [f for f in results if f.extension == ext]
        return results

    def __enter__(self) -> "FileCollection":
        """Start batch"""
        print(f"Start of batch: {self.name}")
        self._processing = True
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self._processing = False
        if exc_type:
            print(f"Error: {exc}")
        else:
            processed = sum(1 for f in self._files if f._processed)
            print(f"Successfully done: {processed}/{len(self)}")
        return False


if __name__ == "__main__":
    print("=" * 70)
    print("🏆  ФИНАЛЬНЫЙ АРТЕФАКТ: FileCollection со всеми магическими методами")
    print("=" * 70)
    print()

    # Создаём коллекцию
    project = FileCollection("мой проект")
    project.add(FileReader("# Main logic", "main.py"))
    project.add(FileReader("# Helpers", "utils.py"))
    project.add(FileReader("# Tests", "test_main.py"))
    project.add(FileReader("debug: true", "config.yaml"))
    project.add(FileReader("# Project", "README.md"))

    # ===== Демонстрация всех методов =====

    print("=== __str__ / __repr__ ===")
    print(f"str(project) = {str(project)}")
    print(f"repr(project) = {repr(project)}")
    print()

    print("=== __bool__ / __len__ ===")
    print(f"bool(project) = {bool(project)}")
    print(f"len(project) = {len(project)}")
    empty = FileCollection("пустая")
    print(f"bool(empty) = {bool(empty)}")
    print()

    print("=== Сравнение (@total_ordering) ===")
    other = FileCollection("другая")
    other.add(FileReader("# A", "a.txt"))
    other.add(FileReader("# B", "b.txt"))
    print(f"project > other: {project > other}  ({len(project)} > {len(other)})")
    print(f"project == project: {project == project}")
    print()

    print("=== __add__ ===")
    combined = project + other
    print(f"project + other = {combined}")
    print()

    print("=== __getitem__ ===")
    print(f"project[0] = {project[0]}")
    print(f"project[-1] = {project[-1]}")
    print(f"project[1:3] = {project[1:3]}")
    print()

    print("=== __contains__ ===")
    print(f'"main.py" in project: {"main.py" in project}')
    print(f'".yaml" in project: {".yaml" in project}')
    print(f'"missing.txt" in project: {"missing.txt" in project}')
    print()

    print("=== __iter__ ===")
    print("for file in project:")
    for f in project:
        print(f"  {f.filename}")
    print()

    print("=== __call__ ===")
    print(f'project("*.py") = {project("*.py")}')
    print(f'project(extension=".yaml") = {project(extension=".yaml")}')
    print()

    print("=== __enter__ / __exit__ (контекстный менеджер) ===")
    with project as batch:
        for f in batch("*.py"):
            f.process()

    print()
    print("=" * 70)
    print("🎉 Все магические методы работают! FileCollection полностью")
    print("   интегрирован с Python — используется как встроенный тип.")
    print("=" * 70)
