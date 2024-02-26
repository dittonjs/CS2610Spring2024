from django.shortcuts import render
from .middleware import num_visits_middleware

# Create your views here.
@num_visits_middleware
def index(req):
    print(req.num_visits)
    return render(req, "core/index.html", {"num_visits": req.num_visits})


def dashboard(req):
    return render(req, "core/dashboard.html")


def profile(req):
    return render(req, "core/profile.html")