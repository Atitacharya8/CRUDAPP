from django.shortcuts import render, redirect
from crudapp.forms import EmployeeForm
from .models import Employee


def base(req):
    return render(req,"crudapp/base.html",{})


def emp(req):
    if req.method == "POST":
        form = EmployeeForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(req, "crudapp/index.html", {"form": form})


def show(req):
    employees = Employee.objects.all()
    return render(req, "crudapp/show.html", {"employees": employees})


def edit(req, id):
    employee = Employee.objects.get(id=id)
    return render(req, "crudapp/edit.html", {"employee": employee})


def update(req, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(req.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(req, "crudapp/edit.html", {"employee": employee})


def delete(req, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
