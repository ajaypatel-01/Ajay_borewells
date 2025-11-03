
# AJAY BOREWELLS — Demo Booking Website

Demo website (white & gold theme) for AJAY BOREWELLS. Built as a Flask app that saves bookings to a simple SQLite database (`bookings.db`).

## Features
- Multi-page site: Home, Availability (booking form), Contact
- Booking submissions saved to local SQLite database
- Admin view for bookings: `/admin/bookings`
- Uses the provided logo (static/images/logo.png)

## Run locally (Python 3.8+)
1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open in browser: http://127.0.0.1:5000/

## Notes
- This is a demo. For production you should add authentication for admin pages, input sanitation, and deploy with a WSGI server.
- To deploy on a server (like DigitalOcean) or platform (Render/Heroku), ensure you configure environment variables and use a production server.

