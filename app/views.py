from flask import render_template
from flask import request

from app import app
from app import admin
from app import database as db
from app.models.content import Title
from app.models.content import About
from app.models.content import Note
from app.models.books import Book
from app.models.books import Subject
from app.models.contact import Contact
from app.models.blogs import Posts
from app.models import Db_Handler
from app.models import Blogs_Manager
from app.utils.admin import Authenticate
from app.utils.url_maker import make_title_from_url

brand = Db_Handler.return_title()

@app.errorhandler(404)
def page_not_found(e):
    """ Handling page_not_found 404 error """
    return (
        render_template(
            "error.html",
            head=404,
            message_1="Sorry, You are Lost",
            message_2="Page is not available",
            title="404",
        ),
        404,
    )


@app.errorhandler(500)
def page_not_found(e):
    """ Handling page_not_found 404 error """
    return (
        render_template(
            "error.html",
            head=500,
            message_1="Internal Server Error",
            message_2="Sorry for Inconvince",
            title="500",
        ),
        500,
    )


@app.route("/")
@app.route("/index")
def index():

    return render_template("index.html", t_about=Db_Handler.return_about(), head=brand, title=brand, notes=Db_Handler.return_notes())


@app.route("/books/<sub_>")
def book_section(sub_):
    sub = make_title_from_url(sub_)
    return render_template(
        "book.html",
        subs=Db_Handler.all_subjects(),
        posts=Db_Handler.all_books_of(sub),
        head=sub,
        title=sub,
        content=sub,
    )


@app.route("/books")
def books():
    return render_template(
        "subjects.html",
        subs=Db_Handler.all_subjects(),
        head="Books",
        title="Books - " + brand,
        content="Books - " + brand,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        head="About",
        title="About - " + brand,
        content="Books - " + brand,
    )


@app.route("/contact", methods=["POST", "GET"])
def contact():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        a = Db_Handler.PostData(name, email, message)
        return render_template("contact.html", head=a["message"])
    return render_template("contact.html", head="Contact" , title="Contact - " + brand, content="Contact - "+ brand)


@app.route("/post/<title_>")
def post_title(title_):
    """
    Route for post with particular Title
    """
    title = make_title_from_url(title_)
    if title in Blogs_Manager.TablePost.all_title():
        return render_template(
            "post.html",
            post=Blogs_Manager.TablePost.query_by_title(title),
            content=title,
            title=title,
            head=title,
        )
    else:
        return page_not_found(404)


@app.route("/posts")
def posts():
    """ Route for all posts """
    return render_template(
        "posts.html",
        posts=Blogs_Manager.TablePost.all_query(),
        head="Blogs",
        title="Blogs - " + brand,
    )


admin.add_view(Authenticate(Title, db.session))
admin.add_view(Authenticate(About, db.session))
admin.add_view(Authenticate(Subject, db.session))
admin.add_view(Authenticate(Book, db.session))
admin.add_view(Authenticate(Contact, db.session))
admin.add_view(Authenticate(Posts, db.session))
admin.add_view(Authenticate(Note, db.session))

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

import os
from flask import url_for

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
