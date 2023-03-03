import mysql.connector

mysql = mysql.connector.connect(host = "localhost", user = "root", passwd = "Shahil@1999")
mycursor = mysql.cursor()


def insert_patient(patient_id, name, sex, age, address, contact, mail, disease, f_pred, p_pred):

    mycursor.execute("create database if not exists city_hospitals")
    mycursor.execute("use city_hospitals")
    
     # creating the tables for storing patient details.
    mycursor.execute("create table if not exists patient_detail(patient_id int(4) primary key, name varchar(30) ,sex varchar(15),age int(3),address varchar(50),contact varchar(15),mail varchar(40), disease varchar(80), breasr_cancer_prediction varchar(20), parkinson_disease_prediction varchar(20))")

    # Inserting Patient Details
    mycursor.execute("insert into patient_detail values('" + patient_id + "','" + name + "','" + sex + "','" + age + "','" + address + "','" + contact + "','" + mail + "','" + disease + "','" + f_pred + "','" + p_pred + "')")
    mysql.commit()
    


def show_patientdb(patient_id):
    mycursor.execute("SELECT * FROM city_hospitals.patient_detail where patient_id ='" + patient_id + "'")
    row = mycursor.fetchall()
    return row


def delete_patientdb(patient_id):
    mycursor.execute("delete from city_hospitals.patient_detail where patient_id='" + patient_id + "'")
    mysql.commit()


def show_all_patientdb():
    mycursor.execute("SELECT * FROM city_hospitals.patient_detail")
    row1 = mycursor.fetchall()
    return row1
