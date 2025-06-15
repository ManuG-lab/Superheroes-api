from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    power = db.Column(db.String(100), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')


    def __repr__(self):
        return f"<Hero {self.super_name} (ID: {self.id})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'power': self.power
        }
    

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Power {self.name} (ID: {self.id})>"
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
    @validates('description')
    def validate_power_description(self, key, value):
        if value and len(value) > 20:
            raise ValueError("Power description cannot exceed 20 characters")
        return value
    def description_must_not_be_empty(self, key, value):
        if not value:
            raise ValueError("Description cannot be empty")
        return value
    
    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    
    def __repr__(self):
        return f"<HeroPower Hero ID: {self.hero_id}, Power ID: {self.power_id}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'strength': self.strength,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'hero': {
                'id': self.hero.id,
                'name': self.hero.name,
                'super_name': self.hero.super_name
            },
            'power': self.power.to_dict()
        }
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ["Strong", "Weak", "Average"]:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return value
    