from script import *
import socket
from datetime import date, timedelta
import time
from configparser import ConfigParser
import sys
import mysql.connector
import threading

def connectSQL(host, user, password, database_name):
  try:
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database_name
    )
    print("Database found successfully.")
    return mydb
  except:
    sys.exit("Database not found!")

def insertData(mycursor, table, data):
    sql = f"INSERT INTO {table} (date, time, lat, lon, device_id) VALUES (%s, %s, %s, %s, %s)"

    try:
        mycursor.execute(sql, data)
        print("Data inserted successfully.")
    except:
        # print(val)
        sys.exit("Data not inserted!")

def server_program():
    val = [] #data to be entered in the database

    # get the hostname
    file= 'Config.ini'
    config= ConfigParser()
    config.read(file)
    
    host = socket.gethostname()
    port = int(config['Port']['port'])  # Call port from Config File
    print(port)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()
    while True:
          # accept new connection
        #threading.Thread(target=client, args=(addr,)).start()
    
        print("Connection from: " + str(address))
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        data = str(data)
        #while(data[-1] != '<'):
            #data = data[:-1]
        #print(data)
        
        if not data:
            break
        #print("from connected user: " + str(data))
       
        print(data)
        '''
        try:
          val = text_EV(data)
          val.append(extended_EV(data))

          mydb = connectSQL(config['Database']['host'], config['Database']['user'], config['Database']['password'], config['Database']['database_name'])
          mycursor = mydb.cursor()

          insertData(mycursor, config['Database']['table'], val)
          mydb.commit()
        except:
          print("Text is not in correct format")
        '''
        
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
