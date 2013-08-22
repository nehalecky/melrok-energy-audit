from flask import render_template, request, flash
from forms import ContactForm
from app import app

# index
#-------------
@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')


# about 
#-------------
@app.route('/about')
def about():
    return render_template('about.html')


# contact
#-------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
  
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'
    elif request.method == 'GET':
        return render_template('contact.html', form=form)    
