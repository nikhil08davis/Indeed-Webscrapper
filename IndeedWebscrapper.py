import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=data+engineer&l=United+States&fromage={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        Date_posted = item.find('span', class_ = 'date').text.strip()
       # location = item.find('span', class_='location accessible-contrast-color-location').text.strip()

        job = {
            'title'   : title,
            'company' : company,
            'Date_posted' : Date_posted
          #  'location': location
        }
        joblist.append(job)
    return

joblist = []

for i in range (0,30,5):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')









