from app import database as db


class Contact(db.Model):  # type: ignore
    """ Database Table for Contact details """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    message = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.name} -> {self.email}"
