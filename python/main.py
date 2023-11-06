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


# mao ni ang mu redirect sa add data


@app.route('/adddata', methods=['GET'])
def redirect_add():
    return render_template('add.html')

# mao ni ang pang delete


@app.route('/delete/<int:id>', methods=['POST'])
def delete_data(id):
    # Delete the data from the database based on the 'id'
    cursor = db.cursor()
    cursor.execute("DELETE FROM `personinfo` WHERE person_ID = %s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

# mao ni pang edit


@app.route('/editdata/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    # Retrieve data for the specified row ID
    data = get_data_by_id(id)

    if request.method == 'GET':
        # Display the edit form with existing data
        return render_template('editdata.html', id=id, data=data)

    elif request.method == 'POST':
        # Process the edit request and update the data
        update_data(id, request.form)
        # Redirect to the 'index' route, not '/table'
        return redirect(url_for('index'))


def get_data_by_id(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `personinfo` WHERE person_ID = %s", (id,))
    data = cursor.fetchone()
    cursor.close()
    return data


def update_data(id, form):
    name = form['name']
    age = form['age']
    gender = form['gender']
    weight = form['weight']
    height = form['height']

    cursor = db.cursor()
    cursor.execute("UPDATE personinfo SET name = %s, age = %s, gender = %s, weight = %s, height = %s WHERE person_ID = %s",
                   (name, age, gender, weight, height, id))
    db.commit()
    cursor.close()


@app.route('/editdata', methods=['GET'])
def redirect_edit():
    return render_template('editdata.html', id=id, data=data)


if __name__ == "__main__":
    app.run(debug=True)
