from django.shortcuts import render
from django.http import HttpRequest
import secrets

# Create your views here.
def index(req: HttpRequest):
    num_visits = int(req.COOKIES.get("num_visits", 0)) + 1
    res = render(req, "core/index.html", {"num_visits": num_visits})
    res.set_cookie("sesson_token", secrets.token_hex(32))
    res.set_cookie("num_visits", num_visits)
    return res