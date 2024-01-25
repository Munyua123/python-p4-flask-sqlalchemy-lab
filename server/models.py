from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)

    animals = db.relationship('Animal', back_populates='zookeepers')

    def __repr__(self):
        return f'<Zookeeper {self.name}, {self.birthday}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', back_populates='enclosures')

    def __repr__(self):
        return f'<Enclosure {self.environment}, {self.open_to_visitors} >'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper = db.Column(db.String, db.ForeignKey('zookeepers.name'))
    enclosure = db.Column(db.String, db.ForeignKey('enclosures.environment'))

    zookeepers = db.relationship('Zookeeper', back_populates='animals')
    enclosures = db.relationship('Enclosure', back_populates='animals')

    def __repr__(self):
        return f'<Animal {self.name}, {self.species}, {self.zookeeper}, {self.enclosures}>'
