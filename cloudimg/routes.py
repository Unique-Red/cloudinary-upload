from flask import render_template, request, redirect, url_for
from cloudimg import app, db
from .models import Create
import cloudinary
from flask_ckeditor import CKEditor
import os

cloudinary.config(
    cloud_name=f"{os.getenv('CLOUDINARY_CLOUD_NAME')}",
    api_key=f"{os.getenv('CLOUDINARY_API_KEY')}",
    api_secret=f"{os.getenv('CLOUDINARY_API_SECRET')}",
    api_env=f"{os.getenv('CLOUDINARY_URL')}"
)

import cloudinary.uploader
import cloudinary.api

ckeditor = CKEditor()
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

@app.route("/", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        text = request.form.get("text")
        files = request.files.getlist("files")

        upload_results = []
        for file in files:
            local_res = cloudinary.uploader.upload(file)
            upload_results.append(local_res['secure_url'])
            
        if not text:
            return ("Details cannot be empty!")
        else:
            post = Create(text=text, files=upload_results)
            db.session.add(post)
            db.session.commit()

            return redirect (url_for("display"))

    return render_template ("create.html")

@app.route("/display")
def display():
    posts = Create.query.all()
    return render_template ("display.html", posts=posts)