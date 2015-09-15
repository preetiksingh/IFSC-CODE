from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="ifsc")


@app.route('/')
def presidentes():
    cur = db.cursor() 
    cur.execute("SELECT distinct bankname FROM ifsc;") 
    presidentes = cur.fetchall() 
    cur.close() 
    return render_template("template.html", presidentes=presidentes) 

@app.route('/<name>/', methods=['GET', 'POST'])
def hello_name(name):
  # If the user browsed /hello/John, the output would be
  # "Hello John!"
    name +="%"
    cur = db.cursor() 
    cur.execute("SELECT distinct state FROM ifsc where bankname like '%s';"%(name))
    presidentes = cur.fetchall() 
    cur.close() 
    return render_template("bank.html", presidentes=presidentes, name=name) 

@app.route('/<name>/<state>/', methods=['GET', 'POST'])
def hello_naaame(name,state):
  # If the user browsed /hello/John, the output would be
  # "Hello John!"
    name +="%"
    state +="%"
    cur = db.cursor() 
    cur.execute("SELECT distinct city FROM ifsc where bankname like '%s' and state like '%s';"%(name,state))
    presidentes = cur.fetchall() 
    cur.close() 
    return render_template("state.html", presidentes=presidentes , name=name , state=state) 

@app.route('/<name>/<state>/<city>/', methods=['GET', 'POST'])
def hello_naaaaame(name,state,city):
  # If the user browsed /hello/John, the output would be
  # "Hello John!"
    name +="%"
    state +="%"
    city +="%"
    cur = db.cursor() 
    cur.execute("SELECT address,branch,ifsc,contact FROM ifsc where bankname like '%s' and state like '%s' and city like '%s';"%(name,state,city))
    presidentes = cur.fetchall() 
    cur.close() 
    return render_template("city.html", presidentes=presidentes , name=name , state=state , city=city) 



if __name__ == '__main__':
    app.run(debug=True)