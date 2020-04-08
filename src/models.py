import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    fullname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    profile_picture = Column(String(250), nullable=False)
    likes = Column(Boolean, default=False)
    
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    followers = Column(Integer)
    followed_by = Column(Integer)
    personal_description = Column(String(250))
    tagged_photos = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    posts = relationship('Post',  uselist=False)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    picture = Column(String(250))
    caption = Column(String(250), nullable=False)
    created_time = Column(DateTime, index=True, default=datetime.utcnow) 
    user_id = Column(Integer, ForeignKey('users.id'))
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    comment_followers = relationship('Comment')

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    created_time = Column(DateTime, index=True, default=datetime.utcnow)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')