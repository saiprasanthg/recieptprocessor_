from flask import Flask
from flask_cors import CORS
from app.routes import receipt_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)  # ✅ Enable CORS globally
    app.register_blueprint(receipt_blueprint)
    return app
