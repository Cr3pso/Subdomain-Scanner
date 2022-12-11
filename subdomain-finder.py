import requests
from os import path
import argparse
import sys
from colorama import Fore
import threading
import signal
import time

print("\n")
print(Fore.GREEN + "  /$$$$$$            /$$             /$$                                   /$$          ")
print(" /$$__  $$          | $$            | $$                                  |__/          ")
print("| $$  \__/ /$$   /$$| $$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$ /$$$$$$$ ")
print("|  $$$$$$ | $$  | $$| $$__  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$| $$__  $$")
print(" \____  $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$  \ $$")
print(" /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$| $$  | $$")
print("|  $$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$  | $$")
print(" \______/  \______/ |_______/  \_______/ \______/ |__/ |__/ |__/ \_______/|__/|__/  |__/")
print("       /$$$$$$                                                             ")
print("      /$$__  $$                                                            ")
print("     | $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ ")
print("     |  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$")
print("      \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/")
print("      /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      ")
print("     |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$      ")
print("      \______/  \_______/ \_______/|__/  |__/|__/  |__/ \_______/|__/ ")
print(Fore.MAGENTA + "                                                                       #By Cr3pso")

print(Fore.BLUE)
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",help = "[-t/--target] To indicate victim's domain")
parser.add_argument("-w","--wordlist",help = "[-w/--wordlist] To indicate the subdomain's wordlist")
parser.add_argument('-http','--http', action = "store_true", help = "[-http/--http] For only sending HTTP requests (Default http & https)")
parser.add_argument('-https','--https', action = "store_true", help = "[-https/--https] For only sending HTTPS requests (Default http & https)")
parser = parser.parse_args()


def def_handler(sig, frame):
    print(Fore.YELLOW + "\n\n[!] Going to Sleep...\n")
    time.sleep(1)
    sys.exit()

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def main():
    if parser.target and parser.wordlist:
        if path.exists(parser.wordlist):
            if parser.http:
                http()

            elif parser.https:
                https()

            else:
                threading.Thread(target=http, args=()).start()
                threading.Thread(target=https, args=()).start()

        else:
            print(Fore.RED + "[-] Can't find the dictionary "+parser.wordlist)

    else:
        print(Fore.RED + "[-] Please, make use of the correct parameters (-h/--help)")
        sys.exit()

def http():
    wordlist = open(parser.wordlist,"r")
    words = wordlist.read().split("\n")
    for subdominio in words:
                    url = "http://"+subdominio+"."+parser.target
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print(Fore.CYAN + "[+] Founded subdomain: " + url)

def https():
    wordlist = open(parser.wordlist,"r")
    words = wordlist.read().split("\n")
    for subdominio in words:
                    url = "https://"+subdominio+"."+parser.target
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print(Fore.LIGHTYELLOW_EX + "[+] Founded Subdomain: " + url)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n[!] Going to Sleep...")
        time.sleep(1)
        sys.exit()
