from socket import socket, AF_INET, SOCK_STREAM

# 144.39.198.208

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 3010))
    while True:
        text = input("Gimme some text: ")
        s.send(bytes(text, "UTF-8"))
        data = s.recv(8192)
        fuddified_text = str(data, "UTF-8")
        print(fuddified_text)


