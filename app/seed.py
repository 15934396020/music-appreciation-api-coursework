"""Seed data module — populates the database with initial genres and tracks."""

from sqlalchemy.orm import Session

from app.models.entities import Genre, Track


GENRES = [
    {"name": "Classical", "description": "Classical and orchestral music spanning Baroque to modern eras."},
    {"name": "Jazz", "description": "Jazz standards, improvisational pieces, and fusion experiments."},
    {"name": "Ambient", "description": "Atmospheric and meditative soundscapes for deep listening."},
    {"name": "Folk", "description": "Acoustic and traditional singer-songwriter music rooted in storytelling."},
    {"name": "Electronic", "description": "Electronic and synth-based tracks from IDM to house."},
    {"name": "Rock", "description": "Guitar-driven music from classic rock to alternative and indie."},
    {"name": "Blues", "description": "Expressive vocal and guitar music rooted in African-American tradition."},
    {"name": "World", "description": "Traditional and contemporary music from diverse global cultures."},
]

TRACKS = [
    # Classical
    {"title": "Clair de Lune", "artist_name": "Claude Debussy", "album_title": "Suite bergamasque", "duration_seconds": 300, "mood": "dreamy", "play_count": 1500, "genre_name": "Classical"},
    {"title": "Gymnopédie No.1", "artist_name": "Erik Satie", "album_title": "Gymnopédies", "duration_seconds": 210, "mood": "calm", "play_count": 1200, "genre_name": "Classical"},
    {"title": "Canon in D", "artist_name": "Johann Pachelbel", "album_title": "Canon and Gigue", "duration_seconds": 330, "mood": "elegant", "play_count": 2100, "genre_name": "Classical"},
    {"title": "Moonlight Sonata", "artist_name": "Ludwig van Beethoven", "album_title": "Piano Sonata No. 14", "duration_seconds": 900, "mood": "melancholic", "play_count": 1800, "genre_name": "Classical"},
    # Jazz
    {"title": "Take Five", "artist_name": "The Dave Brubeck Quartet", "album_title": "Time Out", "duration_seconds": 324, "mood": "cool", "play_count": 1800, "genre_name": "Jazz"},
    {"title": "So What", "artist_name": "Miles Davis", "album_title": "Kind of Blue", "duration_seconds": 545, "mood": "reflective", "play_count": 1950, "genre_name": "Jazz"},
    {"title": "My Favorite Things", "artist_name": "John Coltrane", "album_title": "My Favorite Things", "duration_seconds": 810, "mood": "uplifting", "play_count": 1400, "genre_name": "Jazz"},
    {"title": "Autumn Leaves", "artist_name": "Bill Evans Trio", "album_title": "Portrait in Jazz", "duration_seconds": 320, "mood": "wistful", "play_count": 1350, "genre_name": "Jazz"},
    # Ambient
    {"title": "An Ending (Ascent)", "artist_name": "Brian Eno", "album_title": "Apollo", "duration_seconds": 260, "mood": "spacious", "play_count": 980, "genre_name": "Ambient"},
    {"title": "Weightless", "artist_name": "Marconi Union", "album_title": "Weightless", "duration_seconds": 505, "mood": "relaxing", "play_count": 1340, "genre_name": "Ambient"},
    {"title": "Music for Airports 1/1", "artist_name": "Brian Eno", "album_title": "Ambient 1: Music for Airports", "duration_seconds": 1020, "mood": "contemplative", "play_count": 870, "genre_name": "Ambient"},
    # Folk
    {"title": "Scarborough Fair", "artist_name": "Simon & Garfunkel", "album_title": "Parsley, Sage, Rosemary and Thyme", "duration_seconds": 220, "mood": "nostalgic", "play_count": 1420, "genre_name": "Folk"},
    {"title": "Blowin' in the Wind", "artist_name": "Bob Dylan", "album_title": "The Freewheelin' Bob Dylan", "duration_seconds": 168, "mood": "thoughtful", "play_count": 1650, "genre_name": "Folk"},
    {"title": "The Sound of Silence", "artist_name": "Simon & Garfunkel", "album_title": "Wednesday Morning, 3 A.M.", "duration_seconds": 187, "mood": "introspective", "play_count": 1900, "genre_name": "Folk"},
    {"title": "Big Yellow Taxi", "artist_name": "Joni Mitchell", "album_title": "Ladies of the Canyon", "duration_seconds": 145, "mood": "bittersweet", "play_count": 1100, "genre_name": "Folk"},
    # Electronic
    {"title": "Windowlicker", "artist_name": "Aphex Twin", "album_title": "Windowlicker", "duration_seconds": 387, "mood": "restless", "play_count": 1100, "genre_name": "Electronic"},
    {"title": "Teardrop", "artist_name": "Massive Attack", "album_title": "Mezzanine", "duration_seconds": 331, "mood": "melancholic", "play_count": 1760, "genre_name": "Electronic"},
    {"title": "Around the World", "artist_name": "Daft Punk", "album_title": "Homework", "duration_seconds": 427, "mood": "energetic", "play_count": 2200, "genre_name": "Electronic"},
    {"title": "Porcelain", "artist_name": "Moby", "album_title": "Play", "duration_seconds": 238, "mood": "ethereal", "play_count": 1050, "genre_name": "Electronic"},
    # Rock
    {"title": "Bohemian Rhapsody", "artist_name": "Queen", "album_title": "A Night at the Opera", "duration_seconds": 354, "mood": "dramatic", "play_count": 3200, "genre_name": "Rock"},
    {"title": "Stairway to Heaven", "artist_name": "Led Zeppelin", "album_title": "Led Zeppelin IV", "duration_seconds": 482, "mood": "epic", "play_count": 2800, "genre_name": "Rock"},
    {"title": "Hotel California", "artist_name": "Eagles", "album_title": "Hotel California", "duration_seconds": 391, "mood": "mysterious", "play_count": 2500, "genre_name": "Rock"},
    {"title": "Creep", "artist_name": "Radiohead", "album_title": "Pablo Honey", "duration_seconds": 236, "mood": "vulnerable", "play_count": 1900, "genre_name": "Rock"},
    # Blues
    {"title": "The Thrill Is Gone", "artist_name": "B.B. King", "album_title": "Completely Well", "duration_seconds": 338, "mood": "soulful", "play_count": 1600, "genre_name": "Blues"},
    {"title": "Cross Road Blues", "artist_name": "Robert Johnson", "album_title": "King of the Delta Blues Singers", "duration_seconds": 163, "mood": "raw", "play_count": 1250, "genre_name": "Blues"},
    {"title": "Red House", "artist_name": "Jimi Hendrix", "album_title": "Are You Experienced", "duration_seconds": 224, "mood": "groovy", "play_count": 1450, "genre_name": "Blues"},
    # World
    {"title": "Chan Chan", "artist_name": "Buena Vista Social Club", "album_title": "Buena Vista Social Club", "duration_seconds": 302, "mood": "warm", "play_count": 1700, "genre_name": "World"},
    {"title": "Biko", "artist_name": "Peter Gabriel", "album_title": "Peter Gabriel (Melt)", "duration_seconds": 427, "mood": "powerful", "play_count": 1150, "genre_name": "World"},
    {"title": "Misirlou", "artist_name": "Dick Dale", "album_title": "Surfers' Choice", "duration_seconds": 137, "mood": "exhilarating", "play_count": 1850, "genre_name": "World"},
]


def seed_initial_data(db: Session) -> None:
    """Populate the database with starter genres and tracks if empty."""
    if db.query(Genre).count() > 0:
        return

    genre_map: dict[str, int] = {}
    for genre_data in GENRES:
        genre = Genre(**genre_data)
        db.add(genre)
        db.flush()
        genre_map[genre.name] = genre.id

    for track_data in TRACKS:
        genre_name = track_data.pop("genre_name")
        track = Track(**track_data, genre_id=genre_map[genre_name])
        db.add(track)

    db.commit()
