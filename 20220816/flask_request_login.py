from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'dsadsaddsa'

@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if user is None:
        return redirect('/login')

@app.after_request
def y(response):
    print('这里先结束')
    return response

@app.route('/login', methods=['GET','POST'])
def x1():
    print('视图函数1')
    return '视图函数1'

@app.route('/index', methods=['GET','POST'])
def x2():
    print('视图函数2')
    return '视图函数2'

@app.errorhandler(404)
def page_not_found(error):
    return 'this page done not exist', 404

if __name__=='__main__':
    app.run(debug=True)