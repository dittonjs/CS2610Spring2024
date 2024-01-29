import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue
            print(str(data, "UTF-8"))
            with open("index.html") as f:

            #TODO: parse the request, send through middleware and encode the response
                res ="HTTP/1.1 200 Ok\nConnection: close\n\n"
                res += f.read()
                connection.send(bytes(res, "UTF-8"))