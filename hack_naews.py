from bs4 import BeautifulSoup
import requests
import json


hack_news = []

HEADRS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
URL = ('https://news.ycombinator.com/')
respons = requests.get(url= URL, verify= False, headers= HEADRS)
respons.encoding='utf-8'
soup = BeautifulSoup(respons.text, 'lxml')


for i in soup.find_all('span', {'class': 'titleline'}):
    Title = i.find('a').get_text('href')
    for elem in soup.find_all('span', {'class': 'titleline'}):
        Title_link = elem.find('a').get('href')
        for hour in soup.find_all('span', {'class': 'age'}):
            Time = hour.find('a').get_text('href')
            
            
    
    name_link = {
        'Title' : Title,
        'Title_link' : Title_link,
        'Points': soup.find('span', class_='score').text,
        'Hour': Time,
        'Comments' : str(soup.find('span', class_='subline',).get_text().split()[-2]),
        'Comments link': 'https://news.ycombinator.com/' + soup.find('span', class_='age').find('a').get('href')
    }



    hack_news.append(name_link)
    with open('news.json', 'w', encoding='utf-8') as file:
        json.dump(name_link, file, indent=4, ensure_ascii=False)

print(hack_news)