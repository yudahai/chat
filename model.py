#coding:utf-8
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Text, DateTime, Boolean, and_, or_, SmallInteger, func, Table
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
engine = create_engine('mysql://root:Dahai1985@localhost:3306/chat?charset=utf8')
Base = declarative_base()


user_chat = Table('user_chat', Base.metadata,
                  Column('to_user_id', Integer, ForeignKey('user.id')),
                  Column('chat_id', Integer, ForeignKey('chat.id'))
                  )


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    email = Column(String(50), index=True)
    password = Column(String(50), index=True)


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    content = Column(String(200))
    send_time = Column(DateTime, default=datetime.now)
    from_user_id = Column(Integer, ForeignKey('user.id'))

    from_user = relationship('User', foreign_keys=[from_user_id], backref=backref('send_chat'))
    to_user = relationship('User', secondary=user_chat, backref=backref('receive_chat'))


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
