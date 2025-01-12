import csv
import psycopg2
from psycopg2 import extras

def insert_data(conn, data):
    cursor = conn.cursor()
    try:
        # Use execute_batch for better performance
        extras.execute_batch(cursor, '''
            INSERT INTO "cast" (name)
            VALUES (%s)
        ''', [(cast.title(),) for cast in data])  # Convert set to list of tuples
        conn.commit()
        print(f"Successfully inserted {len(data)} rows.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

def read_csv(file_path):
    casts = set()  # Use a set to store unique genres
    skipped_rows = 0

    try:
        with open(file_path, mode="r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    castList = row['cast'].strip().split(",")
                    casts1 = [cast.strip() for cast in castList]
                    # Remove leading/trailing whitespace
                    if casts1 and casts1[0] != 'unknown':  # Only add non-empty genres
                        for crew in casts1:
                            casts.add(crew)
                    else:
                        skipped_rows += 1
                        print(f"Skipped row due to empty cast: {row}")
                except KeyError:
                    skipped_rows += 1
                    print(f"Skipped row due to missing 'cast' column: {row}")
                except Exception as e:
                    skipped_rows += 1
                    print(f"Skipped row due to error: {row} - {e}")
        
        print(f"Successfully read {len(casts)} unique casts from CSV.")
        print(f"Total rows skipped: {skipped_rows}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return casts

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