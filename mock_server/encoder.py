from request import Request

def decode_request(http_string):
    return Request(
        method="GET",
        version="HTTP/1.1",
        uri="/hello_world",
        headers={
            # "Session-Token": "asdf;lkajsdf;l.kjhasd"
        },
        text=""
    )

def encode_response(res):
    print(f"Version: {res.version}")
    print(f"Code: {res.code}")
    print(f"Reason: {res.reason}")
    print(f"Headers: {res.headers}")
    print(f"Text: {res.text}")
    return ""
