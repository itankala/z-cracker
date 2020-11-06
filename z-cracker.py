from tqdm import tqdm
import zipfile
from os import system, name
from pyfiglet import figlet_format
from time import sleep

class fcol:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

disclaimer = f"""{fcol.WARNING}{fcol.BOLD}
#===========================================================================#
# [+] Originally Coded By Author: github.com/theindianhackers               #
# [+] Made For Educational Purpose Only Am Not Responsible For Illegal Use  #
# [+] To Run Type Linux: python3 z-cracker.py                               #
# [+] For Any Queries contact us at theindianhackers.help@gmail.com         #
#===========================================================================#
# [+] One Request Please Credit Us If You are                               #
# [+] Modifying this code and distributing it                               #
#===========================================================================#
# [+] We know that this script isn't well optimised                         #
#===========================================================================#
# [+] You Have full rights to modify and distribute the script              #
# [+] But make sure you credit us                                           #
#===========================================================================#
{fcol.ENDC}"""


def scr_clr():
	if name == "posix":
		system("clear")
	else:
		system("cls")

def main(fcol, wordlist, zip_file):
	print(f"{fcol.HEADER}Starting Z-Cracker{fcol.ENDC}\n")
	zip_file = zipfile.ZipFile(zip_file)
	n_words = len(list(open(wordlist, "rb")))
	with open(wordlist, "rb") as wordlist:
		for word in tqdm(wordlist, total=n_words, unit="word"):
			try:
				zip_file.extractall(pwd=word.strip())
			except:
				continue
			else:
				return word.decode().strip()
	print(f"{fcol.FAIL}[!] ERROR: Password not found, try other wordlist.{fcol.ENDC}")
	return False

try:
	print(disclaimer)
	input("Press Enter To Continue ")
	scr_clr()
	print(figlet_format("Z-Cracker"))
	print(f"{fcol.WARNING}{fcol.BOLD}:: Originally Coded By github.com/theindianhacker    v1.0 ::{fcol.ENDC}\n") # Do not remove this line.... it is a request
	print(f"{fcol.WARNING}{fcol.BOLD}:: This script is for Educational Purposes only! ::{fcol.ENDC}\n")

	wordlist = input(str("Wordlist File Name or Path: "))
	zip_file = input(str("Zip File Name or Path: "))

	result = main(fcol, wordlist, zip_file)
	if result != False:
		print(f"{fcol.WARNING}[+] INFO: Continuing In 3 Seconds{fcol.ENDC}")
		sleep(3)
		scr_clr()
		print(figlet_format("Success !!!"))
		print(f"{fcol.OKCYAN}{fcol.BOLD}[+] SUCCESS: Password found: {result}{fcol.ENDC}")
		exit(0)
	else:
		print(f"{fcol.WARNING}[+] INFO: Continuing In 3 Seconds{fcol.ENDC}")
		sleep(3)
		scr_clr()
		print(figlet_format("Fail !!!"))
		print(f"{fcol.OKCYAN}{fcol.BOLD}[!] Fail: Password not found in the wordlist{fcol.ENDC}")
		exit(1)

except KeyboardInterrupt:
	scr_clr()
	print("We are sorry to see you go")
	print(figlet_format(":("))