from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.db import models
import mysql.connector
from datetime import datetime

today = datetime.today()
con=mysql.connector.connect(host='localhost',username='root',password='password',database='nav')
mycur=con.cursor()

d={}
def index(request):
    return render(request,'login.html')
def login(request):
    if request.method == "POST":
        mob=request.POST['mo_num']
        password=request.POST['pass']
        if mob=="":
            messages.error(request, 'Please enter your Mobile Number')
            return redirect('/mail')
        elif password=="":
            messages.error(request, 'Please enter your password')
            return redirect('/mail')
        else:
            try:
                query=f'select * from User where mo_num={mob}'
                mycur.execute(query)
                result=mycur.fetchall()
                list1=result[0]               
                if password==list1[4]:
                    param={'name':list1[0],'email':list1[1],'gender':list1[2],'mob':list1[3],'comname':list1[5]}
                    d['monum']=list1[3]
                    return render(request,'loginpage.html',param)
                else:
                    messages.error(request, 'Incorrect password')
                    return redirect('/mail')
            except Exception as e:
                messages.error(request, 'Mobile Number not registered')
                return redirect('/mail')



        
def signup(request):
    return render(request,'create.html')
def store(request):
    name=request.POST['name']
    gender=request.POST['gender']
    email=request.POST['email']
    monum=request.POST['mob']
    password=request.POST['pass']
    com_name=request.POST['comname']
    if name=="":
        messages.error(request, 'Please enter your name')
        return redirect('/mail/signup')
    elif email=="":
        messages.error(request, 'Please enter your E-mail ID')
        return redirect('/mail/signup')
    elif monum=="" :
        messages.error(request, 'Please enter Valid Mobile Number')
        return redirect('/mail/signup')
    elif com_name=="" :
        messages.error(request, 'Please enter Valid Mobile Number')
        return redirect('/mail/signup')
    elif password=="":
        messages.error(request, 'Password should not be empty')
        return redirect('/mail/signup')
    else:
        query="insert into User (name,gender,email,mo_num,pas,company_name) values (%s,%s,%s,%s,%s,%s)"
        values=(name,gender,email,monum,password,com_name)
        mycur.execute(query,values)
        query3=f'create table n{monum} (nor varchar(30),top varchar(30),nos varchar(30),date varchar(30),time varchar(20),forwhom varchar(30),deliveryno varchar(30))'
        mycur.execute(query3)
        con.commit()
        messages.error(request, 'Registration Success')
        return redirect('/mail')
def entry(request):
    
    return render(request,'entry.html')
def storedata(request):
    a=d['monum']
    noa=request.GET.get('noa')
    top=request.GET.get('top')
    nos=request.GET.get('send')
    fw=request.GET.get('for')
    dn=request.GET.get('dn')
    date=today.strftime("%d/%m/%Y")
    time=today.strftime("%H:%M:%S")
    query=f"insert into n{a} (nor,top,nos,date,time,forwhom,deliveryno) values (%s,%s,%s,%s,%s,%s,%s)"
    values=(noa,top,nos,date,time,fw,dn)
    mycur.execute(query,values)
    con.commit()
    return render(request,'entry.html')
def back(request):
    a=d['monum']
    query=f'select * from User where mo_num={a}'
    mycur.execute(query)
    result=mycur.fetchall()
    list1=result[0]               
    param={'name':list1[0],'email':list1[1],'gender':list1[2],'mob':list1[3],'comname':list1[5]}
    d['monum']=list1[3]
    return render(request,'loginpage.html',param)
def check(request):
    return render(request,'check.html')
def date(request):
    date=today.strftime("%d/%m/%Y")
    time=today.strftime("%H:%M:%S")
    a=d['monum']
    query=f'select * from n{a} where date=%s'
    values=(date,)
    mycur.execute(query,values)
    result=mycur.fetchall()            
    param={'nor':result}
    d['monum']=a
    return render(request,'date_check.html',param)

    





