# Mossy's Discord Bot

A simple, easy to understand discord bot written in python. Will be updated whenever I add new features.

## Current Commands

/rand optional[name, pfp] optional[name, pfp] ...  
	picks a random member of the server and displays infomation about them  
/echo [message]  
	repeats [message]  
/dm [username#tag] [message]  
	dm's a user [message]  
	- need to add @ functionality  
/reddit [subreddit] optional[imagenum]  
	gets the hottest [imagenum] images from r/[subbreddit] and sends them  

## prerequisites

must run on linux to use /reddit  
dotenv  
	pip install dotenv  
discord.py  
	pip install discord.py  
a discord account  
a discord bot setup https://discord.com/developers/applications  

## installation

create a .env file in the bot's directory with the following text  

```# .env
DISCORD_TOKEN=DiscordBotToken
DISCORD_GUILD=NameOfDiscordServer
```
