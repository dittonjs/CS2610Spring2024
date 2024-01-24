from router import router
from encoder import decode_request, encode_response
from middleware import logging_middleware, required_headers_middleware


if __name__ == "__main__":
    # pretend setup a socket
    data = "..."
    request = decode_request(data)
    middleware_chain = required_headers_middleware(router)
    middleware_chain = logging_middleware(middleware_chain)

    response = middleware_chain(request)

    response_data = encode_response(response)
    # send that over the network


