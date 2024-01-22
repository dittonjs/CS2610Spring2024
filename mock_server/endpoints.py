from response import Response
import datetime

def hello_world(req):
    return Response(
        version="HTTP/1.1",
        code=200,
        reason="Ok",
        headers={
            "Connection": "close",
            "Server": "Joseph's Server",
            "Cache-Control": "no-cache",
            "Date": str(datetime.datetime.today()),
            "Content-Type": "text/html",
            "Content-Length": "22"
        },
        text="<h1>Hello, world!</h1>"
    )