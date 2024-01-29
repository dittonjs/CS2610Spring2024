from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import string
import random
# Create your views here.

def index(req):
    return render(req, "core/index.html")


def passwords(req: HttpRequest):
    count = int(req.GET.get("count", 2))
    length = int(req.GET.get("length", 12))
    passwords = []
    for _ in range(count):
        password = "".join(
            random.choice(string.ascii_letters + string.digits) for _  in range(length)
        )
        passwords.append(password)

    context = {
        "passwords": passwords,
        "custom_message": "You are really great!"
    }
    return render(req, "core/passwords.html", context)