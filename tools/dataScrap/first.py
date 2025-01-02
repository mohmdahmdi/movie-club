import requests
from bs4 import BeautifulSoup
import csv
import re

moviesCsv = "E:/codes/projects/movie-club/tools/csv/movies.csv"
movieCastCsv= "E:/codes/projects/movie-club/tools/csv/movie_cast.csv"
movieCrewCsv= "E:/codes/projects/movie-club/tools/csv/movie_crew.csv"
movieGenreCsv= "E:/codes/projects/movie-club/tools/csv/movie_genre.csv"
notFetched = []

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
    notFetched.append(i)
    continue
  
  print("working on data...")
  # holder movie cards list
  holders = soup.find_all('div', class_='item_def_loop')
  titles_years = []
  titles= []
  years = []
  countries = []
  description_list = []
  rating_list = []
  minutes_list = []
  genre_list = []
  director_list = []
  cast_list = []
  poster_list = []
  
  for index, holder in enumerate(holders) :
    li_order = ['sth', 'minute', 'genre', 'director', 'cast', 'country']
    # title, year
    titles_years.append(holder.find('div', class_='title_h').select("h2 > a")[0].text)
    pattern = re.compile(r'^\S+\s+\S+\s+(.+?)\s+(\d{4})')
    match = pattern.search(titles_years[index])
    if match :
      titles.append(match.group(1))
      years.append(match.group(2))
    else :
      titles.append("unknown")
      years.append("unknown")
    
    # minutes
    minute = holder.select(
      "div.meta_loop > div.meta_item > ul > li:nth-of-type(2) > span.res_item"
      )[0].text.split(' ')[0]
    pattern = re.compile(r'\d{2,4}')
    
    if pattern.search(minute) != None:
      minutes_list.append(minute)
    else :
      minutes_list.append('unknown')
      li_order.remove('minute')
      
    # genre
    genre = holder.select(
      f'div.meta_loop > div.meta_item > ul > li:nth-of-type({li_order.index('genre') + 1}) > span.res_item'
      )[0].text
    if genre:
      genre_list.append(genre)
    else : 
      genre_list.append('unkonwn')
      li_order.remove('genre')
    
    # director
    director =holder.select(
      f'div.meta_loop > div.meta_item > ul > li:nth-of-type({li_order.index('director') + 1}) > span.res_item'
      )[0].text
    
    if director : 
      director_list.append(director)
    else :
      director_list.append('unknown')
      li_order.remove('director')
    
    # cast
    cast = holder.select(
      f'div.meta_loop > div.meta_item > ul > li:nth-of-type({li_order.index("cast") + 1}) > span.res_item'
    )
    cast_list.append(cast[0].text if cast else "unknown")
    
    # country
    country = holder.select(
      f'div.meta_loop > div.meta_item > ul > li:nth-of-type({li_order.index('country') + 1}) > span.res_item'
      )
    countries.append(country[0].text if country else "unknown")
    
    # poster
    poster_list.append(holder.select("img")[0].get("src") if holder.select("img") else "unknown")

    # description
    description_list.append(holder.select("div.plot_text")[0].text if holder.select("div.plot_text") else "unknown")
    # rating
    rating_list.append(holder.select("strong")[0].text if holder.select("strong") else "unknown")

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
print(notFetched)




