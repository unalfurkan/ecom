from sqlalchemy import create_engine, Float
from sqlalchemy_utils import database_exists, create_database

import os
from dotenv import load_dotenv
from pathlib import Path


class Create:
    env_path = Path('') / 'ecom.env'
    load_dotenv(dotenv_path=env_path)

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_name = os.environ.get("DB_NAME")

    uri = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    engine = create_engine(uri, echo=True)

    if not database_exists(engine.url):
        create_database(engine.url)
        from sqlalchemy import Table, Column, Integer, String, MetaData
        meta = MetaData()

        users = Table(
            'user', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('username', String(256)),
            Column('password', String(128))
        )
        product = Table(
            'product', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(256)),
            Column('description', String(1028)),
            Column('price', Float)
        )
        cart = Table(
            'cart', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('user_id', Integer)
        )
        cart_item = Table(
            'cart_item', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('cart_id', Integer),
            Column('product_id', Integer),
            Column('product_count', Integer)
        )
        order = Table(
            'order', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('user_id', Integer)
        )
        order_item = Table(
            'order_item', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('order_id', Integer),
            Column('product_id', Integer),
            Column('product_count', Integer)
        )

        meta.create_all(engine)

    else:
        print("Given DB already exists...")
        engine.connect()
