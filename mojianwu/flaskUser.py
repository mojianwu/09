#coding:utf-8
import MySQLdb, json
from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = '12343243'
conn = MySQLdb.connect(host='192.168.31.228', port=3306, user='root', passwd='root', db='mo')
conn.autocommit(True)
cur = conn.cursor()

@app.route('/')
def Index():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:    
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginAction')
def loginAction():
    name = request.args.get('inputName')
    pwd  = request.args.get('inputPwd')
    if name == '1' and pwd == '1':
        session['username'] = 'admin'
    return redirect(url_for('Index'))

@app.route('/show')
def Show():
    sql  = 'select * from server'
    cur.execute(sql)
    data = cur.fetchall()
    return json.dumps(data)

@app.route('/add')
def Add():
    host = request.args.get('host')
    mem  =  request.args.get('mem')
    sql  = 'insert into server(host, memory) values("%s", %s)' %(host, mem)
    cur.execute(sql)
    return 'ok'

@app.route('/del')
def Del():
    ID   = request.args.get('id')
    sql  = 'delete from server where id = %s' %(ID)
    cur.execute(sql)
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)