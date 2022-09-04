from cloudimg import db
from sqlalchemy.dialects.sqlite import JSON

class Create(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    files = db.Column(JSON, nullable=False)

db.create_all()