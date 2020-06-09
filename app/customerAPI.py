from flask import Blueprint, request, jsonify
from models import db, Customer
import bcrypt
import helper_functions

customer_api = Blueprint('customer_api', __name__)


@customer_api.route("/customer", methods=['POST'])
@customer_api.route("/customer/", methods=['POST'])
def create_customer():
    data = request.get_json()
    customer_email = Customer.query.filter_by(email=data['email']).first()
    if customer_email is not None:
        return jsonify({'message': 'Customer email already exists'})

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_customer = helper_functions.populate_customer(data, hashed_password)
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'New  Customer created!'})


@customer_api.route("/")
def hello():
    return "Welcome to the customer_service_api"
