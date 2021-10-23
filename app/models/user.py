from sqlalchemy import Column, String, Integer
from sqlalchemy.ext import declarative
from app import Base


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(50), nullable=False, unique=True)
	password = Column(String(50), nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return f'<User> {self.username}'




