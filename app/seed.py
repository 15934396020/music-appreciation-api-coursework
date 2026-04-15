from sqlalchemy.orm import Session

from app.models.entities import Genre, Track


GENRES = [
    {"name": "Classical", "description": "Classical and orchestral music."},
    {"name": "Jazz", "description": "Jazz standards and improvisational music."},
    {"name": "Ambient", "description": "Atmospheric and meditative soundscapes."},
    {"name": "Folk", "description": "Acoustic and traditional singer-songwriter music."},
    {"name": "Electronic", "description": "Electronic and synth-based tracks."},
]

TRACKS = [
    {"title": "Clair de Lune", "artist_name": "Claude Debussy", "album_title": "Suite bergamasque", "duration_seconds": 300, "mood": "dreamy", "play_count": 1500, "genre_name": "Classical"},
    {"title": "Gymnopédie No.1", "artist_name": "Erik Satie", "album_title": "Gymnopédies", "duration_seconds": 210, "mood": "calm", "play_count": 1200, "genre_name": "Classical"},
    {"title": "Take Five", "artist_name": "The Dave Brubeck Quartet", "album_title": "Time Out", "duration_seconds": 324, "mood": "cool", "play_count": 1800, "genre_name": "Jazz"},
    {"title": "So What", "artist_name": "Miles Davis", "album_title": "Kind of Blue", "duration_seconds": 545, "mood": "reflective", "play_count": 1950, "genre_name": "Jazz"},
    {"title": "An Ending", "artist_name": "Brian Eno", "album_title": "Apollo", "duration_seconds": 260, "mood": "spacious", "play_count": 980, "genre_name": "Ambient"},
    {"title": "Weightless", "artist_name": "Marconi Union", "album_title": "Weightless", "duration_seconds": 505, "mood": "relaxing", "play_count": 1340, "genre_name": "Ambient"},
    {"title": "Scarborough Fair", "artist_name": "Simon & Garfunkel", "album_title": "Parsley, Sage, Rosemary and Thyme", "duration_seconds": 220, "mood": "nostalgic", "play_count": 1420, "genre_name": "Folk"},
    {"title": "Blowin' in the Wind", "artist_name": "Bob Dylan", "album_title": "The Freewheelin' Bob Dylan", "duration_seconds": 168, "mood": "thoughtful", "play_count": 1650, "genre_name": "Folk"},
    {"title": "Windowlicker", "artist_name": "Aphex Twin", "album_title": "Windowlicker", "duration_seconds": 387, "mood": "restless", "play_count": 1100, "genre_name": "Electronic"},
    {"title": "Teardrop", "artist_name": "Massive Attack", "album_title": "Mezzanine", "duration_seconds": 331, "mood": "melancholic", "play_count": 1760, "genre_name": "Electronic"},
]


def seed_initial_data(db: Session) -> None:
    if db.query(Genre).count() > 0:
        return

    genre_map = {}
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
