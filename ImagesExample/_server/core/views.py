from django.shortcuts import render
from django.conf  import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from pathlib import Path
from .models import File
from django.forms.models import model_to_dict

import secrets

# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
@login_required
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0]
    }
    return render(req, "core/index.html", context)


@login_required
def file_upload(req):
    new_file_name = secrets.token_hex(16)
    extension = req.FILES["my_file"].name.split(".", maxsplit=1)[1]
    file_path = f"/uploaded_files/{new_file_name}.{extension}"
    file = File(
        name=req.FILES["my_file"].name,
        path=file_path,
        user=req.user
    )
    file.save()

    with open(f"{Path.cwd()}{file_path}", "ab+") as f:
        for chunk in req.FILES["my_file"].chunks():
            f.write(chunk)

    return JsonResponse({"success": True})


@login_required
def files(req):
    files = File.objects.filter(user=req.user)
    files = [model_to_dict(file) for file in files]
    return JsonResponse({"files": files})

@login_required
def file(req, id):
    file = File.objects.get(id=id, user=req.user)
    f = open(f"{Path.cwd()}{file.path}", "rb")
    return FileResponse(f, as_attachment=True, filename=file.name)