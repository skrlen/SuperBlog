from flask import Flask,render_template,request,redirect,make_response
import datetime
from orm import model
app = Flask(__name__)
# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
app.debug=True
# 将 http://127.0.0.1:5000/ 和index视图函数绑定
@app.route('/')
def index():
    # return "<h1>hellozzy</h1>"

    # 需要从数据库查询书籍列表

    user = None
    user = request.cookies.get("name")
    if user:
        print("之前已经登录过")
    else:
        print("之前没有登录过")

    return render_template('index.html',userinfo = user)

@app.route("/news/<int:num>")
def news(num):
    # print('当前为第',num,"页")
    # 根据num传入  查询数据库 查询第num页显示内容
    # 在视图函数可以获取URL变量
    return render_template("news.html",pagenews= ['股票又涨了','房价又降了','又要放假了'])

@app.route("/regist", methods = ["POST", "GET"])
def regist():
    if request.method == "GET":
        # print(name, value1)
        # print('收到get请求','返回注册页面')
        return render_template("regist.html")
    elif request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        # print(username, password)
        # print('收到post请求', '可以提取表单参数')
        # return  "注册成功"
        # 自动在URL 发起请求 请求list
        return redirect('/login')


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 查询数据库
        print(username,password)
        # return "登录成功"

        # 内容需要查询数据库
        # 第一种 不带接口
        # return render_template("list.html",infoarray = [1,2,3,4,5])
        # 第二种 带接口 重定向
        # 自动在URL 发起请求 请求list

        # 为了让响应可以携带头信息 ，需要构造响应
        res = make_response(redirect('/list'))
        res.set_cookie('name',username, expires = datetime.datetime.now() + datetime.timedelta(days=7))
        return res

@app.route("/quit")
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie("name")
    return res


@app.route("/list")
def list():
    user = None
    user = request.cookies.get("name")
    # 内容需要查询数据库
    return render_template("list.html",infoarray = [1,2,3,4,5],userinfo = user)

@app.route("/detail/<id>")
def detail(id):
    print("当前商品为",id)
    user = None
    user = request.cookies.get("name")
    # 从数据库查询商品详情
    return render_template("detail.html", detail="这个东东非常好",id = id,userinfo = user)

if __name__ == "__main__":
    app.run()