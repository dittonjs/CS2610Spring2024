import datetime
from response import Response

def logging_middleware(next):
    def middleware(req):
        # do something with the input
        print(f"{req.method} {req.uri}")

        # call next middleware
        res = next(req)
        #do something with the response
        print(f"{res.code} {res.reason}")
        print(res.headers)
        # return the thing the caller
        return res

    return middleware


def required_headers_middleware(next):
    def middleware(req):
        res = next(req)
        headers = {
            "Connection": "close",
            "Server": "Joseph's Server",
            "Cache-Control": "no-cache",
            "Date": str(datetime.datetime.today()),
            "Content-Type": "text/html",
            "Content-Length": len(res.text)
        }
        headers.update(res.headers)
        res.headers = headers
        return res

    return middleware

def require_login(next):
    def middleware(req):
        if "Session-Token" in req.headers and req.headers["Session-Token"] != "":
            return next(req)
        else:
            return Response(
                code=401,
                version="HTTP/1.1",
                reason="Unauthorized",
                headers={},
                text="<h1>You are not authorized!</h1>"
            )

    return middleware