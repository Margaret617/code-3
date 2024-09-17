# Concerts Database Management System
This project is a Python application that manages a concert database using SQLite. The application uses raw SQL queries to interact with the database. The database schema includes three primary tables: bands, venues, and concerts.

## Project Overview
The system handles the following entities:

- Bands: Represent musical groups.
- Venues: Locations where concerts are held.
- Concerts: Events that link bands and venues.
## Schema
### bands Table
id (INTEGER, Primary Key): Unique identifier for the band.
name (TEXT): The name of the band.
hometown (TEXT): The hometown of the band.
### venues Table
id (INTEGER, Primary Key): Unique identifier for the venue.
title (TEXT): The title of the venue.
city (TEXT): The city where the venue is located.
### concerts Table
id (INTEGER, Primary Key): Unique identifier for the concert.
band_id (INTEGER, Foreign Key): References bands.id.
venue_id (INTEGER, Foreign Key): References venues.id.
date (TEXT): The date of the concert.
#### Setup Instructions
1. Install Dependencies
Ensure you have Python 3.x installed. The project uses SQLite, which is included with Python’s standard library.

2. Create and Initialize the Database
Run Database Setup

To create the database and tables, execute the db_setup.py script:

bash
Copy code
python db_setup.py
This script sets up the bands, venues, and concerts tables in the concerts.db SQLite database.

3. Test the Functionality
Run the Test Script

To verify the functionality of the methods, run the test_script.py script:

bash
Copy code
python test_script.py
This script demonstrates how to use the various methods provided in the application.

#### Available Methods
##### Concert Methods
concert_band(concert_id): Retrieves the band details for a specific concert.
concert_venue(concert_id): Retrieves the venue details for a specific concert.
##### Venue Methods
venue_concerts(venue_id): Retrieves all concerts held at a specific venue.
venue_bands(venue_id): Retrieves all bands that have performed at a specific venue.
##### Band Methods
band_concerts(band_id): Retrieves all concerts performed by a specific band.
band_venues(band_id): Retrieves all venues where a specific band has performed.
#### Aggregate and Relationship Methods
##### Concert
concert_hometown_show(concert_id): Checks if the concert is in the band’s hometown.
concert_introduction(concert_id): Provides a string introduction for the band at the concert location.
##### Band
band_play_in_venue(band_id, venue_title, date): Adds a new concert entry for the band at a specified venue on a given date.
band_all_introductions(band_id): Returns all introductions for the band.
band_most_performances(): Identifies the band with the most concerts.
##### Venue
venue_concert_on(date): Finds the first concert on a specified date at the venue.
venue_most_frequent_band(venue_id): Identifies the band that has performed the most at a given venue.
#### How to Use
- Setup: Follow the setup instructions to create and initialize the database.
- Testing: Use the test_script.py to run examples and verify the methods.
- Development: Modify or extend the methods as needed by updating the corresponding Python files.
