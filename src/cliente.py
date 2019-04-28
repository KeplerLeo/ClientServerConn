import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999

s.connect((host, port)) 

addr = socket.gethostbyname(host)

print("\nCliente conectado ao servidor IP %s" % str(addr))

print ('Aguardando resposta do servidor...')
msg = s.recv(1024)                                     
print (msg.decode('ascii'))

msg = 'Sou o cliente'+ "\r\n"
s.send(msg.encode('ascii'))

s.close()