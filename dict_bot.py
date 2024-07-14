import urllib.parse
import discord
from discord.ext import commands
import urllib
import requests
from bs4 import BeautifulSoup as sp
from globals import HEADER, TIMEOUT, MAX_RETURN_VALUE_LENGTH, TOKEN
import re


intents=discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='/', intents=intents)

def write_log(message, url, param) -> None:
    with open('./dictbot-log.bin', mode='ab+') as fhandle:
        fhandle.write(f'{message.author} : {url} -- {param}{chr(0x0a)}'.encode('utf-8'))


@bot.event
async def on_ready() -> None:
    await bot.tree.sync()
    print(f'{bot.user.name} active...{chr(0x0a)}')


@bot.hybrid_command(name='dictbot-help', description="displays help message")
async def bot_help(message) -> None:
    write_log(message, 'dictionary.com', 'dictbot-help command')
    help_msg = f'Type `/acronym` to resolve what an acronym may stand for.{chr(0x0a)}EXAMPLE: `/acronym xss`{chr(0x0a)*2}Type `/define` to get the definition of any search using wikipedia{chr(0x0a)}EXAMPLE: `/define cross site scripting`{chr(0x0a)*2}Response data is a product of www.acronymfinder.com and/or www.wikipedia.org respectively.'
    await message.reply(help_msg)
    


@bot.hybrid_command(name="acronym-finder", description="Explore resolutions for acronym meanings from acronymfinder.com")
async def get_acronym(message, *, acronym) -> None:
    write_log(message, 'acronymfinder.com', acronym.upper())
    url_param = urllib.parse.quote(acronym.upper())
    url = f'https://www.acronymfinder.com/{url_param}.html'    
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    try:
        table = soup.find('tbody')
        rows = table.find_all('td', {"class":"result-list__body__meaning"})
        acro_list = ''.join([row.text+'\n' for row in rows])
    except: acro_list = f'Unable to find acronym definitions for {acronym.upper()}'
    finally: await message.reply( f'{acronym.upper()}{chr(0x0a)}URL: {url}{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{acro_list[:(MAX_RETURN_VALUE_LENGTH - (29 + len(acronym) + len(url)))]+'...' if (len(acro_list) + len(acronym) + len(url) + 26) > MAX_RETURN_VALUE_LENGTH else acro_list}```')
    

@bot.hybrid_command(name="wiki", description="Search terms/definitions from wikipedia")
async def get_wiki(message, *, search_term) -> None:
    write_log(message, 'wikipedia.org', search_term)
    url_param = urllib.parse.quote(search_term)
    url = f'https://en.wikipedia.org/wiki/Special:Search?go=Go&search={url_param}&ns0=1'
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    full_wiki = soup.find('div', {'class':'mw-content-ltr mw-parser-output'})
    try: 
        short_wiki_list = full_wiki.find_all('p')
        short_wiki = ''.join([wiki.text for wiki in short_wiki_list]) 
    except: 
        try: short_wiki = soup.find('p', {'class':'mw-search-nonefound'}).text
        except: short_wiki = soup.find('p',{"class":"mw-search-createlink"}).text
    finally: await message.reply(f'{search_term.upper()}{chr(0x0a)}URL: {url}{chr(0x0a)*2}RESPONSE:{chr(0x0a)}```{short_wiki[:(MAX_RETURN_VALUE_LENGTH - (29 + len(search_term) + len(url)))]+'...' if (len(short_wiki) + 26 + len(search_term) + len(url)) > MAX_RETURN_VALUE_LENGTH else short_wiki}```')
    

@bot.hybrid_command(name='dictionary', description='Search definitions from dictionary.com')
async def get_dictionary(message, *, search_term) -> None:
    write_log(message, 'dictionary.com', search_term)
    url_param = urllib.parse.quote(search_term)
    url = f'https://www.dictionary.com/browse/{url_param}'
    data = requests.get(url, headers= HEADER, timeout= TIMEOUT)
    soup = sp(data.text, "html.parser")
    try:
        definition_scrape = soup.find('section', {'data-type':'american-dictionary-entries-module'})
        definition = ''.join([element.text+'\n\n' for element in definition_scrape])
    except: definition = f'Definition for {search_term} not found. Please check your spelling and try again.'
    await message.reply(f'{search_term.upper()}{chr(0x0a)}URL: {url}{chr(0x0a)*2}RESPONSE: ```{definition}```')
    

def main() -> None:
    bot.run(TOKEN)

