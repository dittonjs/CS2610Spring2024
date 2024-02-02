from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def index(req):
    notes = Note.objects.all()
    # read the notes out of the database and put them on the screen
    return render(req, "core/index.html", {"notes": notes})

def notes(req):
    print(req.POST)
    note = Note(
        title=req.POST.get("title"),
        content=req.POST.get("content")
    )
    note.save()
    # create a note in the database
    return redirect("/")