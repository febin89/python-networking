from socket import *

LOCAL_ADDR = ('127.0.0.1', 8000)
MSG_LEN = 1000

fd = socket(AF_INET, SOCK_DGRAM)
fd.bind(LOCAL_ADDR)


while 1:

	data,addr=fd.recvfrom(MSG_LEN)
	print 'Client:'+data
	i=raw_input('Server:')
	fd.sendto(i,addr)
s.close()
