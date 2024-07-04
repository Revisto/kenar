from flask import Flask
from db.models import db
from routes import main

app = Flask(__name__)
app.register_blueprint(main)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.secret_key = 'your_secret_key_here'

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=5000)