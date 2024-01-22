from router import router
from encoder import decode_request, encode_response


if __name__ == "__main__":
    # pretend setup a socket
    data = "..."
    breakpoint
    request = decode_request(data)
    response = router(request)
    response_data = encode_response(response)
    # send that over the network
