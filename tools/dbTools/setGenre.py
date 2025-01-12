import csv
import psycopg2
from psycopg2 import extras

def insert_data(conn, data):
    cursor = conn.cursor()
    try:
        # Use execute_batch for better performance
        extras.execute_batch(cursor, '''
            INSERT INTO genre (name)
            VALUES (%s)
        ''', [(genre,) for genre in data])  # Convert set to list of tuples
        conn.commit()
        print(f"Successfully inserted {len(data)} rows.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

def read_csv(file_path):
    genres = set()  # Use a set to store unique genres
    skipped_rows = 0

    try:
        with open(file_path, mode="r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    genreList = row['genre'].strip().split(",")
                    genres1 = [genre.strip() for genre in genreList]
                    # Remove leading/trailing whitespace
                    if genres1 and genres1[0] != 'unknown':  # Only add non-empty genres
                        for genre in genres1:
                            genres.add(genre)
                    else:
                        skipped_rows += 1
                        print(f"Skipped row due to empty genre: {row}")
                except KeyError:
                    skipped_rows += 1
                    print(f"Skipped row due to missing 'genre' column: {row}")
                except Exception as e:
                    skipped_rows += 1
                    print(f"Skipped row due to error: {row} - {e}")
        
        print(f"Successfully read {len(genres)} unique genres from CSV.")
        print(f"Total rows skipped: {skipped_rows}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return genres

def main():
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'dwxp9415',
        'dbname': 'movie-club'
    }
    csv_path = 'E:/codes/projects/movie-club/tools/csv/movie_genre.csv'

    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        print("Connected to the database.")

        # Read data from CSV
        data = read_csv(csv_path)

        # Insert data into the database
        if data:
            insert_data(conn, data)
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