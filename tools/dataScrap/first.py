import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://digimoviez.com/"
res = requests.get(base_url)

soup = BeautifulSoup(res.text)
divs = soup.find_all('div', class_='plot_text')
# complete the expectations and write in a csv file

for i in range(1, 862):
  movie_url = base_url + f'page/{i}/'
  res = requests.get(movie_url)
  soup = BeautifulSoup(res.text)
  divs = soup.find_all('div', class_='plot_text') #
  
  # complete the expectations and write in a csv file

for div in divs:
    print(div.prettify())


















################################################################
# class MovieScraper:
#   def __init__(self, base_url):
#     self.base_url = base_url

#   def fetch_page(self, url):
#     response = requests.get(url)
#     if response.status_code == 200:
#       return response.text
#     else:
#       return None

#   def parse_movie_data(self, html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     movies = []
#     for movie in soup.find_all('div', class_='movie'):
#       title = movie.find('h2').text
#       rating = movie.find('span', class_='rating').text
#       movies.append({'title': title, 'rating': rating})
#     return movies

#   def scrape_movies(self):
#     html_content = self.fetch_page(self.base_url)
#     if html_content:
#       return self.parse_movie_data(html_content)
#     else:
#       return []

# # Example usage:
# # base_url = 'https://example-movie-site.com'
# # scraper = MovieScraper(base_url)
# # movies = scraper.scrape_movies()
# # for movie in movies:
# #   print(f"Title: {movie['title']}, Rating: {movie['rating']}")
# # Example usage:
# base_url = 'https://example-movie-site.com'
# scraper = MovieScraper(base_url)
# movies = scraper.scrape_movies()

# # Write to CSV file
# csv_file = 'movies.csv'
# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#   writer = csv.DictWriter(file, fieldnames=['title', 'rating'])
#   writer.writeheader()
#   for movie in movies:
#     writer.writerow(movie)

# print(f"Data has been written to {csv_file}")