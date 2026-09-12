from flask import Flask, request, redirect, jsonify, render_template
import sqlite3
import string
import random

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

DATABASE = "database.db"
BASE_URL = "http://127.0.0.1:5000/"

# ----------------------------
# Database Setup
# ----------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE,
            long_url TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ----------------------------
# Generate Short Code
# ----------------------------
def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# ----------------------------
# API: Shorten URL
# ----------------------------
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json(silent=True) or {}
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_code()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Ensure unique code
    while True:
        cursor.execute("SELECT * FROM urls WHERE short_code=?", (short_code,))
        if not cursor.fetchone():
            break
        short_code = generate_code()

    cursor.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)",
                   (short_code, long_url))
    conn.commit()
    conn.close()

    short_url = BASE_URL + short_code
    return jsonify({"short_url": short_url})

# ----------------------------
# Redirect Route
# ----------------------------
@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT long_url FROM urls WHERE short_code=?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return jsonify({"error": "URL not found"}), 404

# ----------------------------
# Run Server
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)