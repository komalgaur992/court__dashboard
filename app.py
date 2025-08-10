from flask import Flask, render_template, request, session, redirect, url_for, send_file
from scraper_enhanced import fetch_case_data
import sqlite3
from datetime import datetime
import random
import string
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

def generate_captcha_text(length=5):
    """Generate a random alphanumeric CAPTCHA text"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_captcha_image(text):
    """Create a CAPTCHA image using PIL"""
    # Create image with white background
    width, height = 200, 80
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except:
        try:
            font = ImageFont.load_default()
        except:
            font = None
    
    # Draw the text
    text_width = draw.textlength(text, font=font) if font else len(text) * 20
    text_height = 36
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with some distortion
    for i, char in enumerate(text):
        char_x = x + i * 35 + random.randint(-5, 5)
        char_y = y + random.randint(-5, 5)
        draw.text((char_x, char_y), char, fill='black', font=font)
    
    # Add some noise lines
    for _ in range(3):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill='gray', width=1)
    
    return image

@app.route('/')
def index():
    # Generate new CAPTCHA for each page load
    captcha_text = generate_captcha_text()
    session['captcha'] = captcha_text
    return render_template('index.html')

@app.route('/captcha')
def captcha_image():
    """Serve the CAPTCHA image"""
    captcha_text = session.get('captcha', '')
    if not captcha_text:
        captcha_text = generate_captcha_text()
        session['captcha'] = captcha_text
    
    image = create_captcha_image(captcha_text)
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/result', methods=['POST'])
def result():
    # Verify CAPTCHA
    user_captcha = request.form.get('captcha', '').upper()
    session_captcha = session.get('captcha', '')
    
    if not user_captcha or user_captcha != session_captcha:
        # Generate new CAPTCHA for retry
        captcha_text = generate_captcha_text()
        session['captcha'] = captcha_text
        return render_template('index.html', error="Invalid CAPTCHA. Please try again.")
    
    case_type = request.form.get("case_type")
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']
    result_data = fetch_case_data(case_type, case_number, filing_year)

    # Save query to SQLite with backward compatibility
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    
    # Check if table exists and get its schema
    c.execute("PRAGMA table_info(queries)")
    columns = [column[1] for column in c.fetchall()]
    
    # Create table with basic schema if it doesn't exist
    if not columns:
        c.execute("""CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            case_type TEXT, 
            case_number TEXT, 
            year TEXT, 
            timestamp TEXT
        )""")
        columns = ['id', 'case_type', 'case_number', 'year', 'timestamp']
    
    # Prepare data for insertion
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Insert basic data (backward compatible)
    c.execute("INSERT INTO queries (case_type, case_number, year, timestamp) VALUES (?, ?, ?, ?)",
              (case_type, case_number, filing_year, timestamp))
    conn.commit()
    conn.close()

    # Generate new CAPTCHA for next use
    captcha_text = generate_captcha_text()
    session['captcha'] = captcha_text
    
    return render_template('result.html', result=result_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
