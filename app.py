from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models import db, Hero, HeroPower, Power
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Welcome to the Heroes API!"

#-------------------get all heroes-------------------#

@app.route('/heroes', methods=['GET'])
def get_all_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200
#---------------------------------------------------#

#-------------------get hero by id-------------------#
@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero_by_id(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return jsonify(hero.to_dict()), 200
#---------------------------------------------------#

#----------------------powers-----------------------#
@app.route('/powers', methods=['GET'])
def get_all_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200
#---------------------------------------------------#

#------------------get power by id------------------#
@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power_by_id(power_id):
    power = Power.query.get_or_404(power_id)
    return jsonify(power.to_dict()), 200
#---------------------------------------------------#

#------------------patch power by id------------------#
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return {"error": "Power not found"}, 404

    try:
        data = request.get_json()
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        return {"errors": [str(e)]}, 400
#---------------------------------------------------#

#------------------post hero_power------------------#
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    try:
        data = request.get_json()
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()

        hero = Hero.query.get(data['hero_id'])
        return jsonify(hero.to_dict()), 201
    except Exception as e:
        return {"errors": [str(e)]}, 400
#---------------------------------------------------#

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)


