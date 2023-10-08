"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

class Cupcake(db.Model):
    """cupcake"""
    __tablename__ = "Cupcakes"
    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    flavor = db.Column(db.Text,
                       nullable = False)
    size = db.Column(db.Text,
                     nullable = False)
    rating = db.Column(db.Float,
                       nullable = False)
    image = db.Column(db.Text,
                      nullable = False, 
                      default = 'https://tinyurl.com/demo-cupcake')
    
    def serialize(self):
        return{
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        """show info about cupcake"""
        c = self
        return f"<Cupcake {c.id} {c.flavor} {c.size} {c.rating} {c.image}>"