from django.shortcuts import render, redirect
from .models import Note

# notes

#index - everything /notes/ GET
#show - specific thing /notes/1/ GET
#create - create a thing /notes/ POST
#update - update a specific thing /notes/1/ PUT/PATCH
#delete - delete a specific thing /notes/1/ DEL

# Create your views here.
def index(req):
    notes = Note.objects.all()
    # read the notes out of the database and put them on the screen
    return render(req, "core/index.html", {"notes": notes})

def show_note(req, id):
    print(type(id))
    note = Note.objects.get(pk=id)
    return render(req, "core/note.html", {"note": note})

def create_note(req):
    print(req.POST)
    note = Note(
        title=req.POST.get("title"),
        content=req.POST.get("content")
    )
    note.save()
    # create a note in the database
    return redirect("/")