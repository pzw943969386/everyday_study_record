from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.before_request
def x():
    print('这里先开始')

@app.after_request
def y(response):
    print('这里先结束')
    return response

@app.route('/x1', methods=['GET','POST'])
def x1():
    print('视图函数1')
    return '视图函数1'

@app.route('/x2', methods=['GET','POST'])
def x2():
    print('视图函数2')
    return '视图函数2'

if __name__=='__main__':
    app.run(debug=True)