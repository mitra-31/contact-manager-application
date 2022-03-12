from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_mysqldb import MySQL

app = Flask(__name__)


app.secret_key = '123456789'
  
  
#  Sql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactDB'
  

mysql = MySQL(app)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        secretkey = request.form['secretkey']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users(email, password, secret_key) VALUES(%s,%s,%s)',(email,password,secretkey))
        mysql.connection.commit()
        
        return redirect('/')
    
    return render_template('register.html')



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        error = ""
        
        # Post request data.
        email = request.form['email']
        password = request.form['password']
        
            
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,email,password FROM users WHERE email = % s AND password = % s', (email, password))
        account = cursor.fetchone()
        
        # check whether the account is correct. 
        if account:
            session['username'] = account[0]
            return redirect(url_for('dashboard'))
       
        # check email or password is incorrect
        else:
            error = "Username Or Password is incorrect."
            flash(error)
            return render_template('login.html')
        
    return render_template('login.html')



@app.route('/user',methods=['GET','POST'])
def dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT contactName,contactNUmber,contactEmail FROM contact WHERE userId = % s ',
                   (session['username'],))
    contacts = cursor.fetchall()
    return render_template('dashboard.html',contacts = contacts,n = len(contacts))



@app.route('/logout')
def logout():
    
    session.pop('email', None)
    
    return redirect('/')

@app.route('/add_contact',methods=['GET','POST'])
def add_contact():
    if request.method == 'POST':
        # Adding new contact to the database
        name = request.form["contact-name"]
        number = request.form["contact-number"]
        email = request.form["contact-email"]
        
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO contact(contactName,contactNUmber,contactEmail,userId) 
                       VALUES(%s,%s,%s,%s)''',
                       (name,number,email,session['username']))
        mysql.connection.commit()
    
        flash('Added Successfully')
    return redirect('/user')


if __name__ == '__main__':
    app.run(debug=True)