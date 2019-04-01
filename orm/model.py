from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://root:123456@localhost/users",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
from sqlalchemy import Column,String,Integer,ForeignKey
# session = sessionmaker()()


class User(Base):
    __tablename__= 'user'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)



class Goods(Base):
    __tablename__='goods'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    goodsname = Column(String(20),nullable=False)
    pirce = Column(Integer,nullable=False)
    userid = Column(Integer,ForeignKey('user.id', ondelete = 'CASCADE'))

if __name__ == "__main__":
    res = Base.metadata.create_all(bind=engine)
