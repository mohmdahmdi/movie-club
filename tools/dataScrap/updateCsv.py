import csv
import re

# Path to the CSV file
file_path = 'E:/codes/projects/movie-club/tools/csv/movies.csv'
file_path1 = 'E:/codes/projects/movie-club/tools/csv/testMovies.csv'

# Read the CSV and modify a field
rows = []

# Regex for allowed characters
allowed_pattern = re.compile(r'[a-zA-Z0-9\s!@#$%^&*()_+{}\[\]:;<>,.?/~`-]+')

with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Extract allowed characters from the title
        matches = allowed_pattern.findall(row['title'])
        if matches:
            # Join the matches to form the cleaned title
            cleaned_title = ' '.join(matches).strip()
            row['title'] = cleaned_title  # Update the title field
        rows.append(row)  # Store the row (modified or not)

# Write the modified rows back to the CSV
with open(file_path, 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['title', 'year', 'language', 'country', 'studios', 'description', 'rating', 'minute', 'poster']  # Use the same fieldnames as the original file
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()  # Write the header
    csv_writer.writerows(rows)  # Write the updated rows