import requests
from bs4 import BeautifulSoup
import re

def scrape_squads(url):
    try:
        x=re.match('/',url)
        if x!=None:
            url=url
        else:
            url=url+'/'
        url=url+"squads"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html5lib')
        a=soup.find_all('a',attrs={'class':'black-link d-none d-md-inline-block pl-2'})
        series=soup.find('h5',class_='header-title label')
        squads={}
        for i in a:
            s=i.text
            new_url="https://www.espncricinfo.com"+i['href']
            rr=requests.get(new_url)
            soup=BeautifulSoup(rr.content,'html5lib')
            names=soup.find_all('a',attrs={'class':'h3 benton-bold name black-link d-inline'})
            roles=soup.find_all('div',attrs={'class':'mb-2 mt-1 playing-role benton-normal'})
            age=soup.find_all('div',attrs={'class':'gray-700 benton-normal meta-info'})
            player_names=[]
            player_role=[]
            player_age=[]
            for name in names:
                player_names.append(name.get_text(strip=True))
            for role in roles:
                player_role.append(role.text)
            for ag in age:
                player_age.append(ag.text)    
            squad=[]       
            players=zip(player_names,player_role,player_age)
            for name,role,age in players:
                squad.append((name, role , age))
            squads[s]=squad
        return {
                'status' :"success",
                'series' : series.text,
                'squads' : squads
                }
    except:
        return {
                'status' :"failed",
                'series' : "",
                'squads' : ""
                }


# a = scrape_squads('https://www.espncricinfo.com/series/india-in-south-africa-2021-22-1277060')
# print(a)