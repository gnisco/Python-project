import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog-home-1')
def bloghome1():
    return render_template("blog-home-1.html")
    
@app.route('/blog-home-2')
def bloghome2():
    return render_template("blog-home-2.html")

@app.route('/blog-post')
def blogpost():
    return render_template("blog-post.html")
    
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
    
@app.route('/pricing')
def pricing():
    return render_template("pricing.html")
    
@app.route('/services')
def services():
    return render_template("services.html")
    
@app.route('/sidebar')
def sidebar():
    return render_template("sidebar.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)