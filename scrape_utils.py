import urllib.parse
import requests
from bs4 import BeautifulSoup as sp
import urllib
from globals import HEADER, TIMEOUT, MAX_RETURN_VALUE_LENGTH


def get_acronym(acronym) -> str:
    url_param = urllib.parse.quote(acronym.upper())
    url = f'https://www.acronymfinder.com/{url_param}.html'

    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    try:
        table = soup.find('tbody')
        rows = table.find_all('td', {"class":"result-list__body__meaning"})
        acro_list = ''.join([row.text+'\n' for row in rows])
    except: acro_list = f'Unable to find acronym definitions for {acronym.upper()}'
    finally: return f'URL:`{url}`{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{acro_list[:(MAX_RETURN_VALUE_LENGTH - (24 + len(url)))] if (len(acro_list) + len(url) + 24) > MAX_RETURN_VALUE_LENGTH else acro_list}```'


def get_definition(search_term) -> str:
    url_param = urllib.parse.quote(search_term)
    url = f'https://www.wikipedia.org/search-redirect.php?family=Wikipedia&language=en&search={url_param}&language=en&go=Go'
    
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    full_wiki = soup.find('div', {'class':'mw-content-ltr mw-parser-output'})
    try: short_wiki = full_wiki.find('p')
    except: short_wiki = soup.find('p',{"class":"mw-search-createlink"}) #if definition does not exist
    finally: return f'URL:`{url}`{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{short_wiki.text[:(MAX_RETURN_VALUE_LENGTH - (24 + len(url)))] if (len(short_wiki.text) + 24 + len(url)) > MAX_RETURN_VALUE_LENGTH else short_wiki.text}```'
