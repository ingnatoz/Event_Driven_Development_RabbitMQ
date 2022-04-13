from flask import Blueprint, jsonify
import requests

from models.Product import Product, ProductSchema, ProductUser, ProductUserSchema
from utils.db import db

product = Blueprint("product", __name__)


# Create migrations
@product.route('/generate_migration', methods=['GET'])
def migrations():
    db.drop_all()
    db.create_all()
    result = {'message': 'migrations ok!'}
    return jsonify(result)


@product.route('/', methods=['GET'])
def home():
    content = {'message': 'home :)'}
    return jsonify(content)


@product.route('/api/products', methods=['GET'])
def index():
    products = Product.get_all()
    serializer = ProductSchema(many=True)
    data = serializer.dump(products)
    return jsonify(data), 200


@product.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.win.localhost:86/api/user/')
    json = req.json()
    print(json)
    try:
        product_user = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })
