import uuid
from models import Customer

def combine_results(customers):
    output =[]
    for customer in customers:
        customer_data = allocate_data(customer)
        output.append(customer_data)
    return output


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


def allocate_data(customer):
    customer_data = {'public_id': customer.public_id,
                     'email': customer.email,
                     'first_name': customer.first_name,
                     'last_name': customer.last_name,
                     'addressLine1': customer.addressLine1,
                     'addressLine2': customer.addressLine2,
                     'city': customer.city,
                     'district': customer.district,
                     'country': customer.country
                  }
    return customer_data
