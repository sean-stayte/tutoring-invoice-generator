# A program to generate tutoring invoices
from csv import writer
import pandas as pd
import os
import tkinter as tk
from tkinter import simpledialog

# Step 1: Enter info 
ROOT = tk.Tk()
ROOT.withdraw()

date = simpledialog.askstring(title="Invoice Generator",
                                  prompt="Date of Session:",
                                  initialvalue="dd/mm/yyyy")
student = simpledialog.askstring(title="Invoice Generator",
                                  prompt="Student Name:")
length = simpledialog.askstring(title="Invoice Generator",
                                  prompt="Session Length (hours):")
rate = simpledialog.askstring(title="Invoice Generator",
                                  prompt="Rate per hour (£):")
totaldue = round((float(length) * int(rate)), 2)
invoicenumber = (len(pd.read_csv('C:/fakepath/lesson_log.csv')) + 1)

# Step 2: Update lesson log 
lesson_details = [date, student, length, rate, totaldue, invoicenumber]
lesson_log = open(r'C:\fakepath\lesson_log.csv', 'a')
lesson_log_writer = writer(lesson_log)
lesson_log_writer.writerow(lesson_details)
lesson_log.close()
os.startfile('C:/fakepath/lesson_log.csv')

# Step 3: Generate invoice 
invoicepath = r'C:\fakepath\INV' + str(invoicenumber) + '.txt'
invoice = open(invoicepath, 'w')
invoice.write('INVOICE\n*******\nDate: ' + date + 
'\nInvoice Number: ' + str(invoicenumber) +
'\nStudent: ' + student + 
'\nSession Length (hours): ' + str(length) + 
'\nRate Per Hour: £' + str(rate) +
'\n*******\nTotal Due: £' + str(totaldue) +
'\n*******\nPlease make payment to:\nAccount Name: A N Other\nBank: FlatWest\nAccount Number: 12345678\n12-34-56\n*******\nThank You!')
os.startfile(invoicepath)