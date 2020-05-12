import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'appt_booking'
app.config["MONGO_URI"] = 'mongodb+srv://gnisco:Rainbow123@cluster0-fijio.mongodb.net/appt_booking?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin_login')
def adminlogin():
    return render_template("admin_login.html")

@app.route('/appointments')
def appointments():
    return render_template("appointments.html", appointments=mongo.db.appointments.find())


@app.route('/booking')
def booking():
    return render_template("booking.html", services=mongo.db.services.find())


@app.route('/blog-home-1')
def bloghome1():
    return render_template("blog-home-1.html")
    
@app.route('/blog-home-2')
def bloghome2():
    return render_template("blog-home-2.html")

@app.route('/blog-post')
def blogpost():
    return render_template("blog-post.html")

@app.route('/book-appointments')
def bookappointments():
    return render_template("book-appointments.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")
    
@app.route('/portfolio-1-col')
def portfolio1col():
    return render_template("portfolio-1-col.html")
    
@app.route('/portfolio-2-col')
def portfolio2col():
    return render_template("portfolio-2-col.html")
    
@app.route('/portfolio-3-col')
def portfolio3col():
    return render_template("portfolio-3-col.html")
    
@app.route('/portfolio-4-col')
def portfolio4col():
    return render_template("portfolio-4-col.html")
    
@app.route('/portfolio-item')
def portfolioitem():
    return render_template("portfolio-item.html")
    
@app.route('/services')
def services():
    return render_template("services.html", services=mongo.db.services.find())

@app.route('/services_admin')
def servicesadmin():
    return render_template("services_admin.html", services=mongo.db.services.find())

@app.route('/add_services')
def addservices():
    return render_template("add_services.html", services=mongo.db.services.find())
    
@app.route('/sidebar')
def sidebar():
    return render_template("sidebar.html")

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    appointments = mongo.db.appointments
    appointments.insert_one(request.form.to_dict())
    return redirect(url_for('appointments'))

@app.route('/edit_service/<service_id>')
def edit_service(service_id):
    the_service =  mongo.db.services.find_one({"_id": ObjectId(service_id)})
    return render_template('edit_service.html', service=the_service)

@app.route('/update_service/<service_id>', methods=["POST"])
def update_service(service_id):
    services = mongo.db.services
    services.update( {'_id': ObjectId(service_id)},
    {
        'service_type':request.form.get('service_type'),
        'service_name':request.form.get('service_name'),
        'service_description': request.form.get('service_description'),
        'service_cost': request.form.get('service_cost'),
    })
    return redirect(url_for('servicesadmin'))

@app.route('/add_service')
def add_service():
    return render_template('add_service.html', services=mongo.db.services.find())


@app.route('/insert_service', methods=['POST'])
def insert_service():
    services =  mongo.db.services
    services.insert_one(request.form.to_dict())
    return redirect(url_for('servicesadmin'))

@app.route('/delete_service/<service_id>')
def delete_service(service_id):
    mongo.db.services.remove({'_id': ObjectId(service_id)})
    return redirect(url_for('servicesadmin'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        if password == '' or username == '':
            error = 'Please enter a username and password'
            return render_template('index.html')

        existing_user = mongo.db.users.find_one({'username' : username})

        if existing_user is None:
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(14))
            mongo.db.users.insert_one({
                'username' : username, 
                'password' : hashed_password
            })
            session['username'] = username
            return redirect(url_for('index'))

        else:
            flash('This username already exists!')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("THE DATA:")
    print(request.data)

    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
        login_user = mongo.db.users.find_one({'username' : username})

        
    
        if login_user:
            hashed_password = login_user['password']
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                session['username'] = username
                return redirect(url_for('index', user_id = username ))
            else:
                flash('Invalid Username or Password, Please try again.')
                return render_template(url_for('adminlogin'))
        else:
            flash('Invalid Username or Password, Please try again.')
        
    return render_template("admin_login.html")

@app.route('/end_session')
def end_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'kEysarEsEcrEt'
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
