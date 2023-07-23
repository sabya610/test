from flask import Flask,jsonify,request
import psycopg2

app=Flask(__name__)
conn = psycopg2.connect(
      host = 
      port =
      database =
      user =
      password =
)

@app.route('/api/data',methods=['POST'])
def create_data():
    json_data = request.get_json()
    name = json_data['name']
    age = json_data['age']
    cursor = conn.cursor()
    ins_query = "INSERT INTO your_table (name,age) VALUES (%s,%s) 
    cursor.execute(ins_query,(name,age))
    conn.commit
    cursor.close()
    return jsonify({'message':'data created'})
if __name__ = '__main__'
   app.run(debug=True)
