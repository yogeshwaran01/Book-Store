from datetime import datetime

from app import database as db


class Posts(db.Model):  # type: ignore
    """ Database Table for Blog post """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title} -> {self.timestamp}"
