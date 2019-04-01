import socket


def is_listed(ip):
	RBL="zen.spamhaus.org"
	REVERSE_IP = ip.split(".")
	REVERSE_IP = REVERSE_IP[::-1]
	REVERSE_IP = '.'.join(REVERSE_IP)
	try:
		c = socket.gethostbyname_ex(REVERSE_IP+"."+RBL)
		severity = len(c[2])	# determina in quante RBL è listato, 1,2 o 3
		return severity
	except socket.gaierror:
		return 0

