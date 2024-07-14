import requests
from bs4 import BeautifulSoup as sp
from globals import HEADER, TIMEOUT, MAX_RETURN_VALUE_LENGTH

def acronymfinder(url, acronym) -> str:
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    try:
        table = soup.find('tbody')
        rows = table.find_all('td', {"class":"result-list__body__meaning"})
        acro_list = ''.join([row.text+'\n' for row in rows])
    except: acro_list = f'Unable to find acronym definitions for {acronym.upper()}'
    finally: return ( f'URL: {url}{chr(0x0a)}ACRONYM: {acronym.upper()}{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{acro_list[:(MAX_RETURN_VALUE_LENGTH - (38 + len(acronym) + len(url)))]+'...' if (len(acro_list) + len(acronym) + len(url) + 35) > MAX_RETURN_VALUE_LENGTH else acro_list}```')


def wiki(url, search_term) -> str:
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    full_wiki = soup.find('div', {'class':'mw-content-ltr mw-parser-output'})
    try: 
        short_wiki_list = full_wiki.find_all('p')
        short_wiki = ''.join([wiki.text for wiki in short_wiki_list]) 
    except: 
        try: short_wiki = soup.find('p', {'class':'mw-search-nonefound'}).text
        except: short_wiki = soup.find('p',{"class":"mw-search-createlink"}).text
    finally: return (f'URL: {url}{chr(0x0a)}DEFINE: {search_term}{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{short_wiki[:(MAX_RETURN_VALUE_LENGTH - (38 + len(search_term) + len(url)))]+'...' if (len(short_wiki) + 35 + len(search_term) + len(url)) > MAX_RETURN_VALUE_LENGTH else short_wiki}```')
