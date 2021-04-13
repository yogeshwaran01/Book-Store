from app import database as db
from .content import Title
from .content import About
from .content import Note
from .books import Subject
from .books import Book
from .contact import Contact
from .blogs import Posts
from app.utils.url_maker import make_url_from_title
import markdown
from typing import Any


class Db_Handler:
    @staticmethod
    def return_title():
        try:
            return Title.query.all()[0].text
        except IndexError:
            return None

    @staticmethod
    def return_about():
        return About.query.all()[0].text

    @staticmethod
    def all_books_of(name: str):
        subs = Subject.query.filter_by(name=name).first()
        return subs.books

    @staticmethod
    def all_subjects():
        return [i for i in Subject.query.all()]

    @staticmethod
    def PostData(name: str, email: str, message: str) -> dict:
        """
        Method add contact data to the db
        """
        con = Contact(name=name, email=email, message=message)
        db.session.add(con)
        db.session.commit()
        return {"status": 200, "message": "Message sended successfully"}

    @staticmethod
    def return_notes():

        return Note.query.all()


class Blogs_Manager:
    """
    Class that directly interacts with database
    """

    class TablePost:
        """ Class handele the Post table in db """

        @staticmethod
        def all_query() -> list:
            """
            Method returns lists of all posts from database
            """
            data = []
            posts = Posts.query.all()
            for post in posts:
                x = {
                    "title": post.title,
                    "body": post.body,
                    "timestamp": post.timestamp,
                    "id": post.id,
                    "url": make_url_from_title(post.title),
                }
                data.append(x)
            return data

        @staticmethod
        def query_by_id(_id: int) -> dict:
            """
            Method returns post for given id from db
            """
            post = Posts.query.filter_by(id=_id).first()
            if post is None:
                return {"status": 404, "message": "No id Available"}
            return {
                "title": post.title,
                "body": markdown.markdown(post.body),
                "timestamp": post.timestamp,
                "id": post.id,
                "url": make_url_from_title(post.title),
            }

        @staticmethod
        def query_by_title(title: str) -> dict:
            """
            Method returns post for given id from db
            """
            post = Posts.query.filter_by(title=title).first()
            if post is None:
                return {"status": 404, "message": "No Post Available"}
            return {
                "title": post.title,
                "body": markdown.markdown(post.body),
                "timestamp": post.timestamp,
                "id": post.id,
                "url": make_url_from_title(post.title),
            }

        @staticmethod
        def all_id() -> list:
            """
            Method return all id of the post
            """
            return [str(i["id"]) for i in Blogs_Manager.TablePost.all_query()]

        @staticmethod
        def all_title() -> list:
            """
            Method returns all titles of the posts from db
            """
            return [i["title"] for i in Blogs_Manager.TablePost.all_query()]

        @staticmethod
        def title_by_id(id_: int) -> Any:
            """
            Return the title of the post for given id
            """
            post = Posts.query.filter_by(id=id_).first()
            if post is None:
                return "404"
            return post.title

        @staticmethod
        def PostData(title: str, body: str) -> dict:
            """
            Method add blog posts data to the db
            """
            post = Posts(title=title, body=body)
            db.session.add(post)
            db.session.commit()
            return {"status": 200, "message": "Data Posted successfully"}
