from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config

from controllers.product_controller import product

app = Flask(__name__)
# Configure the SqlAlchemy part of the app instance
app.config.from_object(config)
CORS(app)
# Create the SqlAlchemy db instance
SQLAlchemy(app)
# Initialize Marshmallow
Marshmallow(app)

# Routes
app.register_blueprint(product)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
