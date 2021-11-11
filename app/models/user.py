from sqlalchemy import Column, String, Integer
from sqlalchemy.ext import declarative
from app import Base


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(50), nullable=False, unique=True)
	hashed = Column(String(50), nullable=False)
	salt = Column(String(50), nullable=False)

	def __init__(self, username, hashed, salt):
		self.username = username
		self.hashed = hashed
		self.salt = salt

	def __repr__(self):
		return f'<User> {self.username}'




