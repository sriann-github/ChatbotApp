from flask import Flask, jsonify, request
import pyodbc
import debugpy

app = Flask(__name__)

# Database connection details
server = 'eastus-sqlserver.database.windows.net'
database = 'eastus-sqldb'
username = 'SqlAdmin'
password = 'adminPass123'
driver = '{ODBC Driver 18 for SQL Server}'

# Attach debugpy to a specific port
debugpy.listen(("0.0.0.0", 5001))  
print("Debugger is listening on port 5001. Attach your debugger to continue.")

def get_db_connection():  
  conn = pyodbc.connect(f'DRIVER={driver};Server=tcp:sqlsrvr-eastus.database.windows.net,1433;Database=Sqldb-eastus;Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
  return conn

#Endpoint to fetch all emails
@app.route('/emails', methods=['GET'])
def get_emails():
  conn = None
  print("Hello")
  try:    
      conn = get_db_connection()
      print(str(conn))
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM Emails")
      columns = [column[0] for column in cursor.description]
      data = [dict(zip(columns, row)) for row in cursor.fetchall()]
      return jsonify(data)
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  finally:
    if conn:
      conn.close()
    
#Endpoint to fetch email details by Incident ID
@app.route('/emails/<incident_id>', methods=['GET'])
def get_email_by_incident_id(incident_id):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Emails WHERE incident_id = ?", (incident_id))
    row = cursor.fetchone()
    if row:
      columns = [column[0] for column in cursor.description]
      data = dict(zip(columns, row))
      return jsonify(data)
    else:
      return jsonify({"error": "Incident ID not found"}), 404
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  finally:
    conn.close()

# Run the flask app
if __name__== '__main__':
  app.run(debug=True, host='127.0.0.1', port=5001)

