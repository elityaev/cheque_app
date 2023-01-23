from sqlalchemy import (
    create_engine, Column, Integer,
    DateTime, String, Float, Boolean, ForeignKey, Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from .config import Setting as settings

engine = create_engine(settings.DB_URL)
Base = declarative_base()


class Receipt(Base):
    __tablename__ = 'receipts_receipt'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    organization = Column(String(256))
    summa = Column(Float)
    processing = Column(Boolean, default=False)
    products = relationship('Product', backref='receipt', lazy='dynamic')


class Product(Base):
    __tablename__ = 'receipts_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Float)
    price = Column(Float)
    sum = Column(Float)
    sub_category_id = Column(
        Integer, ForeignKey('receipts_subcategory.id'))
    receipt_id = Column(Integer, ForeignKey('receipts_receipt.id'))
    description = Column(Text)
    tag = Column(String(25))


class Category(Base):
    __tablename__ = 'receipts_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    sub_categories = relationship('SubCategory', backref='sub_category',
                                     lazy='dynamic')


class SubCategory(Base):
    __tablename__ = 'receipts_subcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    category_id = Column(Integer, ForeignKey('receipts_category.id'))
    products = relationship(Product, backref='sub_category',
                              lazy='dynamic')


Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session()