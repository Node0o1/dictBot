# dictBot
discord bot for resolving acronyms and defining search terms. 
##### *Type: Discord-Bot*

## Whats new
> This bot supports slash commands and now also adopted dictionary.com
> This allows users to search definitions of words within the Discord chat.
>
> **Also creates a log of used commands for analysis purposes. Feel free to remove the write_log function and related calls if desired.**

### Description:
>Search acronym meanings and search definitions of words/terms/etc within discord chat. This application uses www.acronymfinder.com, www.wikipedia.org, and www.dictionary.com respectively.
>
### Notes:
>Quite reliable and decent speed. Uses the python Requests and BeautifulSoup libraries to scrape the relevant data from the site corospnding to the search.
>
>Notice that Discord has a limit of 2000 characters in bot responses. Therefore any output generated that exceeds this limit will be truncated. The URL of the given response will be included with the output for all queries to allow users to easily navigate to and explore responses to the fullest extent if needed.  
>
>This is not meant to be downloaded form git as an application in whole, but rather to make the source code public. However, you are welcome to do so.
>Token not included. To run this bot as your own, you will need to create a Discord bot linked to your account at `https://discord.com/developers/applications` to recieve a valid bot login token. That token will need to be saved inside the `.env` file as `TOKEN=YOUR_TOKEN` which has already been created for you. You just need to edit the file when you recieve a valid token.
>
>*NEVER SHARE YOUR LOGIN TOKENS WITH ANYONE!*
>
>I may start running these bots on a dedicated instance and make them available to invite to your server in the near future. Stay tuned for future implementations.



## **Images:**
- /dictbot-help
<p align="center">
  <img width="608" alt="image" src="https://github.com/user-attachments/assets/f7b608c0-112f-4706-bf62-3fc143c84f35">


</p>

- /acronym-finder
<p align="center">
  <img width="608" alt="image" src="https://github.com/user-attachments/assets/4ef17478-fc0c-4df3-a8df-94ae2bf1d6dd">


</p>

- /wiki
<p align="center">
  <img width="608" alt="image" src="https://github.com/user-attachments/assets/e9da88eb-e5e2-486b-a28b-65627d0a1e88">


</p>

-/dictionary
<p align="center">
  <img width="608" alt="image" src="https://github.com/user-attachments/assets/5ae6996c-f913-47a1-890e-2d6710a10cb4">


</p>


  

