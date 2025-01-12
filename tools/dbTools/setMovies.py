import csv
import psycopg2
from psycopg2 import sql, extras

def insert_data(conn, data):
    cursor = conn.cursor()
    try:
        # Use execute_batch for better performance
        extras.execute_batch(cursor, '''
            INSERT INTO movie (title, year, language, country, studios, description, rating, minute, poster)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', data)
        conn.commit()
        print(f"Successfully inserted {len(data)} rows.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode="r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Handle 'year' column
                    year = int(row['year']) if row['year'] and row['year'].lower() != 'unknown' else None
                except (ValueError, KeyError):
                    year = None

                try:
                    # Handle 'minute' column
                    minute = int(row['minute']) if row['minute'] and row['minute'].lower() != 'unknown' else None
                except (ValueError, KeyError):
                    minute = None

                try:
                    # Handle 'rating' column
                    rating = float(row['rating']) if row['rating'] and row['rating'].lower() != 'unknown' else None
                except (ValueError, KeyError):
                    rating = None

                # Handle 'country' column (convert to text[])
                countries = row.get('country', '').split(',')
                country = [country.strip() for country in countries if country.strip()]

                # Append the row to data
                data.append((
                    row.get('title'),
                    year,
                    row.get('language'),
                    country,
                    row.get('studios'),
                    row.get('description'),
                    rating,
                    minute,
                    row.get('poster')
                ))
        print(f"Successfully read {len(data)} rows from CSV.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

def main():
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'dwxp9415',
        'dbname': 'movie-club'
    }
    csv_path = 'E:/codes/projects/movie-club/tools/csv/movies.csv'

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