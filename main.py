import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

print(Fore.YELLOW + "Hi")
print(Fore.GREEN + "Python")
print(Back.WHITE + Fore.RED + "Play with me")