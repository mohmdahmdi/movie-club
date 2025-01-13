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


def fetch_crew_records(conn):
    """Fetch crew records from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT crew_id, name FROM crew")
    records = cursor.fetchall()
    return {normalize_name(name): crew_id for crew_id, name in records}  # Normalize crew names


def read_csv(file_path):
    """Read CSV data into a dictionary."""
    movie_crew_data = {}
    skipped_rows = 0

    try:
        with open(file_path, mode="r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    title = normalize_name(row['title'])  # Normalize movie title
                    crew_list = [normalize_name(crew) for crew in row['crew'].split(",")]  # Normalize crew names
                    movie_crew_data[title] = crew_list
                except KeyError:
                    skipped_rows += 1
                    print(f"Skipped row due to missing 'title' or 'crew' column: {row}")
                except Exception as e:
                    skipped_rows += 1
                    print(f"Skipped row due to error: {row} - {e}")

        print(f"Successfully read {len(movie_crew_data)} movies and their crews from CSV.")
        print(f"Total rows skipped: {skipped_rows}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return movie_crew_data


def insert_movie_crew_data(conn, movie_crew_data, movie_records, crew_records):
    """Insert data into the movie_crew table."""
    cursor = conn.cursor()
    inserted_rows = 0
    missing_movies = set()
    missing_crews = set()

    try:
        for title, crew_names in movie_crew_data.items():
            if title in movie_records:
                movie_id = movie_records[title]
                for crew_name in crew_names:
                    if crew_name in crew_records:
                        crew_id = crew_records[crew_name]
                        cursor.execute(
                            "INSERT INTO movie_crew (movie_id, crew_id) VALUES (%s, %s)",
                            (movie_id, crew_id)
                        )
                        inserted_rows += 1
                    else:
                        missing_crews.add(crew_name)  # Track missing crew members
            else:
                missing_movies.add(title)  # Track missing movies

        conn.commit()
        print(f"Successfully inserted {inserted_rows} rows into the movie_crew table.")

        # Log missing movies and crew members
        if missing_movies:
            print(f"The following movies were not found in the database: {missing_movies}")
        if missing_crews:
            print(f"The following crew members were not found in the database: {missing_crews}")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting data into movie_crew table: {e}")
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
    csv_path = 'E:/codes/projects/movie-club/tools/csv/movie_crew.csv'

    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        print("Connected to the database.")

        # Fetch movie and crew records
        movie_records = fetch_movie_records(conn)
        crew_records = fetch_crew_records(conn)

        # Read data from CSV
        movie_crew_data = read_csv(csv_path)

        # Insert data into the movie_crew table
        if movie_crew_data:
            insert_movie_crew_data(conn, movie_crew_data, movie_records, crew_records)
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