import os
import bcrypt
from flask import (
    Flask, flash, render_template, redirect, request, url_for, session, flash, g)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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

@app.route('/schedule')
def schedule():
    return render_template("schedule.html", appointments=mongo.db.appointments.find())
    
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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("adminlogin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("adminlogin"))

    return render_template("adminlogin.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("admin_login"))

@app.route('/order', methods=['POST'])
def order_entry():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    entries = sorted(entries, key=lambda d: d['title'])
    return render_template('show_entries.html', entries=entries)

@app.route('/end_session')
def end_session():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def error_page(e):
    
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.secret_key = 'kEysarEsEcrEt'
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
