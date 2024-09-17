import sqlite3


def get_band_for_concert(concert_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (concert_id,))
    band = cursor.fetchone()
    conn.close()
    return band


def get_venue_for_concert(concert_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (concert_id,))
    venue = cursor.fetchone()
    conn.close()
    return venue


def get_concerts_for_venue(venue_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (venue_id,))
    concerts = cursor.fetchall()
    conn.close()
    return concerts


def get_bands_for_venue(venue_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (venue_id,))
    bands = cursor.fetchall()
    conn.close()
    return bands


def get_concerts_for_band(band_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (band_id,))
    concerts = cursor.fetchall()
    conn.close()
    return concerts


def get_venues_for_band(band_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        (band_id,))
    venues = cursor.fetchall()
    conn.close()
    return venues
