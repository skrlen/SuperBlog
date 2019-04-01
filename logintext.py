from sqlalchemy import create_engine
from orm import model
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/users",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
# from sqlalchemy import Column,String,Integer
session = sessionmaker()()


def insertUser(username,password):
    result = session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
    print(result)

def checkUser(username,password):
    result = session.query(model.User).filter(model.User.username==username).filter(model.User.password==password).first().id
    if result:
        return result
    else:
        return -1

def lookUser(username):
    result = session.query(model.User.id).filter(model.User.username==username).first()
    if result:
        return result
    else:
        return -1

def insertgoods(goodsname,pirce,userid):
    result = session.add(model.Goods(goodsname=goodsname,pirce=pirce,userid=userid))
    session.commit()
    session.close()
    print(result)

def checkGoods(userid):
    # result = session.query(model.Goods).filter(model.Goods.pirce).filter(model.Goods.id ==userid).first()
    res = session.query(model.Goods.id,model.Goods.goodsname,model.Goods.pirce).filter(model.Goods.userid ==userid).all()
    if res:
        return res
    else:
        return 0

def checkGoodsUserid(id):
    res = session.query(model.Goods.userid).filter(model.Goods.id ==id).all()

    if res:
        return res
    else:
        return 0

def checkGoodsById(id):
    # result = session.query(model.Goods).filter(model.Goods.pirce).filter(model.Goods.id ==userid).first()
    res = session.query(model.Goods.id,model.Goods.goodsname,model.Goods.pirce).filter(model.Goods.id ==id).all()
    print('<>>>>>>>>>',res)
    if res:
        print('-------->',res[0][1])
        return res
    else:
        return -1


def delGoods(id):
    result = session.query(model.Goods).filter(model.Goods.id == id).delete()
    session.commit()
    session.close()
    print(result)

#编辑
def updateGood(goodsname,pirce):
    res = session.query(model.Goods).filter(model.Goods.goodsname == goodsname).update({model.Goods.goodsname:goodsname,model.Goods.pirce:pirce})
    session.commit()
    return res