
import sqlite3
from flask import Flask, request, jsonify # type: ignore
from geopy.distance import geodesic # type: ignore

app = Flask(__name__)

# Database Setup
def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        genre TEXT,
                        owner TEXT,
                        location_lat REAL,
                        location_lon REAL
                      )''')
    conn.commit()
    conn.close()

@app.route('/add_book', methods=['POST'])
def add_book():
    try:
        data = request.json
        with sqlite3.connect('books.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, genre, owner, location_lat, location_lon) VALUES (?, ?, ?, ?, ?)",
                           (data['title'], data['genre'], data['owner'], data['location_lat'], data['location_lon']))
            conn.commit()
        return jsonify({'message': 'Book added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/search_books', methods=['GET'])
def search_books():
    try:
        user_lat = float(request.args.get('lat'))
        user_lon = float(request.args.get('lon'))
        genre = request.args.get('genre')
        radius = float(request.args.get('radius', 10))  # Default radius 10km

        user_location = (user_lat, user_lon)

        with sqlite3.connect('books.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE genre = ?", (genre,))
            books = cursor.fetchall()

        results = []
        for book in books:
            book_location = (book[4], book[5])
            distance = geodesic(user_location, book_location).km
            if distance <= radius:
                results.append({'title': book[1], 'genre': book[2], 'owner': book[3], 'distance_km': round(distance, 2)})

        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
