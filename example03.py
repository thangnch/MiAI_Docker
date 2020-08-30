from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello():
    # MySQL param
    MYSQL_HOST = 'mysql'
    MYSQL_DB = 'mysql'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'password'
    rowcount = -1
    connection = None
    try:
        connection = mysql.connector.connect(host=MYSQL_HOST, database=MYSQL_DB, user=MYSQL_USER,
                                             password=MYSQL_PASS, port=3306, auth_plugin='mysql_native_password')
        mysql_insert_query = "SELECT * FROM mysql.user"
        print(mysql_insert_query)
        cursor = connection.cursor()
        cursor.execute(mysql_insert_query)
        records = cursor.fetchall()
        rowcount = cursor.rowcount

    except mysql.connector.Error as error:
        print("Fail login {}".format(error))
        ret_result = -1
    finally:
        if connection is not None:
            connection.close()
        del connection

    return "Total user numers = : "+  str(rowcount)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', use_reloader=False)