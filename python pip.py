from typing import List
import random

class Audio:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
        self._ratings: List[int] = []

    def play(self):
        # In a real app you might stream the URL
        print(f"▶️ Playing '{self.title}' from {self.url}")

    def add_rating(self, rating: int):
        if 1 <= rating <= 5:
            self._ratings.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")

    @property
    def average_rating(self) -> float:
        if not self._ratings:
            return 0.0
        return sum(self._ratings) / len(self._ratings)


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.audios: List[Audio] = []
        self._ratings: List[int] = []

    def add_audio(self, audio: Audio):
        self.audios.append(audio)

    def search_audio(self, title: str) -> List[Audio]:
        return [a for a in self.audios if title.lower() in a.title.lower()]

    def add_rating(self, rating: int):
        if 1 <= rating <= 5:
            self._ratings.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")

    @property
    def average_rating(self) -> float:
        if not self._ratings:
            return 0.0
        return sum(self._ratings) / len(self._ratings)


class User:
    def __init__(self, username: str):
        self.username = username

    def rate_audio(self, audio: Audio, rating: int):
        audio.add_rating(rating)

    def rate_playlist(self, playlist: Playlist, rating: int):
        playlist.add_rating(rating)


class MusicPlayer:
    def __init__(self):
        self.playlists: List[Playlist] = []
        self.users: List[User] = []

    def create_user(self, username: str) -> User:
        user = User(username)
        self.users.append(user)
        return user

    def create_audio(self, title: str, url: str) -> Audio:
        return Audio(title, url)

    def create_playlist(self, name: str) -> Playlist:
        pl = Playlist(name)
        self.playlists.append(pl)
        return pl

    def search_playlists(self, name: str) -> List[Playlist]:
        return [pl for pl in self.playlists if name.lower() in pl.name.lower()]

    def search_audio_in_all(self, title: str) -> List[Audio]:
        found = []
        for pl in self.playlists:
            found.extend(pl.search_audio(title))
        return found


# Example usage:
if __name__ == "__main__":
    player = MusicPlayer()
    # create users
    for uname in ("alice", "bob", "carol"):
        player.create_user(uname)
    # create some audio and a playlist
    a1 = player.create_audio("Song A", "https://example.com/a.mp3")
    a2 = player.create_audio("Ballad B", "https://example.com/b.mp3")
    pop_pl = player.create_playlist("Pop Hits")
    pop_pl.add_audio(a1)
    pop_pl.add_audio(a2)
    # generate random ratings for demonstration
    for user in player.users:
        user.rate_audio(a1, random.randint(1, 5))
        user.rate_audio(a2, random.randint(1, 5))
        user.rate_playlist(pop_pl, random.randint(1, 5))

    print(f"{a1.title} avg rating: {a1.average_rating:.2f}")
    print(f"{a2.title} avg rating: {a2.average_rating:.2f}")
    print(f"Playlist '{pop_pl.name}' avg rating: {pop_pl.average_rating:.2f}")
