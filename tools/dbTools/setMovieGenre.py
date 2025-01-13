import psycopg2
import csv


def fetch_movie_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM films")
    records = cursor.fetchall()
    return {name: id for id, name in records}


def fetch_genre_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM genres")
    records = cursor.fetchall()
    return {name.strip(): id for id, name in records}


def load_csv_data(file_path):
    movie_genres = {}
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if 'category' not in reader.fieldnames:
                raise KeyError("Missing 'category' column in CSV.")
            for entry in reader:
                categories = [category.strip() for category in entry['category'].split(',')]
                movie_genres[entry['film']] = categories
    except Exception as e:
        print(f"Error: {e}")
        return {}
    return movie_genres


def update_genre_associations(connection, movie_genres, film_records, genre_records):
    cursor = connection.cursor()
    for film, categories in movie_genres.items():
        if film in film_records:
            film_id = film_records[film]
            for category in categories:
                if category in genre_records:
                    genre_id = genre_records[category]
                    cursor.execute(
                        "INSERT INTO film_genres (film_id, genre_id) VALUES (%s, %s)",
                        (film_id, genre_id)
                    )
    connection.commit()


def execute():
    db_config = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'dwxp9415',
        'dbname': 'movie-club'
    }
    csv_file_path = 'E:/codes/projects/movie-club/tools/csv/movie_genre.csv'

    try:
        db_connection = psycopg2.connect(**db_config)
        films = fetch_movie_records(db_connection)
        genres = fetch_genre_records(db_connection)
        csv_data = load_csv_data(csv_file_path)
        if csv_data:
            update_genre_associations(db_connection, csv_data, films, genres)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if db_connection:
            db_connection.close()


if __name__ == '__main__':
    execute()