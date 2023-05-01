from flask import *
import mysql.connector


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check',methods=['GET'])
def check():
    registration_number= request.args.get('register number')
    mydb = mysql.connector.connect(
        host="db",port="3306",
        user="root",
        password="chicken65",
        database="studentdb"
    )


    mycursor = mydb.cursor()


    sql = "SELECT vaccinated FROM students WHERE registration_number = %s"
    val = (registration_number,)


    mycursor.execute(sql, val)


    result = mycursor.fetchone()


    if result:
        return "Vaccination Status: {} thank you for being vaccinated!".format(result[0])
    else:
        return "Student not found."


    
    
