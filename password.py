import subprocess as sp
import pyfiglet
from colorama import Fore , Style

output = pyfiglet.figlet_format("Password  Stealer")

command1 = "netsh wlan show profile "
print(Fore.BLUE+output+Style.DIM)
print(sp.run(command1, shell=True, stdout=True, text=True).stdout)
#sp.call(["netsh","wlan", "show", "profile"])




print(Fore.RED.join(":***************************************************:")+Style.DIM)
SSID = input("Choose SSID : ")
print(":***************************************************:")

command2 = f'netsh wlan show profile name="{SSID}" key=clear | findstr "Key Content" '



print(sp.run(command2, shell=True, stdout=True, text=True).stdout)
print(":***************************************************:")