import socket
import sys
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ms.bind(("", 5986))
except socket.error:
    print('Bind Failed')
    sys.exit()
    
ms.listen(5)

while True:
    conn, addr = ms.accept()
    print('Got a Request!')
    data = conn.recv(1000)
    print(data)
    if not data:
          break
    conn.sendall(data)
          
conn.close()
ms.close()
    
          