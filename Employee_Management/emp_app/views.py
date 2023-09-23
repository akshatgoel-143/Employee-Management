from django.shortcuts import render,HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role= int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary,bonus=bonus, phone=phone, dept_id=dept, role_id= role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")

    return render(request, 'add_emp.html')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            rem_emp = Employee.objects.get(id = emp_id)
            rem_emp.delete()
            return HttpResponse("Employee Removed")
        except:
            return HttpResponse("Invalid Employee")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    return render(request, 'filter_emp.html')