from django.shortcuts import render, redirect
from .models import Note, Task
from django.http import HttpResponseNotFound
import json
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

def create_task(req, id):
    task = Task(
        content=req.POST.get("content", ""),
        is_completed=False,
        note_id=id
    )

    task.save()
    return redirect(f"/notes/{id}/")


def delete_note(req, id):
    try:
        note = Note.objects.get(pk=id)
        note.delete()
        return redirect("/")
    except Note.DoesNotExist as e:
        return HttpResponseNotFound()


def update_task(req, id):
    body = json.loads(req.body)
    task = Task.objects.get(pk=id)
    task.is_completed = body.get("is_completed", False)
    task.save()
    return redirect("/")

