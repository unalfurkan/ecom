from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
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


def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()


# create_user("test_name33", "test_pw33")

def authenticate_user():
    pass


def view_user_profile_with_id(id):
    user_profile = session.get(User, id)
    print(user_profile.username)


view_user_profile_with_id(1)


def create_product():
    pass


def list_all_products():
    pass


def get_product_details():
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
