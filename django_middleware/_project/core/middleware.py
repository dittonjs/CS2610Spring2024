
def num_visits_middleware(next):
    def middleware(req):
        num_visits = int(req.COOKIES.get("num_visits", 0)) + 1
        req.num_visits = num_visits
        res = next(req)
        res.set_cookie("num_visits", num_visits)
        return res

    return middleware