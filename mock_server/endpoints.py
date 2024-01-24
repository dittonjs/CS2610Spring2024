from response import Response
import datetime
from middleware import require_login, logging_middleware
# user should be logged in

@logging_middleware
@require_login
def hello_world(req):
    return Response(
        version="HTTP/1.1",
        code=200,
        reason="Ok",
        headers={
            "X-CustomHeader": "my headers"
        },
        text="<h1>Hello, world!</h1>"
    )



#don't need to be logged in
def goodbye_world(req):
    return Response(
        version="HTTP/1.1",
        code=200,
        reason="Ok",
        headers={
            "X-CustomHeader": "my headers"
        },
        text="<h1>Goodbye, world!</h1>"
    )