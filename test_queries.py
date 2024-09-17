from query_methods import (
    get_band_for_concert,
    get_venue_for_concert,
    get_concerts_for_venue,
    get_bands_for_venue,
    get_concerts_for_band,
    get_venues_for_band
)


def test_queries():
    band = get_band_for_concert(1)
    print(f"Band: {band}")

    venue = get_venue_for_concert(1)
    print(f"Venue: {venue}")

    concerts = get_concerts_for_venue(1)
    print(f"Concerts for venue: {concerts}")

    bands = get_bands_for_venue(1)
    print(f"Bands for venue: {bands}")

    concerts = get_concerts_for_band(1)
    print(f"Concerts for band: {concerts}")

    venues = get_venues_for_band(1)
    print(f"Venues for band: {venues}")


if __name__ == "__main__":
    test_queries()

