import datetime
import multiprocessing as mp
import socket as s
from multiprocessing.dummy import Pool as ThreadPool

import requests


class Awalan:
	def __init__(self, ip):
		self.ip = ip
		
	def Catat(self, data):
		with open ("hasil.txt",'a') as dataku:
			dataku.write(f"{data}\n")
			
                         
	def Scanner(self, data):
		url = f"https://{data}.{self.ip}"
		try:
			requests.get(url)
			now = datetime.datetime.now()
			jam = now.strftime(f"%H:%M:%S")
			self.Catat(url)
			print(f"\033[92m [#] aktif : [{jam}] {url}")
		except requests.ConnectionError:
			print(f"\033[91m [#] tidak aktif : {url}")
			pass
			
def Utama(data, domain):
	sin = Awalan(domain)
	sin.Scanner(data)
	
if __name__ == "__main__":
	print('''
 _______   _______   _______     
/______/\ /______/\ /______/\ 
\__::::\/ \__::::\/ \__::::\/  

   █████╗ ██████╗ ██╗   ██╗
  ██╔══██╗██╔══██╗██║   ██║
  ███████║██████╔╝██║   ██║
  ██╔══██║██╔══██╗╚██╗ ██╔╝
  ██║  ██║██║  ██║ ╚████╔╝ 
  ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝                       
 _______   _______   _______  
/______/\ /______/\ /______/\ 
\__::::\/ \__::::\/ \__::::\/                                  
	''')

	global domain	
	domain = input("Masukkan Domain: ")
	print(f'IP Address dari {domain} adalah \033[93m {s.gethostbyname(domain)}')
	

	core = mp.cpu_count()
	core = int(input(f"\nMasukkan Jumlah CPU (Max {core} CPU) : "))
	print(f'IP Address dari {domain} adalah \033[93m {s.gethostbyname(domain)}')
	
	print(''' \033[94m
	+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 	|S|E|D|A|N|G| |S|C|A|N| |D|O|M|A|I|N| |T|U|N|G|G|U| |B|E|B|E|B|R|A|P|A| |S|A|A|T|!|!|
 	+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
		''')

	with open('subdomain.md','r') as dataku:
		data = dataku.read().splitlines()
	temp = []

	for i in data:
		temp.append(domain)
	p = mp.Pool(int(core))
	pool = ThreadPool(int(core))
	pool.starmap(Utama, zip(data, temp)) 
	pool.close() 
	pool.join()  
