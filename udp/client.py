from socket import *


TO_ADDR = ('127.0.0.1', 8000)
MSG_LEN=10000
fd = socket(AF_INET, SOCK_DGRAM)


while 1:
	
	i=raw_input('CLient:')
	fd.sendto(i,TO_ADDR)
		
	data,addr=fd.recvfrom(MSG_LEN)

	print 'Server:'+data

