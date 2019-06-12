import socket

#实例化一个socket对象
server = socket.socket()

#server端的IP地址
ip_port = ("127.0.0.1",8080)

#server对象绑定IP地址
server.bind(ip_port)

#监听套接字连接
server.listen()

#server.accept创建与服务端之间通信的通道
#conn是客户端和服务端建立好的连接通道,addr:客户端的地址
conn,client_addr = server.accept()
#print(conn)
#print(client_addr)

#接收消息
while True:

    from_client_msg = conn.recv(1024) #一次性接收数据的大小单位是b
    print(from_client_msg)
    msg = input(">>>>").strip()
    if not msg:
        continue
    if msg == "bey":
        break

#发送消息
    conn.send(msg.encode("utf-8"))

#关闭通道
conn.close()

#关闭server对象
server.close()