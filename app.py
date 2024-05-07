import sqlite3
from flask import Flask, render_template, send_file

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a table to store song metadata
c.execute('''CREATE TABLE IF NOT EXISTS songs
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, album TEXT, file_path TEXT)''')

# Dummy data for demonstration purposes
c.execute("INSERT INTO songs (title, artist, album, file_path) VALUES (?, ?, ?, ?)", ('Song 1', 'Artist 1', 'Album 1', 'music/song1.mp3'))
c.execute("INSERT INTO songs (title, artist, album, file_path) VALUES (?, ?, ?, ?)", ('Song 2', 'Artist 2', 'Album 2', 'music/song2.mp3'))
conn.commit()

@app.route('/')
def index():
    # Fetch all songs from the database
    c.execute("SELECT * FROM songs")
    songs = c.fetchall()
    return render_template('index.html', songs=songs)

@app.route('/music/<path:filename>')
def serve_music(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
