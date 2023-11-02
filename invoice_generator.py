# A program to generate tutoring invoices
from csv import writer
import pandas as pd

# Step 1: Enter info (next step, tkinter dialog box)
date = input('What date did the lesson take place? (dd/mm/yyyy): ')
student = input('What was the student\'s name? ')
length = float(input('How long was the session in hours? '))
rate = 30 # May add option to vary this later
totaldue = length * rate
invoicenumber = (len(pd.read_csv('C:/fakepath/lesson_log_test.csv')) + 1)

# Step 2: Update lesson log 
lesson_details = [date, student, length, rate, totaldue, invoicenumber]
lesson_log = open(r'C:\fakepath\lesson_log_test.csv', 'a')
lesson_log_writer = writer(lesson_log)
lesson_log_writer.writerow(lesson_details)
lesson_log.close()

# Step 3: Generate invoice 
invoicepath = r'C:\fakepath\INV' + str(invoicenumber) + '.txt'
invoice = open(invoicepath, 'w')
invoice.write('INVOICE\n*******\nDate: ' + date + 
'\nInvoice Number: ' + str(invoicenumber) +
'\nStudent: ' + student + 
'\nSession Length (hours): ' + str(length) + 
'\nRate Per Hour: £' + str(rate) +
'\n*******\nTotal Due: £' + str(totaldue) +
'\n*******\nPlease make payment to:\nAccount Name: A N Other\nBank: Floyds\nAccount Number: 12345678\nSort Code: 12-34-56\n*******\nThank You!')