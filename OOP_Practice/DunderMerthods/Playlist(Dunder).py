from random import shuffle
from typing import Any


class Track:
    def __init__(self, name: str, artist: str, duration: int) -> None:
        self.name = name
        self.artist = artist
        self.duration = duration
        pass

    def __repr__(self) -> str:
        mins, secs = divmod(self.duration, 60)
        return f"Track('{self.name}' by {self.artist}, {mins}:{secs:02d})"

    def __str__(self) -> str:
        mins, secs = divmod(self.duration, 60)
        return f"🎵 {self.artist} — {self.name} ({mins}:{secs:02d})"


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tracks: list[Track] = []
        self._mode = "normal"

    @property
    def total_duration(self) -> int:
        return sum(t.duration for t in self.tracks)

    @property
    def mode(self):
        return self._mode

    def __str__(self) -> str:
        mins, secs = divmod(self.total_duration, 60)
        hours, mins = divmod(mins, 60)
        if hours:
            return f"Playlist: {self.name}, {hours}:{mins:02d}:{secs:02d}"
        else:
            return f"Playlist: {self.name}, {mins}:{secs:02d}"

    def __repr__(self) -> str:
        tracks = [t.name for t in self.tracks[:3]]
        if len(self.tracks) > 3:
            tracks.append("...")
        return f"Playlist('{self.name}', {tracks})"

    def __len__(self):
        return len(self.tracks)

    def __bool__(self):
        return len(self.tracks) > 0

    def add(self, track: Track) -> None:
        self.tracks.append(track)

    def __add__(self, other) -> "Playlist":
        new_playlist = Playlist(f"{self.name} + {other.name}")
        for track in self.tracks:
            new_playlist.add(track)
        for track in other.tracks:
            new_playlist.add(track)
        return new_playlist

    def __contains__(self, item):
        if not self.tracks:
            return False
        if isinstance(item, str):
            return any(t.name == item for t in self.tracks)
        if isinstance(item, Track):
            return item in self.tracks
        return False

    def __getitem__(self, key):
        return self.tracks[key]

    def __iter__(self):
        return PlaylistIterator(self.tracks, self._mode)

    def __call__(self, mode: str) -> Any:
        valid_modes = {"normal", "shuffle", "repeat_one", "repeat_all"}
        if mode not in valid_modes:
            raise ValueError(f"Неверный режим. Допустимые: {valid_modes}")
        self._mode = mode
        return self


class PlaylistIterator:
    def __init__(self, tracks: list[Track], mode: str = "normal") -> None:
        self.mode = mode
        self._current_index = 0
        self._repeat_count = 0
        self._max_repeats = 7

        if mode == "shuffle":
            self.tracks = tracks.copy()
            shuffle(self.tracks)
        else:
            self.tracks = tracks

    def __iter__(self):
        return self

    def __next__(self):
        if self.mode == "repeat_one":
            self._repeat_count += 1
            if self._repeat_count > self._max_repeats:
                raise StopIteration
            if self.tracks:
                return self.tracks[0]
            raise StopIteration

        if self.mode == "repeat_all":
            if not self.tracks:
                raise StopIteration
            if self._current_index >= len(self.tracks):
                self._current_index = 0
                self._repeat_count += 1
                if self._repeat_count >= self._max_repeats:
                    raise StopIteration
            track = self.tracks[self._current_index]
            self._current_index += 1
            return track

        if self._current_index >= len(self.tracks):
            raise StopIteration

        track = self.tracks[self._current_index]
        self._current_index += 1
        return track


if __name__ == "__main__":
    print("=" * 60)
    print("🎵 ЭТАЛОН: Playlist с итератором и режимами")
    print("=" * 60)
    print()

    # Создаём плейлист
    rock = Playlist("Rock Classics")
    rock.add(Track("Bohemian Rhapsody", "Queen", 354))
    rock.add(Track("Stairway to Heaven", "Led Zeppelin", 482))
    rock.add(Track("Hotel California", "Eagles", 391))
    rock.add(Track("Sweet Child O' Mine", "Guns N' Roses", 356))
    rock.add(Track("Comfortably Numb", "Pink Floyd", 382))

    print(f"Плейлист: {rock}")
    print(f"repr: {repr(rock)}")
    print()

    # __len__
    print(f"len(rock) = {len(rock)} треков")
    print()

    # __contains__
    print("=== Поиск треков ===")
    print(f'"Bohemian" in rock: {"Bohemian" in rock}')
    print(f'"Yesterday" in rock: {"Yesterday" in rock}')
    print()

    # __getitem__
    print("=== Индексация ===")
    print(f"rock[0] = {rock[0]}")
    print(f"rock[-1] = {rock[-1]}")
    print()

    # __iter__ (normal mode)
    print("=== Режим: normal ===")
    rock("normal")
    for i, track in enumerate(rock):
        print(f"  {i + 1}. {track}")
        if i >= 2:
            print("  ...")
            break
    print()

    # __iter__ (shuffle mode)
    print("=== Режим: shuffle ===")
    rock("shuffle")
    print(f"Плейлист: {rock}")
    for i, track in enumerate(rock):
        print(f"  {i + 1}. {track}")
    print()

    # __iter__ (repeat_one mode)
    print("=== Режим: repeat_one (с ограничением) ===")
    rock("repeat_one")
    for i, track in enumerate(rock):
        print(f"  Повтор {i + 1}: {track}")
    print()

    # __add__
    print("=== Объединение плейлистов ===")
    jazz = Playlist("Jazz Essentials")
    jazz.add(Track("Take Five", "Dave Brubeck", 324))
    jazz.add(Track("So What", "Miles Davis", 545))

    combined = rock + jazz
    print(f"rock + jazz = {combined}")
    print()

    # __call__ — fluent interface
    print("=== Fluent interface ===")
    print('rock("shuffle") возвращает self, можно делать цепочки:')
    print(f'rock("normal").mode = {rock("normal").mode}')
