# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DATETIME

engine = create_engine('sqlite:///database.sqlite3', echo=True)
metadata = MetaData()
metadata.bind = engine

stream = Table(
    'stream', metadata,
    Column('id', String, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('startdate', DATETIME)
)

stcomment = Table(
    'st_comment', metadata,
    Column('id', String, primary_key=True),
    Column('date', DATETIME, primary_key=True),
    Column('amount', Integer)
)

stview = Table(
    'st_view', metadata,
    Column('id', String, primary_key=True),
    Column('date', DATETIME, primary_key=True),
    Column('amount', Integer)
)

sttotalview = Table(
    'st_total_view', metadata,
    Column('date', DATETIME, primary_key=True),
    Column('ammount', Integer)
)