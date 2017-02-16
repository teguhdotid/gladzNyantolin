#!/usr/bin/python
#Author Teguh Sasongko ( ./Mr.GLADz404 )
#60% lihat dari tool KATOOLIN
#Thanks To tool KATOOLIN

import os
import sys, traceback

def main():
	try:
		print ('''\033[1;91m          _           _       ______                              _ _       
         | |         | |     |  ___ \                   _        | (_)      
     ____| | ____  _ | |_____| |   | |_   _  ____ ____ | |_  ___ | |_ ____  
    / _  | |/ _  |/ || (___  | |   | | | | |/ _  |  _ \|  _)/ _ \| | |  _ \ \033[1;m 
   \033[1;39m( ( | | ( ( | ( (_| |/ __/| |   | | |_| ( ( | | | | | |_| |_| | | | | | |
    \_|| |_|\_||_|\____(_____|_|   |_|\__  |\_||_|_| |_|\___\___/|_|_|_| |_|
   (_____|                           (____/   ( Tool Installer Indonesia )\033[1;m
                                               
\033[1;36m	     Author	       \033[1;m: \033[1;39mTeguh Sasongko ( ./Mr.GLADz404 )\033[1;m
\033[1;36m	     Release        \033[1;m   : \033[1;39m15/02/2017 \033[1;m
\033[1;36m	     Codename       \033[1;m   : \033[1;39mgladzNyantolin\033[1;m
\033[1;36m	     Follow me on fb \033[1;m  : \033[1;39mwww.fb.com/gladz404.id\033[1;m
\033[1;36m	     My Blog	     \033[1;m  : \033[1;39mwww.teguhsasongko.tk	  \033[1;m
\033[1;36m	     Greetz	       \033[1;m: \033[1;39mAllah S.W.T , IndoXploit & All My Friends \033[1;m ''')
		def inicio1():
			while True:
				print ('''		
  ___| _) |       |                     |_)      _) |_) |    
\___ \  | |  _` | |  /  _` | __ \    _` | | __ \  | | | __ \ 
      | | | (   |   <  (   | |   |  (   | | |   | | | | | | |
_____/ _|_|\__,_|_|\_\\__,_|_|  _| \__,_|_| .__/ _|_|_|_| |_|
                                           _|                        
1) Lihat Kategori
2) Bantuan
			''')
				maklo0 = raw_input("\033[1;32m Pilih Angka > \033[1;m")	

				def inicio():

					while maklo0 == "1":

						print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
 ,-.                      ,  ,     .                    
(   `                     | /      |                   o
 `-.  ,-. ;-.-. . . ,-:   |<   ,-: |-  ,-. ,-: ,-. ;-. .
.   ) |-' | | | | | | |   | \  | | |   |-' | | | | |   |
 `-'  `-' ' ' ' `-` `-`   '  ` `-` `-' `-' `-| `-' '   '
                                           `-'          
\033[1;m \033[1;33m__________________________________________________\033[1;m

1) Install Tool Buatan dari Indonesia
2) Password Attacks
3) Vulnerability Analysis
4) Wireless Attacks
5) Information Gathering
6) Reverse Engineering

