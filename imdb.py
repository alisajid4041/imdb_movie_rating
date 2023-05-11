import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd

#Access the imdb webpage
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

movies = soup.select('td.titleColumn')
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

list = []
for index in range(0, len(movies)):
    movie = (' '.join((movies[index].get_text()).split()))
    movie_title = movie[len(str(index))+1:-7]
    
    data = {"movie_title":movie_title,
            "rating":ratings[index]
            }
    list.append(data)
    
    
for movie in list:
    print(movie['movie_title'],'-', movie['rating'])
    
df = pd.DataFrame(list)
df.to_csv('imdb.csv', index=False)
             