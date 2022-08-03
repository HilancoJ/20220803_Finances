from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
	return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
	return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		firstName = request.form.get('firstName')
		password = request.form.get('password')
		confirm_password = request.form.get('confirm_password')

		if len(email) < 4:
			print(email)
			flash('Email must have more than 3 characters.', category='error')
		elif len(firstName) < 2:
			flash('First name must have more than 1 character.', category='error')
		elif password != confirm_password:
			flash('The passwords don\'t match', category='error')
		elif len(password) < 7:
			flash('Password must have more than 6 character.', category='error')
		else:
			flash('Account created!', category='success')

	return render_template("sign_up.html")