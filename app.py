from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('') / 'ecom.env'
load_dotenv(dotenv_path=env_path)

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

uri = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

engine = create_engine(uri, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)


class CartItem(Base):
    __tablename__ = 'cart_item'
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer)
    product_id = Column(Integer)
    product_count = Column(Integer)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    product_count = Column(Integer)


def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()


def get_user_profile_with_username(username):
    user_profile = session.query(User).filter(User.username == username).first()
    return user_profile


def authenticate_user(username, password):
    user_to_login = get_user_profile_with_username(username)

    if user_to_login:
        print(user_to_login.password)
        if user_to_login.password == password:
            print("login success!")
            return True
        else:
            print("login fail!")
            return False
    else:
        print("user not found!")


def view_user_profile_with_id(id):
    user_profile = session.get(User, id)
    print(user_profile.username)
    return user_profile


def create_product(name, description, price):
    new_product = Product(name=name, description=description, price=price)
    session.add(new_product)
    session.commit()


def list_all_products():
    product_list = session.query(Product).all()
    for i in product_list:
        print(i.name, i.description, i.price)
    return product_list


def get_product_details_with_id(id):
    product_to_list = session.get(Product, id)
    print(product_to_list.name, product_to_list.description)


def create_new_cart():
    pass


def add_product_to_cart():
    pass


def update_cart_item_quantity():
    pass


def remove_product_from_cart():
    pass


def view_cart():
    pass


def create_order_from_cart():
    pass


def view_order_history():
    pass


def view_order_details():
    pass
