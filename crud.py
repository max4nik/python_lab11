import copy
import json

from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from model.abstract_gemstone import AbstractGemstone

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URL = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'.format(
    user=SECRET['user'],
    password=SECRET['password'],
    host=SECRET['host'],
    port=SECRET['port'],
    db=SECRET['db'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class AbstractGemstoneForDB(AbstractGemstone, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(32), unique=False)
    price_in_usd_dollars = db.Column(db.Float, unique=False)
    country_of_origin = db.Column(db.String(32), unique=False)
    chemical_formula = db.Column(db.String(64), unique=False)
    weight_in_carats = db.Column(db.Float, unique=False)
    transparency_from_zero_to_one = db.Column(db.Float, unique=False)

    # change
    connection_protocol = db.Column(db.String(64), unique=False)
    data_transfer_amount = db.Column(db.Float, unique=False)

    def __init__(self, color='N/A', price_in_usd_dollars=0, country_of_origin='N/A', chemical_formula='N/A',
                 weight_in_carats=0, transparency_from_zero_to_one=0, connection_protocol='net',
                 data_transfer_amount=0):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula,
                         weight_in_carats, transparency_from_zero_to_one)
        self.connection_protocol = connection_protocol
        self.data_transfer_amount = data_transfer_amount


class AbstractGemstoneSchema(ma.Schema):
    class Meta:
        fields = ('color', 'price_in_usd_dollars', 'country_of_origin', 'chemical_formula',
                  'weight_in_carats', 'transparency_from_zero_to_one', 'connection_protocol', 'data_transfer_amount')


smart_abstract_gemstone_schema = AbstractGemstoneSchema()
smart_abstract_gemstones_schema = AbstractGemstoneSchema(many=True)


@app.route('/gemstone', methods=['POST'])
def add_gemstone():
    gemstone = AbstractGemstoneForDB(request.json['color'],
                                     request.json['price_in_usd_dollars'],
                                     request.json['country_of_origin'],
                                     request.json['chemical_formula'],
                                     request.json['weight_in_carats'],
                                     request.json['transparency_from_zero_to_one'],
                                     request.json['connection_protocol'],
                                     request.json['data_transfer_amount'])
    db.session.add(gemstone)
    db.session.commit()
    return smart_abstract_gemstone_schema.jsonify(gemstone)


@app.route('/gemstone', methods=['GET'])
def get_gemstone():
    all_abstract_gemstone = AbstractGemstoneForDB.query.all()
    result = smart_abstract_gemstones_schema.dump(all_abstract_gemstone)
    return jsonify({'gemstones': result})


@app.route('/gemstone/<id>', methods=['GET'])
def get_gemstone_by_id(id):
    gemstone = AbstractGemstoneForDB.query.get(id)
    if not gemstone:
        abort(404)
    return smart_abstract_gemstone_schema.jsonify(gemstone)


@app.route('/gemstone/<id>', methods=['PUT'])
def update_gemstone_by_id(id):
    gemstone = AbstractGemstoneForDB.query.get(id)
    if not gemstone:
        abort(404)
    old_gemstone = copy.deepcopy(gemstone)
    gemstone.color = request.json['color']
    gemstone.price_in_usd_dollars = request.json['price_in_usd_dollars']
    gemstone.country_of_origin = request.json['country_of_origin']
    gemstone.chemical_formula = request.json['chemical_formula']
    gemstone.weight_in_carats = request.json['weight_in_carats']
    gemstone.transparency_from_zero_to_one = request.json['transparency_from_zero_to_one']
    gemstone.connection_protocol = request.json['connection_protocol']
    gemstone.data_transfer_amount = request.json['data_transfer_amount']
    db.session.commit()
    return smart_abstract_gemstone_schema.jsonify(old_gemstone)


@app.route('/gemstone/<id>', methods=['DELETE'])
def delete_gemstone_by_id(id):
    gemstone = AbstractGemstoneForDB.query.get(id)
    if not gemstone:
        abort(404)
    db.session.delete(gemstone)
    db.session.commit()
    return smart_abstract_gemstone_schema.jsonify(gemstone)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host=SECRET['host'], port=5000)
