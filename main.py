from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter TV Show name: ').lower() # converting user input to all lowercase
url = url.replace(' ', '-') # if user input has spaces in title then convert all spaces to hyphens
url_general = 'https://thetvdb.com/series/' + url # concatenate user url with standard TVDB URL
url_seasons = 'https://thetvdb.com/series/' + url + '/allseasons/official'

soup_home = BeautifulSoup(urlopen(url_general), 'html.parser')
soup_seasons = BeautifulSoup(urlopen(url_seasons), 'html.parser')

# GRABBING TITLE OF SHOW
table = soup_home.findAll("div", {"class": "col-xs-12 col-sm-8 col-md-8 col-lg-9 col-xl-10"})
for text in table:
  title = text.find('h1').text
  title = title.strip()

# GRABBING DESCRIPTION OF SHOW
table = soup_home.findAll("div", {"data-language": "eng"})
for text in table:
  description = text.find('p').text
  description = description.strip()

# GRABBING NUMBER OF SEASONS
number_of_seasons = soup_seasons.findAll('h3', attrs={'class':'mt-4'})
number_of_seasons = (len(number_of_seasons))

print('\n')
print('Title:', title)
print('\n')
print('Description:', description)
print('\n')
print("No. of Seasons:", number_of_seasons)
