from sqlalchemy import Column, Integer, String

from modules import db



class Order(db.Model):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    title = Column(String)
