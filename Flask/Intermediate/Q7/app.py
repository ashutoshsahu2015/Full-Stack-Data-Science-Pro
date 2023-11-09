# Problem Statement: Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

# Importing the libraries
from flask import Flask, render_template, url_for, redirect,g,request
import sqlite3

# Create an app
app = Flask(__name__)
app.config['DATABASE'] = 'items.db'

# Get DB method
def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row

    return db

# Route for homepage
@app.route('/')
def index():
    cursor = get_db().execute('SELECT * FROM items')
    items = cursor.fetchall()
    cursor.close()
    return render_template('index.html',items = items)

# Route for add item 
@app.route('/add_item',methods=['POST'])
def add_item():
    name = request.form['name']
    cursor = get_db().execute('INSERT INTO items (name) VALUES (?)',(name,))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))

# Route for Get Item
@app.route('/item/<int:item_id>',methods=['GET'])
def get_item(item_id):
    cursor = get_db().execute('SELECT * FROM items where id = ?',(item_id,))
    item = cursor.fetchone()
    cursor.close()
    return render_template('edit_item.html',item = item)

# Route for Edit Item
@app.route('/edit_item/<int:item_id>',methods=['POST'])
def edit_item(item_id):
    new_name = request.form['new_name']
    cursor = get_db().execute('UPDATE items SET name = ? WHERE id = ?',(new_name,item_id))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))

# Route for Delete Item
@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    cursor = get_db().execute('DELETE FROM items WHERE id = ?',(item_id,))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ =="__main__":
    app.run(host = '0.0.0.0',port = 5001, debug=True)