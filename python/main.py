from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="person"
)


@app.route('/')
def index():
    # Create a cursor
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `personinfo`")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)


@app.route('/add', methods=['POST'])
def add_data():
    name = request.form.get('name')
    cursor = db.cursor()
    cursor.execute("INSERT INTO personinfo (name) VALUES (%s)", (name,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
