from app import database as db
from app.utils.url_maker import make_url_from_title


class Subject(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    books = db.relationship("Book", backref="sub")

    def url(self):
        return make_url_from_title(self.name)

    def len(self):
        return len(self.books)

    def __repr__(self):
        return f"{self.name} -> {len(self.books)}"


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    author = db.Column(db.String(140))
    link = db.Column(db.String(140))
    sub_id = db.Column(db.Integer, db.ForeignKey("subject.id"))

    def __repr__(self):
        return f"{self.name} -> {self.author}"
