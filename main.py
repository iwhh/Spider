#!/usr/lib/python3.7
# IRAN CYBER SECURITY GROUP | iran-cyber.net
from re import findall
from time import sleep
from requests import get
from colorama import Fore, Style
import sys
import random
from os import system, name
class Spider(object):
    def __init__(self):
        self.blue = Fore.BLUE
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.white = Fore.WHITE
        self.yellow = Fore.YELLOW
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.res = Style.RESET_ALL

        try:
            self.url = sys.argv[1]
            self.clear()
            self.logo()
            self.make_request(self.url)
        except IndexError:
            self.clear()
            self.logo()
            print(f"{self.cyan}==========================")
            print(f"{self.yellow}[{self.red}~{self.yellow}] {self.green}python {self.magenta}{sys.argv[0]} {self.green}google.com")
            sys.exit(1)



    def logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
             /$$$$$$                      /$$$$$$            /$$       /$$                    
            |_  $$_/                     /$$__  $$          |__/      | $$                    
              | $$    /$$$$$$$  /$$$$$$ | $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
              | $$   /$$_____/ /$$__  $$|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$
              | $$  | $$      | $$  \ $$ \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/
              | $$  | $$      | $$  | $$ /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$      
             /$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$      
            |______/ \_______/ \____  $$ \______/ | $$____/ |__/ \_______/ \_______/|__/      
                               /$$  \ $$          | $$    iran-cyber.net | iraniancoders.ir                                    
                              |  $$$$$$/          | $$                                        
                               \______/           |__/            web spider v1.0                            
                Coded by iwHH 
                github.com/iwhh
            """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            sleep(0.07)
    def clear(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def make_request(self, url):
        print(f"{self.red}Target => {self.blue}{url}\n{self.cyan}===========================")
        if url.startswith("http://"):
            url.replace("http://", "")
        if url.startswith("https://"):
            url.replace("https://", "")
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        self.request = get(f"http://{url}", headers=headers , timeout=5)
        self.request.encoding = "utf-8"
        self.spider(self.request.text)

    def spider(self, target):
        finder = findall(r'"((http|ftp)s?://.*?)"', target)
        for _ in finder:
            print(f"{self.yellow}[{self.red}+{self.yellow}]{self.magenta}{_[0]}")
            sleep(0.08)
if __name__ == "__main__": run = Spider()