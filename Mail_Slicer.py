# E-mail Slicer 
# 3:22 PM March 22, 2021
# Playing: Sa Susunod na Lang by Skusta Clee

# import xlwt
from xlwt import Workbook
import sys

wb = Workbook()
sheet1 = wb.add_sheet('Mail Slicer')

sheet1.write(0, 0, 'e-mail address')
sheet1.write(0, 1, 'First Name')
sheet1.write(0, 2, 'Last Name')
sheet1.write(0, 3, 'Host Mail')

def m_slice(mail_ct):
    for ctr in range(mail_ct):
        
        mail = input("Enter e-mail address: ")
        
        full_n = mail.split("@")
        host = full_n[1]    # host mail
        full_n = full_n[0]  # string 'full name'
       
        f_n = full_n.split(".")
        un = f_n[0]
        un1 = un.capitalize()   # First Name
        last = f_n[1]
        last1 = last.capitalize() # Last Name
            
        sheet1.write(ctr + 1, 0, mail)
        sheet1.write(ctr + 1, 1, un1)
        sheet1.write(ctr + 1, 2, last1)
        sheet1.write(ctr + 1, 3, host)
        
        wb.save('slice_3.xls') 
    return sys.exit()

mail_ct = int(input("How many e-mail addresses will you enter? "))
print(input(m_slice(mail_ct)))



