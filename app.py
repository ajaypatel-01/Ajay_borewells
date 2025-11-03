
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3, os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bookings.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            service TEXT NOT NULL,
            vehicle_type TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            notes TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

app = Flask(__name__)
app.secret_key = 'change-this-to-a-random-secret'

@app.before_first_request
def setup():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/availability', methods=['GET', 'POST'])
def availability():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        service = request.form.get('service')
        vehicle_type = request.form.get('vehicle_type')
        date = request.form.get('date')
        time = request.form.get('time')
        notes = request.form.get('notes')
        created_at = datetime.now().isoformat(timespec='seconds')

        # basic validation
        if not (name and phone and service and vehicle_type and date and time):
            flash('Please fill all required fields.', 'error')
            return redirect(url_for('availability'))

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""INSERT INTO bookings (name, phone, email, service, vehicle_type, date, time, notes, created_at)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, phone, email, service, vehicle_type, date, time, notes, created_at))
        conn.commit()
        conn.close()
        return render_template('booking_success.html', name=name, date=date, time=time, service=service)

    return render_template('availability.html')

@app.route('/contact')
def contact():
    owner = {
        'name': 'Adi Reddy',
        'phone': '9866972000',
        'email': 'adireddy6030@gmail.com'
    }
    return render_template('contact.html', owner=owner)

# Simple admin view to list bookings (no auth for demo)
@app.route('/admin/bookings')
def admin_bookings():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, name, phone, email, service, vehicle_type, date, time, notes, created_at FROM bookings ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('admin_bookings.html', bookings=rows)

if __name__ == '__main__':
    app.run(debug=True)
