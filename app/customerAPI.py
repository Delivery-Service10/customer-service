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


@customer_api.route('/customer/id/<public_id>', methods=['GET'])
@customer_api.route('/customer/id/<public_id>/', methods=['GET'])
def get_one_customer(public_id):
    customer = Customer.query.filter_by(public_id=public_id).first()
    if not customer:
        return jsonify({'message': ' No customer found'})
    else:
        customer_data = helper_functions.allocate_data(customer)
        return jsonify({'customer': customer_data})


@customer_api.route('/customer', methods=['GET'])
@customer_api.route('/customer/', methods=['GET'])
def get_all_customers():

    customers = Customer.query.all()
    return jsonify({'customers': helper_functions.combine_results(customers)})


@customer_api.route('/customer/keyword/<keyword>', methods=['GET'])
@customer_api.route('/customer/keyword/<keyword>/', methods=['GET'])
def get_specified_customers(keyword):

    customers = Customer.query.filter(Customer.last_name.like("%" + keyword + "%"))
    return jsonify({'customers': helper_functions.combine_results(customers)})


@customer_api.route('/customer/<public_id>', methods=['DELETE'])
@customer_api.route('/customer/<public_id>/', methods=['DELETE'])
def delete_store(public_id):
    customer = Customer.query.filter_by(public_id=public_id).first()
    if not customer:
        return jsonify({'message': 'Customer not found'})
    else:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted'})


@customer_api.route("/")
def hello():
    return "Welcome to the customer_service_api"



