import csv
import psycopg2
from psycopg2 import extras


def normalize_name(name):
    """Normalize names by stripping whitespace and converting to lowercase."""
    return name.strip().lower()


def fetch_movie_records(conn):
    """Fetch movie records from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, title FROM movie")
    records = cursor.fetchall()
    return {normalize_name(title): movie_id for movie_id, title in records}  # Normalize movie titles


def fetch_cast_records(conn):
    """Fetch cast records from the database."""
    cursor = conn.cursor()
    cursor.execute('SELECT cast_id, name FROM "cast"')
    records = cursor.fetchall()
    return {normalize_name(name): cast_id for cast_id, name in records}  # Normalize cast names


def read_csv(file_path):
    """Read CSV data into a dictionary."""
    movie_cast_data = {}
    skipped_rows = 0

    try:
        with open(file_path, mode="r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    title = normalize_name(row['title'])  # Normalize movie title
                    cast_list = [normalize_name(cast) for cast in row['cast'].split(",")]  # Normalize cast names
                    movie_cast_data[title] = cast_list
                except KeyError:
                    skipped_rows += 1
                    print(f"Skipped row due to missing 'title' or 'cast' column: {row}")
                except Exception as e:
                    skipped_rows += 1
                    print(f"Skipped row due to error: {row} - {e}")

        print(f"Successfully read {len(movie_cast_data)} movies and their casts from CSV.")
        print(f"Total rows skipped: {skipped_rows}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return movie_cast_data


def insert_movie_cast_data(conn, movie_cast_data, movie_records, cast_records):
    """Insert data into the movie_cast table."""
    cursor = conn.cursor()
    inserted_rows = 0
    skipped_rows = 0
    missing_movies = set()
    missing_casts = set()

    try:
        for title, cast_names in movie_cast_data.items():
            if title in movie_records:
                movie_id = movie_records[title]
                for cast_name in cast_names:
                    if cast_name in cast_records:
                        cast_id = cast_records[cast_name]
                        cursor.execute(
                            """
                            INSERT INTO movie_cast (movie_id, cast_id)
                            VALUES (%s, %s)
                            ON CONFLICT (movie_id, cast_id) DO NOTHING
                            """,
                            (movie_id, cast_id)
                        )
                        if cursor.rowcount > 0:  # Check if a row was inserted
                            inserted_rows += 1
                        else:
                            skipped_rows += 1  # Track skipped duplicates
                    else:
                        missing_casts.add(cast_name)  # Track missing cast members
            else:
                missing_movies.add(title)  # Track missing movies

        conn.commit()
        print(f"Successfully inserted {inserted_rows} rows into the movie_cast table.")
        print(f"Skipped {skipped_rows} duplicate rows.")

        # Log missing movies and cast members
        if missing_movies:
            print(f"The following movies were not found in the database: {missing_movies}")
        if missing_casts:
            print(f"The following cast members were not found in the database: {missing_casts}")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting data into movie_cast table: {e}")
    finally:
        cursor.close()


def main():
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'dwxp9415',
        'dbname': 'movie-club'
    }
    csv_path = 'E:/codes/projects/movie-club/tools/csv/movie_cast.csv'

    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        print("Connected to the database.")

        # Fetch movie and cast records
        movie_records = fetch_movie_records(conn)
        cast_records = fetch_cast_records(conn)

        # Read data from CSV
        movie_cast_data = read_csv(csv_path)

        # Insert data into the movie_cast table
        if movie_cast_data:
            insert_movie_cast_data(conn, movie_cast_data, movie_records, cast_records)
        else:
            print("No data to insert.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == '__main__':
    main()