from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/admin-login')
def admin_login():
    return render_template('admin-login.html')


@app.route('/customer-dashboard')
def customer_dashboard():
    return render_template('customer-dashboard.html')

@app.route('/submit-request')
def submit_request():
    return render_template('submit-request.html')

@app.route('/my-requests')
def my_requests():
    return render_template('my-requests.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/technicians')
def technicians():
    return render_template('technicians.html')

@app.route('/admins')
def admins():
    return render_template('admins.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')


if __name__ == '__main__':
    app.run(debug=True)