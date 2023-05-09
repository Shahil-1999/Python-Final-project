

from fpdf import FPDF
from email.message import EmailMessage
import ssl
import os
import smtplib


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 




# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
def send_mail(patient_id, name, age, sex, address, contact, mail, desease, p_pred):
#     
    # layout('P', 'U')
    # Unit ('mm','cm','in')
    # format ('A3','A4','A5', 'Letter','Legal',(100,150)) {A4(default) and (100,150)Cusomize height and width}


    class PDF(FPDF):
        def header(self):
            #logo
            self.image('C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/mail/code.jpg', 8, 8, 15)
            self.image('C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/mail/R.jpg', 187, 7, 15)
            #font
            self.add_font('Lucida Bright','',r'C:/Windows/Fonts/LCALLIG.TTF', uni=True) # uni = True does true type font subset embedding
            self.set_font('Lucida Bright','U',20)
            # RGB
            self.set_text_color(134,108,15)
            # Title
            self.cell(0,10,'Disease prediction System for',ln=True, align='C',)
            self.cell(0,10,'Breast Cancer and Parkinson ',ln=True, align='C',)
            self.cell(0,10,'Disease Using Voice Command',ln=True, align='C',)
            #line break
            self.ln(20)

    # Create Object
    pdf = PDF('P','mm')
    # Add a page
    pdf.add_page()

    #Specify Fonts ('times','courier' etc)
    # 'B'(bold), 'U' (underline), ' I'(Italics), ''(regular),'BU' (combination)
    # Font size
    pdf.set_font('courier', 'U', 16)
    
    pdf.add_font('Goudy Old Style','',r'C:/Windows/Fonts/GOUDOSB.TTF', uni=True) # uni = True does true type font subset embedding
    pdf.set_font('Goudy Old Style', '', 16)
    # pdf.set_text_color(0,0,0)
    # Add Text
    # w = 'width'
    # h = 'height'
    pdf.cell(0,10, f'Patient ID: {patient_id}', ln=1)
    pdf.cell(0,10, f'Name: {name}', ln=1)
    pdf.cell(0,10, f'Age: {age}', ln=1)
    pdf.cell(0,10, f'Gender: {sex}', ln=1)
    pdf.cell(0,10, f'Address: {address}', ln=1)
    pdf.cell(0,10, f'Contact: +91{contact}', ln=1)
    pdf.cell(0,10, f'Mail: {mail}', ln=1)
    pdf.cell(0,10, f'Disease: {desease}', ln=1)
    pdf.cell(0,10, f'Parkinson Disease Prediction: {p_pred}', ln=1)
    y_axis_initial = 255
    pdf.set_y(y_axis_initial)
    pdf.set_font('times', 'U', 16)
    pdf.cell(0,10,"Doctor's Sign with Date", ln = 1, align='R')
    a = "C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/Paitent_Details_PDF/"
    pdf.output(f"{a}{name}.pdf")


    email_sender = "shahil.official.college@gmail.com"
    pwd_sender = "fotammwjxavbeank" #os.environ.get("Email_Password")   
    receiver = mail
    # msg = MIMEMultipart()

    subject = f'{name} Health Report'

    body = ''
    em = EmailMessage()
    em['From'] = email_sender

    em['To'] = receiver
    em['Subject'] = subject

    em.set_content(body)
    context = ssl.create_default_context()


    files = f"C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/Paitent_Details_PDF/{name}.pdf"
    with open (files, 'rb') as m:
        file_data = m.read()
        file_name = name + ".pdf"
    em.add_attachment(file_data, maintype='pdf', subtype = 'octet-stream', filename = file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, pwd_sender)
        smtp.sendmail(
            email_sender, receiver, em.as_string())











