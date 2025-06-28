# Simple Spotify Artist ETL & Analytics

This project is a simple ETL (Extract, Transform, Load) pipeline for collecting, cleaning, and analyzing Indonesian music artist data from the Spotify API using Python and SQL. It is designed for learning and portfolio purposes, and can run on low-resource computers (no Airflow or Docker required).

## Main Features

- **Extract:** Retrieve artist, album, and top track data from the Spotify API for multiple artists at once.
- **Transform:** Clean and normalize the data into relational tables (artist, album, track, genre, and many-to-many relationship tables).
- **Load:** Load the transformed data into a SQLite database.
- **EDA (Exploratory Data Analysis):** Analyze the data using SQL directly in a Jupyter Notebook, including:
  - Top tracks, artists, albums, and genres
  - Popularity distribution
  - Insights on solo vs. collaboration albums
  - Average track duration, and more

## Folder Structure

```
src/
  extract.py        # Extract data from Spotify API
  transform.py      # Transform and normalize data
  load.py           # Load data into SQLite
  EDA.ipynb         # Data exploration with SQL
  hindia_spotify.db # SQLite database
  env               # Spotify API credentials
data/
  artist_*.json     # Raw extract per artist
  albums_*.json
  top_tracks_*.json
  artist.csv        # Normalized tables
  album.csv
  track.csv
  artist_genre.csv
  album_artist.csv
  track_artist.csv
```

## How to Run

1. **Clone the repo & install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare the `env` file**  
   Fill with:
   ```
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   ```

3. **Extract data from Spotify**
   ```bash
   python src/extract.py
   ```

4. **Transform & normalize the data**
   ```bash
   python src/transform.py
   ```

5. **Load into SQLite database**
   ```bash
   python src/load.py
   ```

6. **Explore the data in Jupyter Notebook**
   ```bash
   jupyter notebook src/EDA.ipynb
   ```

## Possible Insights

- Which artist has the most followers?
- What are the most popular genres?
- Which tracks and albums are the most popular?
- Comparison of solo vs. collaboration albums
- Average track duration per artist
- And more, as needed!

## Notes

- This project does not use Airflow, Docker, or cloud databases to keep it lightweight and easy to run on any machine.
- Data is for educational and non-commercial use only.

---

**Data Engineering Portfolio**  
This project demonstrates ETL, data normalization, pipeline automation, and SQL-based data exploration skills.

---

Feel free to open an issue or pull request if you want to contribute or have questions!
