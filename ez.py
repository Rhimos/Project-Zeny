import os
from colorama import Fore
import pyautogui
from dhooks import Webhook
import time
from datetime import date
dl = date.today()

print('''
Made By Fano#0001 ''')
time.sleep(2)
print('''
Sending Packets
''')

print(dl.month,-dl.day,-dl.year)
print(''' Hosting...  ''')
time.sleep(2)
os.system("cls && title Administator:            ∘        Zeny Multitool        ∘   Made By Fano#0001")
print('''
Multitool Project Zayn
 ''')
time.sleep(2)
print('''

''')







def Design():
    print(f'''
 
{Fore.LIGHTGREEN_EX}                ██▓███   ██▀███  ▄▄▄██▀▀▀▄████▄  ▄▄▄█████▓      ▒███████▒ ▄▄▄     ▓██   ██▓ ███▄    █ 
{Fore.LIGHTGREEN_EX}               ▓██░  ██▒▓██ ▒ ██▒  ▒██  ▒██▀ ▀█  ▓  ██▒ ▓▒      ▒ ▒ ▒ ▄▀░▒████▄    ▒██  ██▒ ██ ▀█   █ 
{Fore.LIGHTGREEN_EX}               ▓██░ ██▓▒▓██ ░▄█ ▒  ░██  ▒▓█    ▄ ▒ ▓██░ ▒░      ░ ▒ ▄▀▒░ ▒██  ▀█▄   ▒██ ██░▓██  ▀█ ██▒
{Fore.LIGHTGREEN_EX}               ▒██▄█▓▒ ▒▒██▀▀█▄ ▓██▄██▓ ▒▓▓▄ ▄██▒░ ▓██▓ ░         ▄▀▒   ░░██▄▄▄▄██  ░ ▐██▓░▓██▒  ▐▌██▒
{Fore.LIGHTGREEN_EX}               ▒██▒ ░  ░░██▓ ▒██▒▓███▒  ▒ ▓███▀ ░  ▒██▒ ░       ▒███████▒ ▓█   ▓██▒ ░ ██▒▓░▒██░   ▓██░
{Fore.LIGHTGREEN_EX}               ▒▓▒░ ░  ░░ ▒▓ ░▒▓░▒▓▒▒░  ░ ░▒ ▒  ░  ▒ ░░         ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░   ▒ ▒ 
{Fore.LIGHTGREEN_EX}               ░▒ ░       ░▒ ░ ▒░▒ ░▒░    ░  ▒       ░          ░░▒ ▒ ░ ▒  ▒   ▒▒ ░▓██ ░▒░ ░ ░░   ░ ▒░
{Fore.LIGHTGREEN_EX}               ░░         ░░   ░ ░ ░ ░  ░          ░            ░ ░ ░ ░ ░  ░   ▒   ▒ ▒ ░░     ░   ░ ░ 
{Fore.LIGHTGREEN_EX}                ░     ░   ░  ░ ░                       ░ ░          ░  ░░ ░              ░ 
{Fore.LIGHTGREEN_EX}> Made By Fano#0001    {Fore.LIGHTGREEN_EX}  ░                       ░                  ░ ░                              
> Discord.gg/aly  
{Fore.LIGHTGREEN_EX} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   
 [1] Webhook Spammer 
 [2] Spammer
 [3] Mass Dm
 [4] Mass Report                                        
   
   
                                        
     
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                    
          ''')
    answer = input(" [>>>] ")

    if answer == "1":
        print(f'''
 Press Ctrl + C To Stop
        ''')
        Webhook1 = pyautogui.prompt(text='Webhook Url:', title='Webhook Spammer By Fano#0001')

        hook = Webhook(Webhook1)

        MessageToSpam = pyautogui.prompt(text='Message to spam (it @ everyone ', title='Webhook Spammer By Fano#0001')
        while True:
            hook.send(f"@everyone {MessageToSpam}")

            





Design()

os.system("pause")