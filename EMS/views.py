from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateEmployeeForm
from .models import Employee
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
    count_of_employees=len(Employee.objects.all())
    count_of_employees_on_leave=len(Employee.objects.all().filter(on_leave=True))
    return render(request,'home.html',{'count_of_employees':count_of_employees,'count_of_employees_on_leave':count_of_employees_on_leave})



def create_employee(request):
    form=CreateEmployeeForm()
    if request.method == 'POST':
        form=CreateEmployeeForm(request.POST)
        if form.is_valid():
            object=form.save(commit=False)
            if form.cleaned_data.get('on_leave'):
                object.leave_count=1
            else:
                object.leave_count=0
            object.save()
            return redirect('create_employee')
    return render(request,'create.html',{'form':form})



def all_employees(request):
    employees=Employee.objects.all()
    return render(request,'all_employees.html',{'employees':employees})


def employees_on_leave(request):
    employees=Employee.objects.all().filter(on_leave=True)
    return render(request,'employees_on_leave.html',{'employees':employees})


def update_employee(request,id):
    try:
        employee = Employee.objects.get(pk=id)
        is_on_leave=employee.on_leave
        leave_count=employee.leave_count
    except:
        return HttpResponse("Employee  Not Exist .")
    form = CreateEmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():  
        check_on_leave=form.cleaned_data.get("on_leave")
        object=form.save(commit=False)
        if is_on_leave==False and check_on_leave==True:
            object.leave_count=leave_count+1
        object.save()
        return redirect('all_employees')
    else:
        return render(request, 'update_employee.html', context={'form': form})

def get_employee(request,id):
    try:
        employee = Employee.objects.get(pk=id)
        return render(request, 'particulur_employee.html', {'employee': employee})
    except:
        return HttpResponse("Employee  not exist .")


def remove_employee(request,id):
    try:
        employee = Employee.objects.get(pk=id)
    except:
        return HttpResponse("Employee  not exist .")
    employee.delete()
    return redirect('all_employees')

