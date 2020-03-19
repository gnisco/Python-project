import os
from flask import Flask, render_template, redirect, request, url_for
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
    
@app.route('/full-width')
def fullwidth():
    return render_template("full-width.html")
    

    
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
    
@app.route('/sidebar')
def sidebar():
    return render_template("sidebar.html")

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    appointments = mongo.db.appointments
    appointments.insert_one(request.form.to_dict())
    return redirect(url_for('appointments'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)