import requests
from bs4 import BeautifulSoup
import csv
import re

# datas
base_url = "https://digimoviez.com/"
csv_addr="" 


res = requests.get(base_url)
soup = BeautifulSoup(res.text)

# holder movie cards list
holders = soup.find_all('div', class_='item_def_loop')

# holder of title of movie
title_holders = [div.find('div', class_='title_h') for div in holders]

pattern = re.compile(r'دانلود فیلم\s(.+)')
titles_years1 = [pattern.search(holder.text).group(1) for holder in title_holders]

pattern = re.compile(r'(.+)\s(\d{4})')
titles_years = [pattern.search(title_year) for title_year in titles_years1]

titles=[match.group(1) for match in titles_years]
years=[match.group(2) for match in titles_years]
#######################################################

country_list = [div.select(
  "div.meta_loop > div.meta_item > ul > li:nth-of-type(6) > span.res_item"
  ) for div in holders]
countries = [country[0].text for country in country_list]
#######################################################

description_list = [div.select("div.plot_text")[0].text for div in holders]
#######################################################

rating_list = [div.select("strong")[0].text for div in holders]
#######################################################

minutes_list = [div.select(
  "div.meta_loop > div.meta_item > ul > li:nth-of-type(2) > span.res_item"
  )[0].text for div in holders]
minutes_list = [minutes.split(" ")[0] for minutes in minutes_list]
#######################################################

genre_list = [div.select(
  "div.meta_loop > div.meta_item > ul > li:nth-of-type(3) > span.res_item"
  )[0].text for div in holders]
#######################################################

director_list = [div.select(
  "div.meta_loop > div.meta_item > ul > li:nth-of-type(4) > span.res_item"
  )[0].text for div in holders]
#######################################################

cast_list = [div.select(
  "div.meta_loop > div.meta_item > ul > li:nth-of-type(5) > span.res_item"
  )[0].text for div in holders]
#######################################################

poster_list = [div.select("img")[0].get("src") for div in holders]
#######################################################

for div in poster_list:
    print(div, "\n")













# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# complete the expectations and write in a csv file

# for i in range(1, 862):
#   movie_url = base_url + f'page/{i}/'
#   res = requests.get(movie_url)
#   soup = BeautifulSoup(res.text)
#   divs = soup.find_all('div', class_='plot_text') #
  
  # complete the expectations and write in a csv file