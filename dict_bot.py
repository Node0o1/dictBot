import discord
import scrape_utils
from globals import TOKEN


async def respond(message) -> None:
    if(str(message.content).lower().startswith('?acronym')):
        search = message.content.removeprefix('?acronym').strip()
        await message.reply(scrape_utils.get_acronym(search))
    elif(str(message.content).lower().startswith('?define')):
        search = message.content.removeprefix('?define').strip()
        await message.reply(scrape_utils.get_definition(search))    


async def bot_help(message) -> None:
    help_msg = f'Type `?acronym` to resolve what an acronym may stand for.{chr(0x0a)}EXAMPLE: `?acronym xss`{chr(0x0a)*2}Type `?define` to get the definition of any search using wikipedia{chr(0x0a)}EXAMPLE: `?define cross site scripting{chr(0x0a)*2}Response data is a product of www.acronymfinder.com and/or www.wikipedia.org respectively.'
    await message.reply(help_msg)


def listener() -> None:
    intents=discord.Intents.default()
    intents.message_content=True
    client=discord.Client(intents=intents)

    @client.event
    async def on_ready() -> None:
        print(f'{client.user} active...{chr(0x0a)}')

    @client.event
    async def on_message(message) -> None:
        if(message.author == client.user):return
        if(not(message.content.startswith('?acronym') or message.content.startswith('?define') or message.content.startswith('?help'))):return
        print(f'USER:{message.author} COMMAND:{message.content}')
        if(message.content.startswith('?help')): await bot_help(message)
        else: await respond(message)
    
    client.run(TOKEN)
