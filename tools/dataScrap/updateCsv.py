import csv
import re

# Path to the CSV file
file_path = 'E:/codes/projects/movie-club/tools/csv/movies.csv'
file_path1 = 'E:/codes/projects/movie-club/tools/csv/testMovies.csv'

# Read the CSV and modify a field
rows = []
exclude_arabic_persian = re.compile(r'([^\u0600-\u06FF]+)$')

# Regex for allowed characters
allowed_pattern = re.compile(r"([a-zA-Z0-9%^@%&'\"’\-_.:\(\)\[\]\{\} ]+)$")


with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        match = exclude_arabic_persian.search(row['title']) # Find the row to modify
        if match and allowed_pattern.match(row['title']):
          row['title'] = match.group(1)   # Update the field
        rows.append(row)         # Store the row (modified or not)

# Write the modified rows back to the CSV
with open(file_path1, 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['title', 'year', 'language', 'country', 'studios', 'description', 'rating', 'minute', 'poster']  # Use the same fieldnames as the original file
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()  # Write the header
    csv_writer.writerows(rows)  # Write the updated rows