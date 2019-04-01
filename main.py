'''
flask模块引用
'''
from flask import Flask,render_template,request,redirect,make_response
import datetime,random
import logintext as e
from orm import model
app=Flask(__name__)

app.send_file_max_age_default = datetime.timedelta(seconds=1)

#将http//127.0.0.1:500 和 index视图函数绑定
@app.route('/')
def index():
    user = None
    user = request.cookies.get("name")
    res = datetime.datetime.now()
    res=str(res)
    res = res[11:13:]
    res = int(res)
    print('_________--------===>>',res)
    if user:
        print("之前登陆过")
    else:
        print("没有登录过")

    return render_template('首页.html',userinfo = user,res = res)


@app.route('/regist',methods=['POST','GET'])
def regist():


    if request.method=='GET':

        return render_template('regist.html')

    elif request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        try:
            e.insertUser(username,password)
            return redirect('/login')
        except:
            return redirect('/regist')


@app.route("/list",methods=['GET','POST'])
def list():
    if request.method =='GET':
        user = None
        # id = None
        user = request.cookies.get("name")
        pwd = e.lookUser(user)
        asd = e.checkGoods(pwd[0])
        if asd == 0:
            asd = '0'
            return render_template("list.html",infoarray=asd,userinfo = user)
        else:

            return render_template("list.html",infoarray=asd,userinfo = user)
    elif request.method == 'POST':
        goodsname = request.form['goodsname']
        pirce = request.form['pirce']
        try:
            user = request.cookies.get("name")
            pwd = e.lookUser(user)
            e.insertgoods(goodsname,pirce,pwd[0])
            return redirect('/list')

        except:
            return redirect('/list')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")

    elif request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        try:
            asd = e.checkUser(username,password)
            res = make_response(redirect('/list'))
            res.set_cookie('name', username,  expires=datetime.datetime.now() + datetime.timedelta(days=7))
            return res

        except:

            return redirect('/login')


@app.route('/addgoods',methods=['GET','POST'])
def addgoods():
    if request.method=='GET':
        return render_template('addgoods.html')

@app.route('/readme')
def readme():
    return render_template("/加入我们.html")


@app.route('/delt/<id>')
def delt(id):

    e.delGoods(id)
    return redirect('/list')


@app.route('/updated',methods=['GET','POST'])
def updated():
    if request.method=='GET':

        return render_template("updateGoods.html")

    elif request.method=='POST':
        try:
            # 获取当前用户id
            user = request.cookies.get("name")
            pwd = e.lookUser(user)

            # 获取用户输入的商品编号
            res = request.form['id']
            res = int(res)
            aa = e.checkGoodsUserid(res)
            if aa == 0:
                return render_template("updateGoods.html")

            elif pwd[0] == aa[0][0]:
                res = int(res)
                goods = e.checkGoodsById(res)
                return render_template("updateGoods.html",id=res,goods=goods)
            else:
                return render_template("updateGoods.html")
        except:
            return redirect("/updateGoods")


@app.route('/upd',methods=['GET','POST'])
def upd():
    if request.method =='GET':
        return render_template("updateGoods.html")
    elif request.method=='POST':

        res = request.form['goodsname']
        asd = request.form['pirce']
        e.updateGood(res,asd)
        return redirect("/list")


@app.route('/quit')
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie("name")
    return res


@app.route("/detail/<id>")
def detail(id):
    print("当前商品为:",id)
    user=None
    # res = random.choices['这个东西是又大又圆','放在碗里是又长又宽','嚼起来是筋筋到到','这和你吃皮没关系']
    user = request.cookies.get("name")
    return render_template('detail.html', detail='放在碗里是又长又宽',id=id,userinfo = user)


if __name__=='__main__':
    app.run(host='192.168.12.132', port=5000,debug=True)