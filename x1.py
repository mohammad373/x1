# x1

import os
import sys
import socket
import time
import webbrowser as wb
from colorama import Fore

def __wb__():
    os.system("clear")
    try:
        time.sleep(1)
        print(Fore.YELLOW + "[*] ~ Hello . Welcome Back ;)")
        time.sleep(1)
        target = input(Fore.GREEN + "\n[!] - Enter your Address Target ==>  ")
        ip = socket.gethostbyname(target)
        if target == "" or None:
            try:
                time.sleep(2)
                print(Fore.RED + "\n[!] ~ Error : Your Target is Not Found ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        time.sleep(0.2)
        print(Fore.BUE + "\n[" + Fore.RED + "+" + Fore.BLUE + "]" + Fore.YELLOW + "~" + Fore.GREEN + "Your Ip Target : " + Fore.YELLOW + "o")
        time.sleep(0.6)
        yes = input(Fore.GREEN + "\n[!] ~ Do You Want To Continue ? (y or n ) ==>  ")
        if yes == "" or None:
            try:
                time.sleep(1)
                print(Fore.RED + "\n[!] - Error : Sory Not Found ;(")
                time.sleep(0.2)
                print(Fore.YELLOW + "Ok Good Bay ;)")
                sys.exit()
            except:
                pass
        if yes.lower() == "n":
            try:
                time.sleep(0.5)
                print(Fore.GREEN + "\n[-] ~ Ok Good Bay ;)")
                time.sleep(0.3)
                sys.exit()
            except:
                pass
        if yes.lower() == "y":
            try:
                time.sleep(0.3)
                print(Fore.GREEN + "\n[+] ~ OK Lets Go ;)")
                time.sleep(0.2)
                y = int(input(Fore.GREEN + "\n[!] - Do You Want the 1 : Site Link Or The 2 : Site Will Open ? ==> "))
                if y == "" or None:
                    try:
                        time.sleep(0.4)
                        print(Fore.RED + "[!] - Error : Not Found ;(")
                        time.sleep(0.3)
                        sys.exit()
                    except:
                        pass
                if y == 1:
                    try:
                        time.sleep(2)
                        print(Fore.YELLOW + "\n[!] ~ Pleass Wait 5 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 4 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 3 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 2 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 1 Sec ...")
                        time.sleep(1)
                        link = "https://who.is/whois-ip/ip-address/" + ip
                        print(Fore.YELLOW + "[+] ~ Your Link Is : " + link)
                        time.sleep(2)
                        print(Fore.green + "\n[*] ~ Good Bay ;)")
                        time.sleep(2)
                    except:
                        pass
                if y == 2:
                    try:
                        time.sleep(2)
                        print(Fore.YELLOW + "\n[!] ~ Pleass Wait 5 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 4 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 3 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 2 Sec ...")
                        time.sleep(1)
                        print(Fore.YELLOW + "[!] ~ Pleass Wait 1 Sec ...")
                        time.sleep(1)
                        wb.open("https://who.is/whois-ip/ip-address/"+ ip)
                        time.sleep(0.5)
                        sys.exit()
                    except:
                        pass
            except:
                pass
    except:
        pass
__wb__()
