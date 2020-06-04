#write
import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path
import os

def output(filename,sheet,num,name,present):
    my_file=Path('C:\\Python27\\working face recg\\attendance\\'+str(datetime.now().date())+'.xls')
    print(my_file)
    if my_file.is_file():
        rb=open_workbook('C:\\Python27\\working face recg\\attendance\\'+str(datetime.now().date())+'.xls')
        book=copy(rb);#make writeable  copy of opened excel file
        sh=book.get_sheet(0)
    else:
        book=xlwt.Workbook()
        sh=book.add_sheet(sheet)
    style0=xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
    style1=xlwt.easyxf(num_format_str='D-MMM-YY')

    sh.write(0,0,datetime.now().date(),style1);
    col1_name='Name'
    col2_name='Attendance'

    sh.write(1,0,col1_name,style0);
    sh.write(1,1,col2_name,style0);
    nm=str(name)
    sh.write(num+2,0,name);
    sh.write(num+2,1,'Present');
    fullname=str(datetime.now().date())+'.xls';
    book.save('C:\\Python27\\working face recg\\attendance\\'+str(datetime.now().date())+'.xls')
    return fullname;
