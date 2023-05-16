import os
import voice.speak as sp
import voice.command as cmd
import voice.wish as ws
import mail.email as email
import disease_pred.parkinson as park
import database.patient_db as p_details
import database.staff_db as sd


while (True):

    
    Admin_passwd = os.environ.get("Admin_Password")


    while (True):
        ws.wishMe()
        print("Disease Prediction System for Parkinson Disease using Voice Command")
        sp.speak("Disease Prediction System for Parkinson Disease using Voice Command")
        
        print("""       
                        1. Registration
                        2. Sign In
                        3. Show Admin database
                        """)
        sp.speak("""press 1 for Registration
                    press 2 for Sign In
                    press 3 for Show Admin database""")
        

        r = int(input("enter your choice: "))
        if r == 1:
            print("""
                !!!!!!!!!!Register Yourself!!!!!!!!""")


            sp.speak(("Please Enter username..."))
            u = input("Enter username!!:")


            sp.speak("Please Enter password(Password Must Be Strong)...")
            p = input("Enter Your password (Password must be strong!!!): ")

            show_userdb = sd.show_staffdb(u)
            
            if len(show_userdb):
                print("Username Already Registered choose different username")
                sp.speak("Username Already Registered choose different username")
            else:
                sd.insert_staff(u, p)

                print("""
                ============================================
                !!Well Done!!Registration Done Successfully!!
                ============================================
                                                    """)
                sp.speak("Registration Done Sucessfully...")

            sp.speak("Press any key to continue")
            os.system("pause")
            

        # IF USER WANTS TO LOGIN
        elif r == 2:
            print("""
                    ==================================
                    !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                    ==================================
                                                        """)
            
            print("Please Verify Your Credentials")
            sp.speak("Please Verify Your Credentials")

            print("Please Enter Your Username")
            sp.speak("Please Enter Your Username")
            un = input("Username!!: ")
            

            print("Please Enter Your Password")
            sp.speak("Please Enter Your Password")
            ps = input("Password!!: ")
            
            

            row = sd.show_staffdb(un)
            for i in row:
                a = list(i)
                if a[0] == str(ps):
                    while(True):
                        print("""
                                    1. Administration
                                    2. Patient(Details)
                                    3. Show patient database
                                    4. Sign Out
                                                    """)
                        sp.speak(""""
                                    press 1 for Administration
                                    press 2 for Patient(Details)
                                    press 3 for Show patient database
                                    press 4 for Sign Out
                                                    """)
                        
                        a = int(input("ENTER YOUR CHOICE: "))
                        if a == 1:
                            print("""
                                    1. Log patient Record
                                    2. Discharge Summary
                                    """)

                            sp.speak("""
                                    press 1 for Log patient Record
                                    press 2 for Discharge Summary
                                    """)
                        
                            
                            
                            x = int(input("ENTER YOUR CHOICE: "))
                            if x == 1:

                                print("""
                                        1. Add New Patient
                                        
                                        """)
                                sp.speak("press 1 Add New Patient")
                                b = int(input("Enter Your Choice: "))

                                # adding new patient
                                if b == 1:
                                    print("If You Want to insert patient details manually then press M, or If you want to add patient details through voice then press V")
                                    sp.speak("If You Want to insert patient details manually then press M, or If you want to add patient details through voice then press V")
                                    p_d = input("Enter Your response: ")
                                    
                                    
                                    if p_d.lower() == 'm':
                                        print("Please Enter Your patient ID")
                                        sp.speak("Please Enter Your patient ID")
                                        patient_id = input("Patient ID: ")

                                        print("Please Enter Your Name")
                                        sp.speak("Please Enter Your Name")
                                        name = input("Name: ")

                                        print("Please Enter Your Gender")
                                        sp.speak("Please Enter Your Gender")
                                        sex = input("Gender: ")

                                        print("Please Enter your Age")
                                        sp.speak("Please Enter your Age")
                                        age = input("Age: ")

                                        print("Please Enter Your Address")
                                        sp.speak("Please Enter Your Address")
                                        address = input("Address: ")

                                        print("Please Enter Your Contact Number")
                                        sp.speak("Please Enter Your Contact Number")
                                        contact = input("Contact Details: ")

                                        print("Please Enter Your Email")
                                        sp.speak("Please Enter Your Email")
                                        mail = input("Mail Id: ")

                                        print("Please Enter Your Disease")
                                        sp.speak("Please Enter Your Disease")
                                        disease = input("Disease: ")

                                    elif p_d.lower() == "v":
                                        
                                    
                                        
                                    
                                    
                                        print("Please Enter Your patient ID")
                                        sp.speak("Please Enter Your patient ID")
                                        patient_id = cmd.takeCommand().lower()
                                        print(patient_id)
                                        sp.speak(patient_id)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        patient_id_satisfaction = input("Enter your value : ")
                                        if patient_id_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_patient_id = input("Enter New Value : ")
                                            patient_id = (new_input_patient_id)
                                            print(patient_id)
                                            sp.speak(patient_id)
                                      
                                            
                                             
                                        
                                        print("Please Enter Your Name")
                                        sp.speak("Please Enter Your Name")
                                        name = cmd.takeCommand().lower()
                                        print(name)
                                        sp.speak(name)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        name_satisfaction = input("Enter your value : ")
                                        if name_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_name = input("Enter New Value : ")
                                            name = (new_input_name)
                                            print(name)
                                            sp.speak(name)
                                            
                                            
                                        print("Please Enter Your Gender")
                                        sp.speak("Please Enter Your Gender")
                                        sex = cmd.takeCommand().lower()
                                        print(sex)
                                        sp.speak(sex)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        gender_satisfaction = input("Enter your value : ")
                                        if gender_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_gender = input("Enter New Value : ")
                                            sex = (new_input_gender)
                                            print(sex)
                                            sp.speak(sex)
                                            
                                            

                                        print("Please Enter Your Age")
                                        sp.speak("Please Enter Your Age")
                                        age = cmd.takeCommand().lower()
                                        print(age)
                                        sp.speak(age)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        age_satisfaction = input("Enter your value : ")
                                        if age_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_age = input("Enter New Value : ")
                                            age= (new_input_age)
                                            print(age)
                                            sp.speak(age)

                                        print("Please Enter Your Address")
                                        sp.speak("Please Enter Your Address")
                                        address = cmd.takeCommand().lower()
                                        print(address)
                                        sp.speak(address)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        address_satisfaction = input("Enter your value : ")
                                        if address_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_address = input("Enter New Value : ")
                                            address = (new_input_address)
                                            print(address)
                                            sp.speak(address)

                                        print("Please Enter Your Contact number")
                                        sp.speak("Please Enter Your contact Number")
                                        contact = cmd.takeCommand().lower()
                                        print(contact)
                                        sp.speak(contact)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        contact_satisfaction = input("Enter your value : ")
                                        if contact_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_contact = input("Enter New Value : ")
                                            contact = (new_input_contact)
                                            print(contact)
                                            sp.speak(contact)

                                        print("Please Enter Your Email")
                                        sp.speak("Please Enter Your Email")
                                        mail = cmd.takeCommand().lower()
                                        print(mail)
                                        sp.speak(mail)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        mail_satisfaction = input("Enter your value : ")
                                        if mail_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_mail = input("Enter New Value : ")
                                            mail = (new_input_mail)
                                            print(mail)
                                            sp.speak(mail)

                                        
                                        print("Please Enter Your Disease")
                                        sp.speak("Please Enter Your disease")
                                        disease = cmd.takeCommand().lower()
                                        print(disease)
                                        sp.speak(disease)
                                        
                                        print("if you satisfy with this value then press Y, else press N")
                                        sp.speak("if you satisfy with this value then press Y, else press N")
                                        disease_satisfaction = input("Enter your value : ")
                                        if disease_satisfaction.lower() == "n":
                                            sp.speak("Enter New Value: ")
                                            new_input_disease = input("Enter New Value : ")
                                            patient_id = (new_input_disease)
                                            print(disease)
                                            sp.speak(disease)

                                    else:
                                        print("Choose Valid Option")
                                        sp.speak("Choose Valid Option")
                                    

                                    # print("Prediction Breast Cancer?")
                                    # sp.speak("Prediction Breast Cancer?")
                                    # br_cancer = input("prediction breast cancer? (y/n): ")
                                    # f_pred = "NA"
                                    
                                    # if br_cancer == "y":
                                    #     f_pred = b_cancer.breast_cancer()
                                    #     print(f_pred)
                                    
                                    print("Prediction parkinson Disease")
                                    sp.speak('prediction parkinson Disease')
                                    p_cancer = input("prediction parkinson disease? (y/n): ")
                                    p_pred = "NA"

                                    
                                    if p_cancer == "y":
                                        # print("parkinson abcd")
                                        p_pred = park.parkinson()
                                        print(p_pred)
                                    
                                      
                                    
                                    p_details.insert_patient(patient_id, name, sex ,age , address, contact, mail, disease, p_pred)

                                    
                                    print("""
                                            ====================================
                                            !!!!!!!Registered Successfully!!!!!!
                                            ====================================
                                                            """)
                                    sp.speak("Patient Registered Sucessfully")

                                    sp.speak("press Any Key To Continue")
                                    os.system("pause")
                                    

                                   
                                    
                                    email.send_mail(patient_id, name, age, sex, address, contact, mail, disease, p_pred)
                                    sp.speak("Mail Sent Sucessfully")

                                else:
                                    print("please Choose Valid Option")
                                    sp.speak("Please Choose Valid Option")

                            # dischare process
                            elif x == 2:
                                
                                print("Please Enter The Patient Name")
                                sp.speak("Please Enter The Patient ID")
                                patient_id = input("Enter The Patient ID: ")
                                
                                
                                
                                    
                                row = p_details.show_patientdb(patient_id)
                                if len(row):
                                    for i in row:
                                        b1 = 0
                                        v1 = list(i)
                                        k1 = ["PATIENT ID","NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                                "MAIL", "DISEASE", "PARKINSON DISEASE PRIDICTION"]
                                        d1 = dict(zip(k1, v1))
                                        print(d1)
                                else:
                                    print("patient Dose not Exist")
                                    sp.speak("patient Dose not Exist")
                                    
                                    sp.speak("press any key to continue")
                                    os.system("pause")
                                    break
                                    
                                    
                                print("Has Patient Paid all the bills")
                                sp.speak("Has Patient Paid all the Bills?")
                                bill = input("Has he paid all the bills? (y/n):")
                                
                                if bill == "y":
                                    p_details.delete_patientdb(patient_id)
                                    print("Patient Discharged Sucessfully")
                                    sp.speak("Patient Discharged Sucessfully")
                                else:
                                    
                                    print("please clear your bill")
                                    sp.speak("Please Clear Your Bill")

                            else:
                                
                                print("Please Choose Valid Option")
                                sp.speak("Please Choose Valid Option")

                                sp.speak("Press Any Key To Continue")
                                os.system("pause")


                        # if user wants to see the details of PATIENT
                        elif a == 2:
                            
                          
                            sp.speak("please Enter patient ID")
                            patient_id = input("Enter The Patient ID: ")
                            
                            
                            row = p_details.show_patientdb(patient_id)
                            if len(row):
                                for i in row:
                                    b = 0
                                    v = list(i)
                                    k = ["PATIENT ID", "NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                        "MAIL", "DISEASE", "PARKINSON DISEASE PRIDICTION"]
                                    d = dict(zip(k, v))
                                    print(d)
                            else:
                                print("patient Dose not Exist in our database")
                                sp.speak("patient Dose not Exist in our database")
                                
                                os.system("pause")
                                sp.speak("press any key to continue")
                                

                        # if user wants to show all patient records
                        elif a == 3:
                          
                            row1 = p_details.show_all_patientdb()
                            for i in row1:
                                b = 0
                                v = list(i)
                                k = ["PATIENT ID","NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                     "MAIL", "DISEASE", "PARKINSON DISEASE PRIDICTION"]
                                d = dict(zip(k, v))
                                print(d)

                        # SIGN OUT
                        elif a == 4:
                            break

                        else:
                            print("Choose Valid Option")
                            sp.speak("Choose Valid Option")

                # IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
                else:
                    print("Staff Dosen't Exist in our database")
                    sp.speak("Staff Dosen't Exist in our database")
                    break

        elif r == 3:

            print("""
                  1. Staff's Data
                  """)
            sp.speak("press 1 for Staff's Data")

            i = int(input("Enter Your Choice: "))
            if i == 1:

              
                sp.speak("Please Enter Your Password")
                pwd = str(input("Enter Your Password: "))
                if pwd == Admin_passwd:
                    while(True):
                        print("""
                                        1. Show Staff's Data
                                        2. Delete staff's data
                                        
                                                        """)

                        sp.speak("""
                                        press 1 Show Staff's Data
                                        press 2 Delete staff's data
                                        
                                                        """)


                        x = int(input("Enter your Choice: "))
                        if x == 1:
                           
                            row1 = sd.show_all_staffdb()
                            for i in row1:
                                b = 0
                                v = list(i)
                                k = ["USERNAME", "PASSWORD"]
                                d = dict(zip(k, v))
                                print(d)
                            sp.speak("press any key to continue")
                            os.system("pause")
                            
                            
                                
                            break
                            
                        elif x == 2:

                            
                            sp.speak("Please Enter The Staff's Username")
                            un = input("Enter the Staff Username: ")

                            
                            sp.speak("Are you Sure")
                            sure = input("Are You Sure? (y/n):")

                            if sure == "y":
                                
                                sd.delete_stafftdb(un)
                                print("Successfully Staff deleted")
                                sp.speak("Staff Sucessfully Deleted")
                            else:
                                print("Staff Not Found")
                                sp.speak("Staff Not Found")

                            sp.speak("Press Any Key To continue")
                            os.system("pause")
                            break

                        else:
                            print("Please Choose Valid Option")
                            sp.speak("Please Choose valid Option")
                else:
                    print("Invalid Password")
                    sp.speak("Invalid Password")
                    break
            else:
                print("Please Choose Valid Option")
                sp.speak("Please Choose Valid Option")
        else:
            print("Please Choose Valid Option")
            sp.speak("Please Choose Valid Option")
