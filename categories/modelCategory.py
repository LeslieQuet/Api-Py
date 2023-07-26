from flask_sqlalchemy import SQLAlchemy
import base64

db = SQLAlchemy()

class Categories(db.Model):
    CategoryId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CategoryName = db.Column(db.String(200), unique=True, nullable=False)
    Description = db.Column(db.String(200), nullable=False)
    Picture = db.Column(db.LargeBinary, nullable=True)

    def serialize(self):
        picture_base64 = base64.b64encode(self.Picture).decode("utf-8") if self.Picture is not None else None
        return {
            "CategoryId": self.CategoryId,
            "CategoryName": self.CategoryName,
            "Description": self.Description,
            "Picture": picture_base64
        }