from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 3010))
    s.listen()
    print("Waiting for connection!")
    conn, address = s.accept()
    with conn:
        while True:
            print(f"Connection recieved from {address}")
            data = conn.recv(8192)
            if not data:
                continue
            text = str(data, "UTF-8").replace("r", "w").replace("R", "W")
            print(f"New text is: {text}")
            conn.sendall(bytes(text, "UTF-8"))



