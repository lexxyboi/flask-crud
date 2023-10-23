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
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `personinfo`")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)


@app.route('/add', methods=['POST'])
def add_data():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    weight = request.form.get('weight')
    height = request.form.get('height')

    cursor = db.cursor()
    cursor.execute("INSERT INTO personinfo (name, age, gender, weight, height) VALUES (%s, %s, %s, %s, %s)",
                   (name, age, gender, weight, height))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

# mao ni ang pang edit


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    if request.method == 'GET':
        # Retrieve the data for editing from the database based on the 'id'
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `personinfo` WHERE id = %s", (id,))
        data_to_edit = cursor.fetchone()
        cursor.close()
        return render_template('edit.html', data=data_to_edit)
    elif request.method == 'POST':
        # Update the data in the database based on the 'id'
        new_name = request.form.get('name')
        cursor = db.cursor()
        cursor.execute(
            "UPDATE personinfo SET name = %s WHERE id = %s", (new_name, id))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))

# mao ni ang pang delete


@app.route('/delete/<int:id>', methods=['POST'])
def delete_data(id):
    # Delete the data from the database based on the 'id'
    cursor = db.cursor()
    cursor.execute("DELETE FROM `personinfo` WHERE person_ID = %s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
