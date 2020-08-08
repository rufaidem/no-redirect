import time
import os
import concurrent.futures
try:
	import requests
except ImportError:
	os.system("clear")
	os.system("pip install requests")
try:
	from colorama import *
except ImportError:
	os.system("clear")
	os.system("pip install colorama")
import time
os.system("clear")
auth = """  


███████╗██╗███╗   ██╗██████╗       ██╗████████╗
██╔════╝██║████╗  ██║██╔══██╗      ██║╚══██╔══╝
█████╗  ██║██╔██╗ ██║██║  ██║█████╗██║   ██║   
██╔══╝  ██║██║╚██╗██║██║  ██║╚════╝██║   ██║   
██║     ██║██║ ╚████║██████╔╝      ██║   ██║   
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝       ╚═╝   ╚═╝                     
        
code by rufaid 
insta rufaid_popzi
youtube : rufaidtech
github : github.com/rufaid-tech/
------------------------------------------                             """

             
print(Style.BRIGHT)
print(Fore.GREEN+auth)
site = input(Fore.RED+" [+] Admin Panel Link: "+Fore.GREEN)
str = site.split("/")
site = site.replace(str[-1],"")
print()
try:
	opn = open("target.txt","r").readlines()
except:
	print(Fore.RED+"\n [+] Target List Not Found [+]")
	quit()
def scan(x):
	try:
		st = x.strip()
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		r = requests.get(site+st,timeout=10,headers=headers)
		code = int(r.status_code)
		if code < 400:
			print(Fore.GREEN+" Found --> "+site+st)
		else:
			print(Fore.RED+" Not Found -->"+site+st)
	except Exception as e:
		print(Fore.CYAN+" Refused Connection -->"+site)
try:
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(scan,opn)
except:
	print(Fore.RED+" [!] Connection Lost!")
print("\n"+Fore.GREEN+" [+] Scanned Finished [+] ")
print(Fore.RESET)
