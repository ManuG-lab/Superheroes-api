from faker import Faker
from random import choice, randint
from app import app
from models import db, Hero, Power, HeroPower

fake = Faker()

def seed_data():
    print("🧹 Clearing existing data...")
    HeroPower.query.delete()
    Power.query.delete()
    Hero.query.delete()
    db.session.commit()

    print("🌱 Seeding heroes...")
    heroes = []
    for _ in range(10):
        hero = Hero(
            name=fake.name(),
            super_name=fake.first_name() + fake.word().capitalize(),
            power=choice(["Flight", "Invisibility", "Telepathy", "Super Strength", "Speed"])
        )
        heroes.append(hero)
    db.session.add_all(heroes)
    db.session.commit()

    print("🌱 Seeding powers...")
    powers = []
    for _ in range(5):
        description = fake.sentence(nb_words=3)
        # Truncate if longer than 20 characters to pass validation
        if len(description) > 20:
            description = description[:20]
        power = Power(
            name=fake.word().capitalize(),
            description=description
        )
        powers.append(power)
    db.session.add_all(powers)
    db.session.commit()

    print("🌱 Seeding hero powers...")
    hero_powers = []
    for _ in range(15):
        hero = choice(heroes)
        power = choice(powers)
        strength = choice(["Strong", "Average", "Weak"])
        hero_power = HeroPower(
            hero_id=hero.id,
            power_id=power.id,
            strength=strength
        )
        hero_powers.append(hero_power)
    db.session.add_all(hero_powers)
    db.session.commit()

    print("✅ Done seeding!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()
