from tkinter import *
import smtplib
import keys
en_keys = keys.encypt_keys


def encrypt(text,key):
    code=list(text)
    for i in range(len(code)):
        code[i]=en_keys[key][code[i]]
    return(''.join(code))


def action():
    s = smtplib.SMTP('smtp.gmail.com' , 587)
    s.starttls()
    s.login('aj56.virus@gmail.com','bmdztsphkbixzyii')
    #apppwd for gmail: bmdztsphkbixzyii
    key= key_type.get()
    to = to_type.get()
    subject= encrypt(subject_type.get(),key)
    body= encrypt(body_type.get(),key)
    s.sendmail('aj56.virus@gmail.com',to ,'Subject:' + subject + '\n\n' + body)

top = Tk()  
top.title('Send Mail')
top.geometry("400x300")  
  
To_label = Label(top, text = "Recipient Email:").place(x = 30,y = 50)  
Subject_label = Label(top, text = "Subject:").place(x = 30, y = 90)  
Body_label = Label(top, text = "Body:").place(x = 30, y = 130)   
Key_label = Label(top, text = "Key(1-6):").place(x = 30, y = 170) 


to_type = StringVar()
subject_type = StringVar()
body_type = StringVar()
key_type = IntVar()
    
to_entry = Entry(textvariable = to_type , width = "25") 
sub_entry = Entry(textvariable = subject_type, width = "25")  
body_entry = Entry(textvariable = body_type, width = "25")  
key_entry = Entry(textvariable = key_type, width = "25").place(x=160,y=170)


to_entry.place(x=160,y=50)
sub_entry.place(x=160,y=90)
body_entry.place(x=160,y=130)


sbmitbtn = Button(top, text = "Submit",background = "pink", foreground = "blue", command= action).place(x = 170, y = 210) 
  
top.mainloop()  