99) Kembali
			 ''')
						maklo1 = raw_input("\033[1;32m Pilih Nomor > \033[1;m")
						if maklo1 == "99":
							inicio1()
						elif maklo1 == "88":
							inicio1()
						else:
							print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")
						
						while maklo1 == "1":
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
,---.         .   ,-.          .             ,       .                      
  |           |   |  )         |             |       |                 o    
  |   ,-. ,-. |   |-<  . . ,-: |-  ,-: ;-.   | ;-. ,-| ,-. ;-. ,-. ,-. . ,-:
  |   | | | | |   |  ) | | | | |   | | | |   | | | | | | | | | |-' `-. | | |
  '   `-' `-' '   `-'  `-` `-` `-' `-` ' '   ' ' ' `-' `-' ' ' `-' `-' ' `-`\033[1;m
  ___________________________________________________________________________
 \033[1;37m=[ - Tool Buatan dari Indonesia - ]\033[1;m

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
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m

;-.                              .    ,.  .   .           ,      
|  )                             |   /  \ |   |           |      
|-'  ,-: ,-. ,-. , , , ,-. ;-. ,-|   |--| |-  |-  ,-: ,-. | , ,-.
|    | | `-. `-. |/|/  | | |   | |   |  | |   |   | | |   |<  `-.
'    `-` `-' `-' ' '   `-' '   `-'   '  ' `-' `-' `-` `-' ' ` `-' \033[1;m
___________________________________________________________________                                                                 
\033[1;37m=[ - Password Attacks - ]\033[1;m

1) WP Bruteforce
2) findmyhash
3) hash-identifier
4) wordlists

0) Install Semua

99) Kembali
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
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
.   ,     .                 .     .   .          ,.          .              
|  /      |                 |   o | o |         /  \         |         o    
| /   . . | ;-. ,-. ;-. ,-: |-. . | . |-  . .   |--| ;-. ,-: | . . ,-. . ,-.
|/    | | | | | |-' |   | | | | | | | |   | |   |  | | | | | | | | `-. | `-.
'     `-` ' ' ' `-' '   `-` `-' ' ' ' `-' `-|   '  ' ' ' `-` ' `-| `-' ' `-'
                                          `-'                  `-'          \033[1;m
________________________________________________________________________________
\033[1;37m=[ - Vulnerability Analysis - ]\033[1;m

1) BBQSQL
2) jSQL
3) Nmap
4) openvas-administrator
5) openvas-cli
6) openvas-manager
7) openvas-scanner
8) Oscanner

0) Install Semua


99) Kembali
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
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
,   .           .                ,.  .   .           ,      
| . | o         |               /  \ |   |           |      
| ) ) . ;-. ,-. | ,-. ,-. ,-.   |--| |-  |-  ,-: ,-. | , ,-.
|/|/  | |   |-' | |-' `-. `-.   |  | |   |   | | |   |<  `-.
' '   ' '   `-' ' `-' `-' `-'   '  ' `-' `-' `-` `-' ' ` `-' \033[1;m
______________________________________________________________
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

						while maklo1 == "5" :
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
,                           .                ,-.     .   .                    
|      ,-                   |   o           /        |   |           o        
| ;-.  |  ,-. ;-. ;-.-. ,-: |-  . ,-. ;-.   | -. ,-: |-  |-. ,-. ;-. . ;-. ,-:
| | |  |- | | |   | | | | | |   | | | | |   \  | | | |   | | |-' |   | | | | |
' ' '  |  `-' '   ' ' ' `-` `-' ' `-' ' '    `-' `-` `-' ' ' `-' '   ' ' ' `-|
      -'                                                                   `-' \033[1;m
________________________________________________________________________________
\033[1;37m=[ - Information Gathering - ]\033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					
29) goofile

0) Install Semua


99) Kembali
				''')
							print ("\033[1;32m Masukan angka yang akan diinstal .\n\033[1;m")
							maklo2 = raw_input("\033[1;32m Pilih Angka > \033[1;m")					
							if maklo2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif maklo2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif maklo2 == "3":
								cmd = os.system("apt-get install amap")
							elif maklo2 == "4":
								cmd = os.system("apt-get install automater")
							elif maklo2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif maklo2 == "6":
								cmd = os.system("apt-get install braa")
							elif maklo2 == "7":
								cmd = os.system("apt-get install casefile")
							elif maklo2 == "8":
								cmd = os.system("apt-get install cdpsnarf")
							elif maklo2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif maklo2 == "10":
								cmd = os.system("apt-get install cookie-cadger")
							elif maklo2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif maklo2 == "12":
								cmd = os.system("apt-get install dmitry")
							elif maklo2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif maklo2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif maklo2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif maklo2 == "16":
								cmd = os.system("apt-get install dnsrecon")
							elif maklo2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif maklo2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif maklo2 == "19":
								cmd = os.system("apt-get install dotdotpwn")
							elif maklo2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif maklo2 == "21":
								cmd = os.system("apt-get install enumiax")
							elif maklo2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif maklo2 == "23":
								cmd = os.system("apt-get install fierce")
							elif maklo2 == "24":
								cmd = os.system("apt-get install firewalk")
							elif maklo2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif maklo2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif maklo2 == "27":
								cmd = os.system("apt-get install ghost-phisher")
							elif maklo2 == "28":
								cmd = os.system("apt-get install golismero")
							elif maklo2 == "29":
								cmd = os.system("apt-get install goofile")
							elif maklo2 == "30":
								cmd = os.system("apt-get install lbd")
							elif maklo2 == "31":
								cmd = os.system("apt-get install maltego-teeth")
							elif maklo2 == "32":
								cmd = os.system("apt-get install masscan")
							elif maklo2 == "33":
								cmd = os.system("apt-get install metagoofil")
							elif maklo2 == "34":
								cmd = os.system("apt-get install miranda")
							elif maklo2 == "35":
								cmd = os.system("apt-get install nmap")
							elif maklo2 == "36":
								cmd = os.system("apt-get install hping3")
							elif maklo2 == "37":
								cmd = os.system("apt-get install p0f")
							elif maklo2 == "38":
								cmd = os.system("apt-get install parsero")
							elif maklo2 == "39":
								cmd = os.system("apt-get install recon-ng")
							elif maklo2 == "40":
								cmd = os.system("apt-get install set")
							elif maklo2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif maklo2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif maklo2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif maklo2 == "44":
								cmd = os.system("apt-get install sslsplit")
							elif maklo2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif maklo2 == "46":
								cmd = os.system("apt-get install sslyze")
							elif maklo2 == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif maklo2 == "48":
								cmd = os.system("apt-get install theharvester")
							elif maklo2 == "49":
								cmd = os.system("apt-get install tlssled")
							elif maklo2 == "50":
								cmd = os.system("apt-get install twofi")
							elif maklo2 == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif maklo2 == "52":
								cmd = os.system("apt-get install wireshark")
							elif maklo2 == "53":
								cmd = os.system("apt-get install wol-e")
							elif maklo2 == "54":
								cmd = os.system("apt-get install xplico")
							elif maklo2 == "55":
								cmd = os.system("apt-get install ismtp")
							elif maklo2 == "56":
								cmd = os.system("apt-get install intrace")
							elif maklo2 == "99":
								inicio()
							elif maklo2 == "88":
								inicio1()
							else:
								print ("\033[1;31m Maaf, Perintah anda salah !!!\033[1;m")

						while maklo1 == "6" :
							print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \033[1;39m
,-.                            ,--.                                    
|  )                           |            o                 o        
|-<  ,-. . , ,-. ;-. ,-. ,-.   |-   ;-. ,-: . ;-. ,-. ,-. ;-. . ;-. ,-:
|  \ |-' |/  |-' |   `-. |-'   |    | | | | | | | |-' |-' |   | | | | |
'  ' `-' '   `-' '   `-' `-'   `--' ' ' `-| ' ' ' `-' `-' '   ' ' ' `-|
                                        `-'                         `-'	\033[1;m
_________________________________________________________________________                                       							
\033[1;37m=[ - Reverse Engineering - ]\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install Semua


99) Kembali
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

					if maklo0 == "2":
						print ('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 
   NOTE  : Masukan angka sesuai dengan angka yang kamu mau install tools nya
	   simple kan ?
	   Ingat!!! angkanya saja, tidak usah pakai ' ) ' (tutup kurung)

Chat Saya di : n00b.zuhaha404(at)gmail.com or
		https://fb.com/gladz404.id
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
