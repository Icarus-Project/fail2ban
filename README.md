# fail2ban
Fail2ban Python
Script principale: fail2ban_sasl.py
Librerie personalizzate:
  - ip_reputation.py
  - obtain_ip.py



#database_msql = MySQLdb.connect(host="127.0.0.1",user="admin",passwd="password",db="fail2ban")
Lo scritp è pensato per aggiornare un MySql che in questo caso è in locale sulla LAMP
E' necessario inserire il puntamento al posto del localhost ("127.0.0.1")
