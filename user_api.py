from flask import Flask

app= flask(__name__)

def db_Conn(dbname,host,password,port):
   db = sqlite3.connect('dbname')
   c_cursor = db.cursor()
   c_cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY_KEY AUTOINCREMENT,name TEXT, email TEXT)")
   db.commit()

@app.route('/api/users',methods=['GET'])
def get_users():
    db = sqlite3.connect('dbname')
    c_cursor = db.cursor()
    c_cursor.execute('SELECT * from users')
    users=[{'id':row[0],'name':row[1],'email':row[2]} for row in c_cursor.fetchall()]
    db.close()
@app.route('/api/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    db = sqlite3.connect('dbname')
    c_cursor = db.cursor()
    c_cursor.execute("SELECT * from users where id = ?", (user_id,))
    user = c_cursor.fetchone()
    db.close()
    if user:
        user_id ={'id'= user[0], 'name' : user[1] , 'email' : user[2] }
        return jsonify(user_dict)
    else:
        return jsonify({'message' : 'User not found'}),404
