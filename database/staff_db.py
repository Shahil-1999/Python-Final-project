import mysql.connector

mysql = mysql.connector.connect(host = "localhost", user = "root", passwd = "Shahil@1999")
mycursor = mysql.cursor()


def insert_staff(u, p):
    
    
    
    mycursor.execute("create database if not exists city_hospitals")

    mycursor.execute("use city_hospitals")
    
    # creating table for storing the username and password of the user
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
    mycursor.execute("insert into user_data values('" + u + "','" + p + "')")
    mysql.commit()


def show_staffdb(un):
    mycursor.execute("select password from city_hospitals.user_data where username='" + un + "'")
    row = mycursor.fetchall()
    return row

    
def show_all_staffdb():
    mycursor.execute("select * from city_hospitals.user_data")
    row1 = mycursor.fetchall()
    return row1


def delete_stafftdb(un):
    mycursor.execute("delete from city_hospitals.user_data where username='" + un + "'")
    mysql.commit()
    
    