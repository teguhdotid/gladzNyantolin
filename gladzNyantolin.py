#!/usr/bin/python
#Author Teguh Sasongko ( ./Mr.GLADz404 )
#WALAUPUN MASIH NYONTEK DARI TOOL KATOOLIN YANG PENTING ADA USAHA
#Thanks To tool KATOOLIN
import os
import sys, traceback

def main():
	try:
		print ('''\033[1;91m	  		  		    
       _           _       ______                              _ _       
      | |         | |     |  ___ \                   _        | (_)      
  ____| | ____  _ | |_____| |   | |_   _  ____ ____ | |_  ___ | |_ ____  
 / _  | |/ _  |/ || (___  | |   | | | | |/ _  |  _ \|  _)/ _ \| | |  _ \ \033[1;m 
\033[1;39m( ( | | ( ( | ( (_| |/ __/| |   | | |_| ( ( | | | | | |_| |_| | | | | | |
 \_|| |_|\_||_|\____(_____|_|   |_|\__  |\_||_|_| |_|\___\___/|_|_|_| |_|
(_____|                           (____/   ( Tool Installer Indonesia )\033[1;m
                                               
	     Author	       : Teguh Sasongko ( ./Mr.GLADz404 )
	     Release           : 15/02/2017 
	     Codename          : gladzNyantolin
	     Follow me on fb   : www.fb.com/gladz404.id
	     My Blog	       : www.teguhsasongko.tk	  
	     Greetz	       : Allah S.W.T , IndoXploit & All My Friends  
''')
		def inicio1():
			while True:
				print ('''
1) Lihat Kategori
2) Bantuan
			''')
				maklo0 = raw_input("\033[1;32m Pilih Angka > \033[1;m")	

				def inicio():

					while maklo0 == "1":
						print ('''
\033[1;33m_____________________Semua Kategori_____________________\033[1;m

1) Tool Asli dari Indonesia
2) Password Attacks
3) Information Gathering
4) Wireless Attacks
5) COMING SOON
6) COMING SOON

99) Kembali
			 ''')
						maklo1 = raw_input("\033[1;32m Pilih Nomor > \033[1;m")
						if maklo1 == "99":
							inicio1()
						elif maklo1 == "88":
							inicio1()	
						while maklo1 == "1":
							print ('''

 1) Dracnmap				
 2) TheFatRat
 3) Brutal
 4) LALIN
 5) gladzBlutz (Making Wordlist)
  

 99) Kembali				
						''')
							print ("\033[1;32m Masukan angka yang akan diinstal .\n\033[1;m")
							maklo2 = raw_input("\033[1;32m Pilih Angka > \033[1;m")
							if maklo2 == "1":
								cmd = os.system("apt-get install git && git clone https://github.com/Screetsec/Dracnmap.git && mv Dracnmap tool/Dracnmap ")
							elif maklo2 == "2":
								cmd = os.system("apt-get install git && git clone https://github.com/Screetsec/TheFatRat.git && mv TheFatRat tool/TheFatRat")
							elif maklo2 == "3":
								cmd = os.system("apt-get install git && git clone https://github.com/Screetsec/Brutal.git && mv Brutal tool/Brutal")
							elif maklo2 == "4":
								cmd = os.system("apt-get install git && git clone https://github.com/Screetsec/LALIN.git && mv LALIN tool/LALIN")
							elif maklo2 == "5":
								cmd = os.system("apt-get install git && git clone https://github.com/teguhdotid/gladzBlutz.git && mv gladzBlutz tool/gladzBlutz")
							elif maklo2 == "99":
								inicio()
							elif maklo2 == "88":
								inicio1()		
							else:
								print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")

						
						while maklo1 == "2" :
							print ('''
\033[1;37m=[ - Password Attacks - ]\033[1;m

1) WP Bruteforce
2) findmyhash
3) hash-identifier
4) wordlists

0) Install Semua
''')
							print ("\033[1;32m Masukan angka yang akan diinstal .\n\033[1;m")
							maklo2 = raw_input("\033[1;32m Pilih Angka > \033[1;m")
							if maklo2 == "1":
								cmd = os.system("git clone https://github.com/atarantini/wpbf.git && cp wpbf/wpbf.py /usr/bin/wpbf && chmod +x /usr/bin/wpbf && wpbf")
							elif maklo2 == "2":
								cmd = os.system("apt-get install findmyhash")
							elif maklo2 == "3":
								cmd = os.system("apt-get install hash-identifier")
							elif maklo2 == "4":
								cmd = os.system("apt-get install wordlists")
							elif maklo2 == "4":
								cmd = os.system("apt-get install -y findmyhash hash-identifier wordlists")	
							elif maklo2 == "99":
								inicio()
							elif maklo2 == "88":
								inicio1()
							else:
								print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")


						while maklo1 == "3" :
							print ('''

\033[1;37m=[ - Information Gathering - ]\033[1;m

1) BBQSQL
2) jSQL
3) Nmap
4) openvas-administrator
5) openvas-cli
6) openvas-manager
7) openvas-scanner
8) Oscanner

0) Install Semua
''')
							print ("\033[1;32m Masukan angka yang akan diinstal .\n\033[1;m")
							maklo2 = raw_input("\033[1;32m Pilih Angka > \033[1;m")					
							if maklo2 == "1":
								cmd = os.system("apt-get install bbqsql")
							elif maklo2 == "2":
								cmd = os.system("apt-get install jSQL")
							elif maklo2 == "3":
								cmd = os.system("apt-get install Nmap")
							elif maklo2 == "4":
								cmd = os.system("apt-get install openvas-administrator")
							elif maklo2 == "5":
								cmd = os.system("apt-get install openvas-cli")
							elif maklo2 == "6":
								cmd = os.system("apt-get install openvas-manager")
							elif maklo2 == "7":
								cmd = os.system("apt-get install openvas-scanner")
							elif maklo2 == "8":
								cmd = os.system("apt-get install Oscanner")
							elif maklo2 == "0":
								cmd = os.system("apt-get install -y bbqsql jSQL Nmap openvas-administrator penvas-cli openvas-manager openvas-scanner")
							elif maklo2 == "99":
								inicio()
							elif maklo2 == "88":
								inicio1()
							else:
								print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")

						while maklo1 == "4" :
							print ('''

\033[1;37m=[ - Wireless Attacks - ]\033[1;m

1) Aircrack-ng
2) eapmd5pass
3) kalibrate-rtl
4) KillerBee
5) redfang
6) Wifite
7) wifitap

0) Install Semua

99) Kembali
				''')
							print ("\033[1;32m Masukan angka yang akan diinstal .\n\033[1;m")
							maklo2 = raw_input("\033[1;32m Pilih Angka > \033[1;m")					
							if maklo2 == "1":
								cmd = os.system("apt-get install eapmd5pass")
							elif maklo2 == "2":
								cmd = os.system("apt-get install kalibrate-rtl")
							elif maklo2 == "3":
								cmd = os.system("apt-get install KillerBee")
							elif maklo2 == "5":
								cmd = os.system("apt-get install redfang")
							elif maklo2 == "6":
								cmd = os.system("apt-get install Wifite")
							elif maklo2 == "7":
								cmd = os.system("apt-get install wifitap")
							elif maklo2 == "0":
								cmd = os.system("apt-get install -y eapmd5pass kalibrate-rtl KillerBee redfang Wifite wifitap")
							elif maklo2 == "99":
								inicio()
							elif maklo2 == "88":
								inicio1()
							else:
								print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")

					if maklo0 == "2":
						print (''' 
   NOTE  : Masukan angka sesuai dengan angka yang kamu mau install tools nya
	   simple kan ?
	   Ingat!!! angkanya saja, tidak usah pakai ' ) ' (tutup kurung)

Chat Saya di : n00b.zuhaha404(at)gmail.com
---------------COMMAND---------------

\033[1;32m99)\033[1;m  \033[1;33mGo back\033[1;m

\033[1;32m88)\033[1;m  \033[1;33mGo to the main menu\033[1;m
_______________________________________________________________________
		''')
				inicio()
		inicio1()
	
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
