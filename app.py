from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

uri = 'mysql+pymysql://root:isThisWeak!@localhost/test_db'
engine = create_engine(uri, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


def create_user(username, password):
    new_user = User(name=username, password=password)
    session.add(new_user)
    session.commit()

def authenticate_user():
    pass


def view_user_profile():
    pass


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


create_user("test_name", "test_pw")