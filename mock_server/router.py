from endpoints import hello_world
from response import Response
import datetime

def router(req):
    if req.uri == "/hello_world":
        return hello_world(req)
    else:
        return Response(
        version="HTTP/1.1",
        code=404,
        reason="Not found",
        headers={
            "Connection": "close",
            "Server": "Joseph's Server",
            "Cache-Control": "no-cache",
            "Date": str(datetime.datetime.today()),
            "Content-Type": "text/html",
            "Content-Length": "23"
        },
        text="<h1>Page not found</h1>"
    )