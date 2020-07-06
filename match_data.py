#Extracting match dataset 
#author : Arman Kazmi

from team_names import *
import pandas as pd

#It extracts all the links for a match type of a country
def years (url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, features='lxml')
    table = soup.find('td') 
    year_link = {}
    for row in table.findAll('ul',attrs={'class':'category-noindent'}):
        for i in row.findAll('a', href=True):
            year_name = i.text
            link = i['href']
            link = "https://stats.espncricinfo.com/"+str(link)
            year_link[year_name] = link
    return year_link

#Extracting the match data 
def match_stat(link):
    data = []
    r = requests.get(link)
    soup = BeautifulSoup(r.content,  features='lxml')
    table = soup.findAll('caption')
    tabs = table[0].findNext('tbody')
    rows = tabs.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols) 
    d1 = pd.DataFrame(data,columns=['Team 1','Team 2 ','Winner','Margins','Ground','Match-date','Scorecard'])
    d1.to_csv("data.csv")
    return d1


#Choice of year for dataset
def year_enter(matches_links):
    year_of_match = input("Enter the year of the match for dataset : ")
    try:
        final_data = match_stat(matches_links[year_of_match])
        print(final_data)
        print("")
    except:
        print("Invalid Year or datset not available ")



#User-Inputs
print(team_aval)
print("Enter the country index for which the dataset is required : ")
country = int(input())
try:
    print("The country chosen is :- "+team_aval[country])
    print("Enter the requried match type dataset by entering from the options below :")
    print("a : Test-Matches")
    print("b : ODI Matches")
    print("c : 20-20 Matches")
    choice = input()



    #extracting the required link of the match held in that particular year
    link_maker = country_link[team_aval[country]]
    pos = link_maker.find('id')
    if choice == 'a':  
        test_match = "https://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=1;"+str(link_maker[pos:])
        matches_year = years(test_match)
        year_enter(matches_year)
    elif choice == 'b':
        odi_match = "https://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=2;"+str(link_maker[pos:])
        matches_year = years(odi_match)
        year_enter(matches_year)
    elif choice == 'c':
        twenty_twenty = "https://stats.espncricinfo.com/ci/engine/records/team/match_results_year.html?class=3;"+str(link_maker[pos:])
        matches_year = years(twenty_twenty)
        year_enter(matches_year)
    else:
        print("Invalid Choice")
except:
    print("Invalid choice")

