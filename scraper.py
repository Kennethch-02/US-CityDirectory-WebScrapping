import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.citydirectory.us/'

def get_links_from_home():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    li_elements = soup.select('#noside > div:nth-child(6) > div > ul > li')
    return ['https://www.citydirectory.us' + li.a['href'] for li in li_elements]

def get_city_links(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    city_li_elements = soup.select('#content > div:nth-child(2) > ul > li > h2 > a')
    return ['https://www.citydirectory.us' +city['href'] for city in city_li_elements]

def extract_city_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('#cityhall').text.strip() 
    table_rows = soup.select('#div_cityhall > table > tr')
    data = {}
    for row in table_rows:
        th = row.find('th')
        td = row.find('td')
        key = th.get_text(strip=True)
        value = td.get_text(strip=True) if not td.find('a') else td.find('a').get_text(strip=True)
        
        data[key] = value
    return {title: data}
