from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student



def index(request):
    return render(request,'index.html')

def stud_list(request):
    stud = Student.objects.all()
    print(stud)
    return render(request, 'student.html', {'stud': stud})      

def add_student(request):
    return render(request,"new.html")    

def create_student(request):

    if request.method == "POST" or request.method == "GET":
        roll = request.POST.get("rn")
        name = request.POST.get("nm")
        age =  request.POST.get("ag")
 #Create new Student object
        stud = Student(roll=roll,name=name,age=age)
        stud.save() 
        return HttpResponse("New Student added successfully!") 
    else:
        return HttpResponse("Error. Something went wrong!")

def edit_student(request,id):
    stud = Student.objects.get(roll=id)
    return render(request, 'edit.html', {'stud': stud}) 

def update_student(request,id):
    if request.method == "POST" or request.method == "GET":
        roll = request.POST.get("rn")
        name = request.POST.get("nm")
        age =  request.POST.get("ag")
 #Update new Student object
        stud = Student.objects.get(roll = id)
        stud.roll = roll
        stud.name = name
        stud.age = age
        stud.save() 
        return HttpResponse("Student record modified successfully!") 
    else:
        return HttpResponse("Error. Something went wrong!")        


def delete_student(request,id):
    stud = Student.objects.get(roll=id)
    stud.delete()
    return HttpResponse("Student record deleted from the database!")





