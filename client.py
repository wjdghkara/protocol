import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',12345))
sock.send(str(input('URL : ')).encode())
data = sock.recv(65535)

data = data.decode()

if int(data) > 100:
    if int(data) >= 160:
        print(data,' 키가 큰편입니다.')
    elif int(data) < 160:
        print(data,' 키가 작은편입니다.')
elif int(data) < 100:
    if int(data) < 50:
        print(data, ' 마른편입니다.')
    elif int(data) >= 50:
        print(data, ' 초큼 마른편입니다.')
