import requests
from bs4 import BeautifulSoup
import csv
import re

moviesCsv = "E:/codes/projects/movie-club/tools/csv/movies.csv"
movieCastCsv= "E:/codes/projects/movie-club/tools/csv/movie_cast.csv"
movieCrewCsv= "E:/codes/projects/movie-club/tools/csv/movie_crew.csv"
movieGenreCsv= "E:/codes/projects/movie-club/tools/csv/movie_genre.csv"

for i in range(0, 862):
  # datas
  print("fetch count : " + str(i) + " / 862")
  base_url = f'https://digimoviez.com/page/{i}'

  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  }
  try:
    res = requests.get(base_url, headers=headers, timeout=30)
    soup = BeautifulSoup(res.text)
  except:
    print(f"Error: Failed to fetch the page {i}.")
    continue
  if (res.status_code != 200):
    break

  print("working on data...")
  # holder movie cards list
  holders = soup.find_all('div', class_='item_def_loop')

  # holder of title of movie
  title_holders = [div.find('div', class_='title_h') for div in holders]

  titles_years1 = [holder.select("h2 > a")[0].text for holder in title_holders]

  pattern = re.compile(r'^\S+\s+\S+\s+(.+?)\s+(\d{4})')
  titles_years = [pattern.search(title_year) for title_year in titles_years1]

  titles=[match.group(1) for match in titles_years]
  years=[match.group(2) for match in titles_years]
  #######################################################

  country_list = [div.select(
    "div.meta_loop > div.meta_item > ul > li:nth-of-type(6) > span.res_item"
    ) for div in holders]
  countries = [country[0].text if country else "Unknown" for country in country_list]

  #######################################################

  description_list = [div.select("div.plot_text")[0].text if div else "unknown" for div in holders]
  #######################################################

  rating_list = [div.select("strong")[0].text if div else "unknown" for div in holders]
  #######################################################

  minutes_list = [div.select(
    "div.meta_loop > div.meta_item > ul > li:nth-of-type(2) > span.res_item"
    )[0].text for div in holders]
  minutes_list = [minutes.split(" ")[0] if minutes else "unknown" for minutes in minutes_list]
  #######################################################

  genre_list = [div.select(
    "div.meta_loop > div.meta_item > ul > li:nth-of-type(3) > span.res_item"
    )[0].text if div else "unknown" for div in holders]
  #######################################################

  director_list = [div.select(
    "div.meta_loop > div.meta_item > ul > li:nth-of-type(4) > span.res_item"
    )[0].text if div else "unknown" for div in holders]
  #######################################################

  cast_list = [div.select(
    "div.meta_loop > div.meta_item > ul > li:nth-of-type(5) > span.res_item"
    )[0].text if div else "unknown" for div in holders]
  #######################################################

  poster_list = [div.select("img")[0].get("src") if div else "unknown" for div in holders]
  #######################################################
  
  print("writing on movies.csv...")

  mode = 'w' if i == 0 else 'a'
  
  with open(moviesCsv, mode, newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'year', 'language', 'country', 'studios', 'description', 'rating', 'minute', 'poster']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if i == 0:  # Write header only on the first iteration
      writer.writeheader()
      
    for j in range(0, len(titles)):
      writer.writerow({
        'title': titles[j], 
        'year': years[j],
        'language': "",
        'country': countries[j],
        'studios': "",
        'description': description_list[j],
        'rating': rating_list[j],
        'minute': minutes_list[j],
        'poster': poster_list[j]
        })
  ##############################################################################################################

  print("writing on movie_genre.csv...")
  
  with open(movieGenreCsv, mode, newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'genre']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    if i == 0:  # Write header only on the first iteration
      writer.writeheader()
    for j in range(0, len(titles)):
      writer.writerow({
        'title': titles[j],
        'genre': genre_list[j]
        })
  ##############################################################################################################
  
  print("writing on movie_crew.csv...")
  
  with open(movieCrewCsv, mode, newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'crew']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if i == 0:  # Write header only on the first iteration
      writer.writeheader()
    for j in range(0, len(titles)):
      writer.writerow({
        'title': titles[j],
        'crew': director_list[j]
        })
    #############################################################################################################
    
  print("writing on movie_cast.csv...")
    
  with open(movieCastCsv, mode, newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'cast']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if i == 0:  # Write header only on the first iteration
      writer.writeheader()
    for j in range(0, len(titles)):
      writer.writerow({
        'title': titles[j],
        'cast': cast_list[j]
        })
print('''
      ##############################\n
      Movie data scraping completed.
      ##############################
      ''')

# 391



