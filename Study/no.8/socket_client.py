import socket
client = socket.socket()
server_ip_port = ("127.0.0.1",8080)
client.connect(server_ip_port)
while True:
    msg = input(">>>>:").strip()
    if not msg:
        continue
    if msg == "bey":break

    client.send(msg.encode("utf-8"))
    from_server_msg =client.recv(1024)
    print(from_server_msg)

client.close()