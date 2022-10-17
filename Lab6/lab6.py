from mimetypes import init
from colorama import init
from colorama import Fore, Back, Style
#init is required for windows
#leave empty for default, populate to automate style reset
init(autoreset=True)

# Change color of text in terminal

print(Fore.CYAN + 'Cyan text')

# Change background of text in terminal

print(Back.RED + 'Text with a red background')

# Style changes the style of text

print('style commands only work in lnux')

print(Fore.RED + 'To close press enter')
n = input()



