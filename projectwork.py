# import tkinter as tk

# class DogGroomingApp:
#     def __init__(self, root):
#         self.root = root

#         # Create the main frame
#         self.frame = tk.Frame(root)
#         self.frame.pack()

#         # Create the labels
#         self.label_name = tk.Label(self.frame, text="Dog's Name:")
#         self.label_name.pack()

#         self.label_breed = tk.Label(self.frame, text="Breed:")
#         self.label_breed.pack()

#         self.label_age = tk.Label(self.frame, text="Age:")
#         self.label_age.pack()

#         self.label_weight = tk.Label(self.frame, text="Weight:")
#         self.label_weight.pack()

#         # Create the entries
#         self.entry_name = tk.Entry(self.frame)
#         self.entry_name.pack()

#         self.entry_breed = tk.Entry(self.frame)
#         self.entry_breed.pack()

#         self.entry_age = tk.Entry(self.frame)
#         self.entry_age.pack()

#         self.entry_weight = tk.Entry(self.frame)
#         self.entry_weight.pack()

#         # Create the buttons
#         self.button_submit = tk.Button(self.frame, text="Submit", command=self.submit)
#         self.button_submit.pack()

#         self.button_cancel = tk.Button(self.frame, text="Cancel", command=self.root.destroy)
#         self.button_cancel.pack()

#     def submit(self):
#         # Get the values from the entries
#         name = self.entry_name.get()
#         breed = self.entry_breed.get()
#         age = self.entry_age.get()
#         weight = self.entry_weight.get()

#         # Print the values
#         print("Dog's name:", name)
#         print("Breed:", breed)
#         print("Age:", age)
#         print("Weight:", weight)

#     def main():
#         root = tk.Tk()
#         app = DogGroomingApp(root)
#         root.mainloop()

# if __name__ == "__main__":
#     dogs=()





# import tkinter as tk

# # Create the main application window
# app = tk.Tk()
# app.title("alphawings pet solution ")

# def getvals():
#     print('its work')

# # Create a label
# label = tk.Label(app, text="Welcome to the Dog Grooming App",font='comicsansms 13 bold',pady=13).grid(row=0,column=3))
# label.pack()

# # Create a button to open a grooming form
# # def open_grooming_form():
# #     grooming_form = tk.Toplevel(app)
# #     grooming_form.title("Grooming Form")
    
#     # Add grooming form elements here

#     name=Label(root,text="Dog Name")
#     phone=Label(root,text="phone")
#     gender=Label(root,text="gender")
#     emergency=Label(root,text="emergency alert")
#     payementmode=Label(root,text="payment mode")

#     name.grid(row=1,column=2)
#     phone.grid(row=2,column=2)
#     gender.grid(row=3,column=2)
#     emergency.grid(row=4,column=2)
#     payementmode.grid(row=5,column=2)

#     namevalue=StringVar()
#     phonevalue=StringVar()
#     gendervalue=StringVar()
#     emergencyvalue=StringVar()
#     payementmodevalue=StringVar()
#     foodservicesvalue=IntVar()

    
#     # Close grooming form button
#     close_button = tk.Button(grooming_form, text="Close", command=grooming_form.destroy)
#     close_button.pack()

# grooming_button = tk.Button(app, text="Open Grooming Form", command=open_grooming_form)
# grooming_button.pack()

# # Start the tkinter main loop
# app.mainloop()







from tkinter import*

import pymysql

root=Tk()


root.title("Dog management app")
root.configure(background='light blue')

# def connectionss():
#            con = pymysql.connect(host="localhost", user="root", password="root")
#            cursor = con.cursor()
#            cursor.execute('create database if not exists Grooming')  
# connectionss()
# def connectionsstable():
#            con = pymysql.connect(host="localhost", user="root", password="root",db='Grooming')
#            cursor = con.cursor()
#            cursor.execute('create table if not exists Person(id int(5),name varchar(20),phone int(5))')  
# connectionsstable()

# def get():
#     print("its works")

