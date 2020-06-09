import uuid
from models import Customer


def populate_customer(data, hashed_password):
    new_customer = Customer(public_id=str(uuid.uuid4()),
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            email=data['email'],
                            password=hashed_password,
                            addressLine1=data['addressLine1'],
                            addressLine2=data['addressLine2'],
                            city=data['city'],
                            district=data['district'],
                            country=data['country']
                      )
    return new_customer
