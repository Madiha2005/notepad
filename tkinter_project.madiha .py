Tkinter Projects
Tkinter is a standard GUI (Graphical User Interface) library in Python, offering tools to create interactive forms and windows for desktop applications. It simplifies form creation through widgets like buttons, input fields, and labels, aiding developers in building user-friendly interfaces.
Project: 1
Tkinter GUI
Code.
import tkinter as tk

root=tk.Tk()

root.geometry("800x500")
root.title("My first GUI")

label = tk.Label(root, text="Hello World!", font=('Arial',18))
label.pack(padx=20,pady=20)

textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click Me!", font=('Arial',18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1" , font=('Arial',18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2" , font=('Arial',18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3" , font=('Arial',18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4" , font=('Arial',18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5" , font=('Arial',18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6" , font=('Arial',18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, height=100,width=100)






root.mainloop()
xxxCode finishxxx
Project:2
Data Entery Form:
Code.
import tkinter
from tkinter import ttk

def enter_data():
    #user info
    firstname = first_name_entery.get()
    lastname = last_name_entery.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()

    print("First name:",firstname,"Last name:",lastname)
    print("Title:",title,"Age:",age,"Nationality:",nationality)
    print("# Courses:",numcourses, "# Semesters:",numsemesters)
    print("Registration Status:",Registrationstatus)
    print("---------------------------------------")



window = tkinter.Tk()
window.title("Data Entery Form")

frame = tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame =tkinter.LabelFrame(frame, text="User Infomation")
user_info_frame.grid(row=0,column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entery = tkinter.Entry(user_info_frame)
last_name_entery = tkinter.Entry(user_info_frame)
first_name_entery.grid(row=1,column=0)
last_name_entery.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Ms","Dr"])
title_label.grid(row=1, column= 2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18,to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3,column=0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa","Antarctica","Asia","Europe","North America","Oceania","South America"])
nationality_label.grid(row=3,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0, sticky="new",padx=20, pady=10)

registered_label = tkinter.Label(courses_frame,text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame,text="Currently Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame,text="#Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame,from_=0,to= "infinity" )
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame,text="#Completed Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame,from_=0,to= "infinity" )
numsemesters_label.grid(row=0, column=2 )
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept terms
#terms_frame = tkinter.Label(frame, text="Terms & Conditions")
#terms_frame.grid(row=0, column=0, sticky="new",padx=20, pady=10)

#terms_check = tkinter.Checkbutton(terms_frame,text="I accept the terms & conditions.")
#terms_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame,text= "Enter data",command= enter_data)
button.grid(row=3, column=0, sticky="new",padx=20, pady=10)



window.mainloop()
xxxCode finishxxxx

Regards 
Madiha Atta
Cohort 9
Python Development


 