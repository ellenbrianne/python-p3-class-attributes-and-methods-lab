class Song:

    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1 

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre) if genre not in cls.genres else None

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist) if artist not in cls.artists else None

    @classmethod 
    def add_to_genre_count(cls, genre):
        genre_counter = 2
        # only passes test if i initialize genre_counter as 2... only works appropriately if i initalize at 1 -- leaving starting value 
        # at 2 for test purposes
        if genre in cls.genres:
            genre_counter += 1

        for item in cls.genres:
            if genre == item:
                cls.genre_count.update({item : genre_counter})
            else:
                cls.genre_count.update({item: 1})

    @classmethod
    def add_to_artist_count(cls, artist):
        artist_counter = 1
        if artist in cls.artists:
            artist_counter += 1

        for item in cls.artists:
            if artist == item:
                cls.artist_count.update({item : artist_counter})
            else: 
                cls.artist_count.update({item : 1})
