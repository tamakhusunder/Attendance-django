# * ---------- IMPORTS --------- *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import psycopg2
import cv2
import numpy as np
import re
from datetime import datetime
import mysql.connector

# Get the relativ path to this file (we will use it later)
FILE_PATH = os.path.dirname(os.path.realpath(__file__))

# * ---------- Create App --------- *
app = Flask(__name__)
CORS(app, support_credentials=True)



# * ---------- DATABASE CONFIG --------- *
# DATABASE_USER = os.environ['ROOT']
# DATABASE_PASSWORD = os.environ['12345678']
# DATABASE_HOST = os.environ['localhost']
# DATABASE_PORT = os.environ['3306']
# DATABASE_NAME = os.environ['project']

def DATABASE_CONNECTION():
    return mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
                )




def check(t1,code):
    # time_str = '13::55::26'
    # time_object = datetime.strptime(time_str, '%H::%M::%S').time()
    # print(type(time_object))
    # print(time_object)
    mydb = DATABASE_CONNECTION()

    cur = mydb.cursor()
    sql = ("""SELECT MAX(time) FROM faceapp_attendancetb WHERE t_id='{}'""".format(code))
    print(sql)
    cur.execute(sql)
    if t1 is not None:
        t1 = datetime.strptime(str(t1),'%H:%M:%S.%f').time()
        t2 = datetime.now().time()
        interval=datetime.combine(datetime.today(), t2) - datetime.combine(datetime.today(), t1)
        minutes = interval.total_seconds() / 60
        if minutes<5:
            return 0
        else:
            return 1
    else:
        return 1


# * --------------------  ROUTES ------------------- *
# * ---------- Get data from the face recognition ---------- *
@app.route('/receive_data', methods=['POST'])
def get_receive_data():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data['name'])
        name=json_data['name']
       
        mydb = DATABASE_CONNECTION()
        cur = mydb.cursor()
        print(mydb)


        sql1 = ("SELECT code FROM faceapp_staffinfo WHERE name ='{}'".format(name))
        print(sql1)

        cur.execute(sql1)
        code = cur.fetchall()
        # code='730320'
        print(code[0][0])
        c=code[0][0]
        # datetime object containing current date and time
        time = datetime.now().time()
        date = datetime.today().strftime('%Y-%m-%d')
        # date = datetime.strptime(str(date), "%Y-%m-%d")

        sql = """SELECT MAX(time) FROM faceapp_attendancetb WHERE t_id='{}'""".format(c)
        cur.execute(sql)
        time1=cur.fetchall()
        t=time1[0][0]
        print(type(t),t)
        sts=check(t,c)

        status='p'
        if sts==1:
            sql=('''INSERT INTO faceapp_attendancetb( date, time, status,t_id)
                VALUES
                ('{}','{}','{}','{}')
                '''.format(date,time,status,c))
            print(sql)
            cur.execute(sql)
            mydb.commit() 
    return jsonify(json_data)






#        
                                 
# * -------------------- RUN SERVER -------------------- *
if __name__ == '__main__':
    # * --- DEBUG MODE: --- *
    app.run(host='127.0.0.1', port=5000, debug=True)
    #  * --- DOCKER PRODUCTION MODE: --- *
    # app.run(host='0.0.0.0', port=os.environ['PORT']) -> DOCKER
