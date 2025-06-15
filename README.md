# 🦸‍♂️ Superheroes API

A RESTful Flask API for managing superheroes and their powers. Built with SQLAlchemy, Flask-Migrate, and Faker for seed data.

## 📦 Features

- Manage `Heroes`, `Powers`, and their relationship via `HeroPower`
- Full CRUD support
- Validations for strength and description
- JSON API responses
- Seed data using Faker
- Ready for deployment on Render

---

## 🛠️ Tech Stack

- Python 3.12
- Flask
- SQLAlchemy
- Flask-Migrate
- Faker
- Gunicorn (for production)

---

## 🚀 Getting Started

### 1. Clone the repo

bash
 1.git clone https://github.com/ManuG-Lab/superheroes-api.git
   cd superheroes-api

 2. Create and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
 3. Install dependencies
    pip install -r requirements.txt
    
 4. Set up the database
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    
 5. Seed the database
    python seed.py
    
10. Run the app locally
    flask run
    Open http://127.0.0.1:5000

🧪 API Endpoints

Method	Endpoint	Description

-GET	/heroes	Get all heroes

-GET	/heroes/<id>	Get hero by ID

-POST	/hero_powers	Assign a power to a hero

-GET	/powers	Get all powers

-GET	/powers/<id>	Get power by ID

-PATCH	/powers/<id>	Update power description

🧾 Project Structure
.
├── app.py

├── models.py

├── seed.py

├── requirements.txt

├── Procfile

├── migrations/

└── README.md


🧪 Requirements
Make sure requirements.txt includes:

Flask
Flask-SQLAlchemy
Flask-Migrate
gunicorn
Faker

Generate it with:
pip freeze > requirements.txt


🌍 Deployment (Render)
Push your project to GitHub.

-Go to Render.com

-Click "New Web Service"

-Connect your GitHub repo

-Set the Build Command:

-pip install -r requirements.txt

-Set the Start Command:

-gunicorn app:app

Click Deploy.

👨‍💻 Author's
GitHub: @ManuG-lab








