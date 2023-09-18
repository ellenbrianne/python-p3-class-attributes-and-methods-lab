class Song:

    count = 0
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1 

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre) if genre not in cls.genres else None

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist) if artist not in cls.artists else None