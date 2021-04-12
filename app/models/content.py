from app import database as db


class Title(db.Model):  # type: ignore

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150))

    def __repr__(self) -> str:
        return f"{self.id}"


class About(db.Model):  # type: ignore

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.id}"


class Note(db.Model): # type: ignore

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    info = db.Column(db.Text())
    link = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.title}"
