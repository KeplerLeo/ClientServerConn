import socket                                         

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()      

port = 9999                                           

serversocket.bind((host, port))                                  
serversocket.listen(5)                                           


clientsocket,addr = serversocket.accept()  

print("\nCliente IP %s" % str(addr) + ' conectado, enviando mensagem de teste')
msg = 'Sou o servidor'+ "\r\n"
clientsocket.send(msg.encode('ascii'))

print ('Mensagem enviada\nAguardando resposta do cliente...')
msg = clientsocket.recv(1024)     
print (msg.decode('ascii'))

clientsocket.close()