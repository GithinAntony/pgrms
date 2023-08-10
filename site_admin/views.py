from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from public.models import Registration as User_Registration, Complaints as User_Complaints
from department.models import Registration as Dep_Registration
# Create your views here.
def login(request):
    if request.method == 'POST':
        data_record = request.POST
        if data_record['email'] == 'admin@admin.com' and data_record['password']  == 'admin':
            request.session['is_logged_in'] = True
            request.session['email'] = 'admin@admin.com'
            request.session['full_name'] = 'admin'
            request.session['usertype'] = 'admin'
            messages.success(request, 'Logged in as admin!')
            return redirect(reverse('site_admin:dashboard'))
        else:
            messages.error(request, 'Wrong credentials. Try again!')
            return redirect(reverse('site_admin:login'))
    return render(request,'site_admin/signin.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['email']
    del request.session['usertype']
    return redirect(reverse('index:home'))

def dashboard(request):
    return render(request,'site_admin/dashboard.html')

def add_location(request):
    if request.method == 'POST':
        data_record = request.POST
        location = Location(
        location = data_record['location']
        )
        location.save()
        messages.success(request, 'Location added successfully!')
        return redirect(reverse('site_admin:add_location'))
    location_list = Location.objects.all()
    context = { 'location_list' : location_list }
    return render(request,'site_admin/add-location.html', context)

def delete_location(request, id):
    Location.objects.filter(unique_id=id).delete()
    messages.error(request, 'Location deleted successfully!')
    return redirect(reverse('site_admin:add_location'))

def add_department(request):
    if request.method == 'POST':
        data_record = request.POST
        check_department_exists = Departments.objects.filter(location=Location.objects.get(unique_id=data_record['select_location']),department_name=data_record['department_name']).all()
        if check_department_exists:
            messages.error(request, 'Department already exists. Try another!')
        else:
            departments = Departments(
            location = Location.objects.get(unique_id=data_record['select_location']),
            department_name = data_record['department_name'],
            )
            departments.save()
            messages.success(request, 'Department added successfully!')
        return redirect(reverse('site_admin:add_department'))
    location_list = Location.objects.all()
    department_list = Departments.objects.all()
    context = { 'location_list': location_list, 'department_list': department_list }
    return render(request,'site_admin/add-department.html', context)

def delete_department(request, id):
    Departments.objects.filter(unique_id=id).delete()
    messages.error(request, 'Department deleted successfully!')
    return redirect(reverse('site_admin:add_department'))

def list_public_user(request):
    datalist = User_Registration.objects.all()
    context = { 'datalist': datalist }
    return render(request,'site_admin/list-public-user.html', context)

def list_dep_user(request):
    datalist = Dep_Registration.objects.all()
    context = { 'datalist': datalist }
    return render(request,'site_admin/list-dep-user.html', context)

def list_complaints(request):
    datalist = User_Complaints.objects.all()
    context = { 'datalist': datalist }
    return render(request,'site_admin/list-complaints.html', context)