# root.geometry("644x344")

# heading
Label(root,text='welcome to alphwaing pet solution app',font='comicsansms 13 bold',pady=13).grid(row=0,column=3)

# text for our form
name=Label(root,text="Dog Name")
phone=Label(root,text="Phone")
schedule=Label(root,text="Date And Timing")
gender=Label(root,text="Gender")
payementmode=Label(root,text="Payment Mode")

# pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
schedule.grid(row=3,column=2)
gender.grid(row=4,column=2)
payementmode.grid(row=5,column=2)

# tkinter variable for storing form
namevalue=StringVar()
phonevalue=StringVar()
schedulevalue=StringVar()
gendervalue=StringVar()
payementmodevalue=StringVar()
prebookservicesvalue=IntVar()

# entries for our form
nameentry= Entry(root,textvariable=namevalue)
phoneentry= Entry(root,textvariable=phonevalue)
scheduleentry= Entry(root,textvariable=schedulevalue)
genderentry= Entry(root,textvariable=gendervalue)
payementmodeentry= Entry(root,textvariable=payementmode)

# packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
scheduleentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
payementmodeentry.grid(row=5,column=3)

# checkbutton
prebookservice= Checkbutton(text="want to prebook your schedule?",variable=prebookservicesvalue)
prebookservice.grid(row=6,column=3)

#button and packing it and assigning it a command
Button(text="submit to aphawings pet solution",command='get').grid(row=7,column=3)


import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime

class Task:
    def __init__(self, name, package, due_date):
        self.name = name
        self.package = package
        self.due_date = due_date


class dogManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Groom Management")

        self.tasks = []

        self.owner_name_var = tk.StringVar()
        self.package_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Task Name Label and Entry
        tk.Label(self.root, text="Owner Name:").grid(row=0, column=0, sticky="w")
        owner_name_entry = tk.Entry(self.root, textvariable=self.owner_name_var)
        owner_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Packages Label and Dropdown
        tk.Label(self.root, text="Package:").grid(row=1, column=0, sticky="w")
        package_values = ["1 Week", "2 Week", "3 Week","4 Week"]
        package_dropdown = ttk.Combobox(self.root, textvariable=self.package_var, values=package_values)
        package_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Due Date Label and Calendar
        tk.Label(self.root, text="Due Date:").grid(row=2, column=0, sticky="w")
        due_date_entry = DateEntry(self.root, textvariable=self.due_date_var, date_pattern="yyyy-mm-dd")
        due_date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add Task Button
        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Task List Treeview
        self.task_list_treeview = ttk.Treeview(self.root, columns=("Package", "Due Date"))
        self.task_list_treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.task_list_treeview.heading("#0", text="Owner Name")
        self.task_list_treeview.heading("Package", text="Package")
        self.task_list_treeview.heading("Due Date", text="Due Date")

        # Delete Task Button
        delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_task_button.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Clear Task Button
        clear_task_button = tk.Button(self.root, text="Clear Task", command=self.clear_task)
        clear_task_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")

    def add_task(self):
        name = self.owner_name_var.get()
        package = self.package_var.get()
        due_date = self.due_date_var.get()

        if name and package and due_date:
            owner = Task(name, package, due_date)
            self.tasks.append(owner)

            self.task_list_treeview.insert("", tk.END, text=owner.name, values=(owner.package, owner.due_date))

            self.owner_name_var.set("")
            self.package_var.set("")
            self.due_date_var.set("")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def delete_task(self):
        selected_item = self.task_list_treeview.selection()
        if selected_item:
            owner_name = self.task_list_treeview.item(selected_item)["text"]
            for owner in self.tasks:
                if owner_name == owner_name:
                    self.tasks.remove(owner)
                    self.task_list_treeview.delete(selected_item)
                    break

    def clear_task(self):
        self.owner_name_var.set("")
        self.package_var.set("")
        self.due_date_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = dogManagementApp(root)
    # root.mainloop()

root.mainloop()









