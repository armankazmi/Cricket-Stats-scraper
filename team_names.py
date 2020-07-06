#Python script to extract the all the names of the Teams available for data.
#author : Arman Kazmi

#Importing libraries

import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup

#url of espncrickinfo stats
url = "https://stats.espncricinfo.com/ci/engine/records/index.html"
r = requests.get(url) 
soup = BeautifulSoup(r.content,  features="lxml" )

#Extracting the names
table = soup.find('div',attrs={'id':'recteam'})
teams = table.findAll('li')
team_aval = {}
country_link = {}
for i in range(0,len(teams)):
    c = teams[i].find('a')
    link = c['href']
    link = "https://stats.espncricinfo.com/"+str(link)
    team_aval[i] = teams[i].text.strip()
    country_link[teams[i].text.strip()] = link

