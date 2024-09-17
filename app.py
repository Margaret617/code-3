import sqlite3


class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    def band(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute( 
                       (self.concert_id,))
        band = cursor.fetchone()
        conn.close()
        return Band(*band) if band else None

    def venue(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT venues.id, venues.title, venues.city
            FROM venues
            JOIN concerts ON venues.id = concerts.venue_id
            WHERE concerts.id = ?
        ''', (self.concert_id,))
        venue = cursor.fetchone()
        conn.close()
        return Venue(*venue) if venue else None


class Venue:
    def __init__(self, venue_id, title=None, city=None):
        self.venue_id = venue_id
        self.title = title
        self.city = city

    def concerts(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM concerts WHERE venue_id = ?', (self.venue_id,))
        concerts = cursor.fetchall()
        conn.close()
        return [Concert(c[0]) for c in concerts]

    def bands(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT bands.id, bands.name, bands.hometown
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
        ''', (self.venue_id,))
        bands = cursor.fetchall()
        conn.close()
        return [Band(*band) for band in bands]


class Band:
    def __init__(self, band_id, name=None, hometown=None):
        self.band_id = band_id
        self.name = name
        self.hometown = hometown

    def concerts(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM concerts WHERE band_id = ?', (self.band_id,))
        concerts = cursor.fetchall()
        conn.close()
        return [Concert(c[0]) for c in concerts]

    def venues(self):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT venues.id, venues.title, venues.city
            FROM venues
            JOIN concerts ON venues.id = concerts.venue_id
            WHERE concerts.band_id = ?
        ''', (self.band_id,))
        venues = cursor.fetchall()
        conn.close()
        return [Venue(*venue) for venue in venues]

    def play_in_venue(self, venue_title, date):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM venues WHERE title = ?', (venue_title,))
        venue_id = cursor.fetchone()
        if venue_id:
            cursor.execute('''
                INSERT INTO concerts (band_id, venue_id, date)
                VALUES (?, ?, ?)
            ''', (self.band_id, venue_id[0], date))
            conn.commit()
        conn.close()

    def all_introductions(self):
        return [
            f"Hello {venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for venue in self.venues()
        ]

if __name__ == "__main__":
    # Setup database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_id INTEGER,
            venue_id INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        )
    ''')
    conn.commit()
    conn.close()

    # Insert sample data
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bands (name, hometown) VALUES (?, ?)', ('BeatleJuice', 'New York'))
    cursor.execute('INSERT INTO venues (title, city) VALUES (?, ?)', ('Royal Albert Hall', 'London'))
    cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', (1, 1, '2024-09-30'))
    conn.commit()
    conn.close()

    band = Band(1, 'BeatleJuice', 'New York')
    venue = Venue(1, 'Royal Albert Hall', 'London')
    concert = Concert(1)

    print("Band for Concert 1:", concert.band().name)
    print("Venue for Concert 1:", concert.venue().title)
    print("Concerts at Venue 1:", [c.concert_id for c in venue.concerts()])
    print("Bands at Venue 1:", [b.name for b in venue.bands()])
    print("Concerts for Band 1:", [c.concert_id for c in band.concerts()])
    print("Venues for Band 1:", [v.title for v in band.venues()])
    band.play_in_venue('Royal Albert Hall', '2024-10-01')
    print("Introductions for Band 1:", band.all_introductions())
