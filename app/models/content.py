from app import database as db

class Note(db.Model): # type: ignore

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    info = db.Column(db.Text())
    link = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.title}"
