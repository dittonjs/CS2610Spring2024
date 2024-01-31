from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    # read the notes out of the database and put them on the screen
    return render(req, "core/index.html")

def notes(req):
    # create a note in the database
    return redirect("/")