from dataclasses import dataclass
from utils.db import db, ma
from sqlalchemy import UniqueConstraint


@dataclass
class Product(db.Model):
    id: int
    title: str
    ml_product: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    ml_product = db.Column(db.String(200))

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    ml_product = ma.auto_field()


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


class ProductUserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProductUser
        load_instance = True

    id = ma.auto_field()
    user_id = ma.auto_field()
    product_id = ma.auto_field()
