from flask import app, redirect, render_template, url_for
from forms import LoginForm  # Importing the LoginForm class from forms.py

# Your Flask routes and application setup...

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
