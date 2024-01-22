def logging_middleware(next):
    def middleware(req):
        # do something with the input
        print(f"{req.method} {req.uri}")

        # call next middleware
        res = next(req)
        #do something with the response
        print(f"{res.code} {res.reason}")
        # return the thing the caller
        return res

    return middleware
