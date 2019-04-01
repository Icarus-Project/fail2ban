#/usr/bin/python3
# coding=utf-8
import os, sys, re
import MySQLdb
from time import strftime, localtime, sleep
import obtain_ip
import ip_reputation
import ip_reputation

#Esempio di log per SASL fallita
pattern = re.compile(r"MAIL-(MT[0-9]+)-P1 .* warning: .*(\[\d+\.\d+\.\d+\.\d+\]).* SASL .* authentication failed: .*")




def get_ip_info(ip):	#SCRIVE IP SU UN FILE CHE PASSA ALLO SCRIPT DI PETER
	info = "country_code" #COME VIENE CHIAMATO NEL JSON
	result_dict = obtain_ip.obtain(ip)
	return result_dict[info]


def populate_db(ip,mta):
	tempo = strftime("%Y-%m-%d_%H:%M", localtime())
	
	#Inserire credenziali DB
	database_msql = MySQLdb.connect(host="127.0.0.1",user="admin",passwd="password",db="fail2ban")
	cursor = database_msql.cursor()
	reputation = ip_reputation.is_listed(ip)	
	#Dobbiamo vedere se l'ip è già presente nel db
	riga = cursor.execute("SELECT * FROM fail2ban WHERE IP like %s;", [ip])
	if int(riga) == 0:	#IP NON PRESENTE NEL DB
		region_code = get_ip_info(ip)
		tentativo = "1"
		cursor.execute("INSERT INTO fail2ban (Reputation, IP, Tentativi, DATA, Region, FE) VALUES (%s, %s,%s,%s,%s,%s);",(reputation,ip,tentativo,tempo,region_code,mta))
		



	else:
		cursor.execute("SELECT * FROM fail2ban WHERE IP like %s;" , [ip])
		query_result = cursor.fetchone()
		tentativi = int(query_result[3])
		cursor.execute("UPDATE fail2ban SET Reputation=%s,Tentativi=%s,DATA=%s,FE=%s WHERE IP=%s;", (reputation,tentativi+1,tempo,mta,ip))


	database_msql.commit()
	cursor.close()
	database_msql.close()







def run_fail2ban():
	#Inserire Log
	log = open("", "r", encoding="utf-8")
	while log.closed == False:
		for line in log :
			if (pattern.search(line)) != None:
				match = pattern.search(line)
				ip = match.group(2)
				mta = match.group(1)
				ip = ip[1:-1]
				populate_db(ip,mta)

	log.close()


if __name__ == "__main__":
	run_fail2ban()
