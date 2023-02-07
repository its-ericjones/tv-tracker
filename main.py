import requests
from bs4 import BeautifulSoup
import pandas as pd

url = input('Enter TV Show name: ').lower() # converting user input to all lowercase
url = url.replace(' ', '-') # if user input has spaces in title then convert all spaces to hyphens

url_main = 'https://thetvdb.com/series/' + url # concatenate user url with standard TVDB URL
url_main = requests.get(url_main)

url_seasons = 'https://thetvdb.com/series/' + url + '/allseasons/official'
url_seasons = requests.get(url_seasons)

soup_home = BeautifulSoup(url_main.text, 'html.parser')
soup_seasons = BeautifulSoup(url_seasons.text, 'html.parser')

main_block = soup_home.find("div", attrs={"class":"row mt-2"})
episode_block = soup_seasons.find("div", attrs={"class":"col-xs-12 col-sm-12 col-md-8 col-lg-8"})

show_title = []
show_description = []
episode_number = []
episode_title = []
episode_air_date = []
episode_description = []

final_df = pd.DataFrame()

def main_page_scrape():
	for items in main_block.findAll("div", attrs={"class": "col-xs-12 col-sm-8 col-md-8 col-lg-9 col-xl-10"}):
		main_title = items.find("h1", attrs={"class": "translated_title mt-0"}).text
		main_description = items.find("div", attrs={"data-language": "eng"}).text

		show_title.append(main_title)
		show_description.append(main_description)
		
	df_main=pd.DataFrame({
		'Title':show_title,
		'Show Description':show_description
	})
	global final_df 
	final_df = final_df.append(df_main)


def season_page_scrape():
	for items in episode_block.findAll("li", attrs={"class": "list-group-item"}):
		number = items.find("h4", attrs={"class": "list-group-item-heading"}).findChildren()[0].text
		title = items.find("h4", attrs={"class": "list-group-item-heading"}).findChildren()[1].text
		air_date = items.find("ul", attrs={"class": "list-inline text-muted"}).findChildren()[0].text
		description = items.find("div", attrs={"class": "col-xs-9"}).findChildren()[0].text

		episode_number.append(number)
		episode_title.append(title)
		episode_air_date.append(air_date)
		episode_description.append(description)
	
	df_season=pd.DataFrame({
		'Number':episode_number,
		'Title':episode_title,
		'Air Date':episode_air_date,
		'Description':episode_description
	})
	global final_df 
	final_df = final_df.append(df_season)

main_page_scrape()
season_page_scrape()
final_df.to_csv("tvdb.csv")