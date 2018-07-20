import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',12345))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
data = client_socket.recv(65535)

first,second,third = data.decode().split('/')
print(data.decode())

nayeoninfo = ['48', '163']
chaeyounginfo = ['46', '159']
junghyuninfo = ['49', '167']
minainfo = ['46','164']
jihyoinfo = ['45','160']
tsuwiinfo = ['51','171']
momoinfo = ['46','162']
dahyuninfo = ['49','158']
sanainfo = ['48','163']

if first == 'twice:':
    if second == 'nayeon' and third == 'weight':
        client_socket.send(nayeoninfo[0].encode())
    elif second == 'nayeon' and third == 'height':
        client_socket.send(nayeoninfo[1].encode())

    if second == 'chaeyoung' and third == 'weight':
        client_socket.send(chaeyounginfo[0].encode())
    elif second == 'chaeyoung' and third == 'height':
        client_socket.send(chaeyounginfo[1].encode())

    if second == 'junghyun' and third == 'weight':
        client_socket.send(junghyuninfo[0].encode())
    elif second == 'junghyun' and third == 'height':
        client_socket.send(junghyuninfo[1].encode())

    if second == 'mina' and third == 'weight':
        client_socket.send(minainfo[0].encode())
    elif second == 'mina' and third == 'height':
        client_socket.send(minainfo[1].encode())

    if second == 'jihyo' and third == 'weight':
        client_socket.send(jihyoinfo[0].encode())
    elif second == 'jihyo' and third == 'height':
        client_socket.send(jihyoinfo[1].encode())

    if second == 'tsuwi' and third == 'weight':
        client_socket.send(tsuwiinfo[0].encode())
    elif second == 'tsuwi' and third == 'height':
        client_socket.send(tsuwiinfo[1].encode())

    if second == 'momo' and third == 'weight':
        client_socket.send(momoinfo[0].encode())
    elif second == 'momo' and third == 'height':
        client_socket.send(momoinfo[1].encode())

    if second == 'dahyun' and third == 'weight':
        client_socket.send(dahyuninfo[0].encode())
    elif second == 'dahyun' and third == 'height':
        client_socket.send(dahyuninfo[1].encode())

    if second == 'sana' and third == 'weight':
        client_socket.send(sanainfo[0].encode())
    elif second == 'sana' and third == 'height':
        client_socket.send(sanainfo[1].encode())
# client_socket.send(data)
