from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from site_admin.models import *

# public
# Create your views here.
def signin(request):
    if request.method == 'POST':
            data_record = request.POST
            if Registration.objects.filter(mobilenumber=data_record['mobilenumber'],password=data_record['password']):
                user_details = Registration.objects.get(mobilenumber=data_record['mobilenumber'],password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['firstname'] = user_details.firstname
                    request.session['lastname'] = user_details.lastname
                    request.session['user_id'] = user_details.unique_id
                    request.session['mobilenumber'] = user_details.mobilenumber
                    request.session['usertype'] = 'user'
                    return redirect(reverse('public:dashboard'))
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect(reverse('film_user:signin'))
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect(reverse('public:signin'))
    return render(request,'public/signin.html')

def signup(request):
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect(reverse('public:signup'))
        elif Registration.objects.filter(mobilenumber=data_record['mobilenumber']):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect(reverse('public:signup'))
        else:
            registration = Registration(
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email_address'],
            mobile_number=data_record['mobilenumber'],
            address=data_record['address'],
            password=data_record['password'],
            status='active',
            )
            registration.save()
            messages.success(request, 'User registered successfully!')
            return redirect(reverse('public:signin'))
    return render(request,'public/signup.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    del request.session['mobilenumber']
    del request.session['usertype']
    return redirect(reverse('public:signin'))

def dashboard(request):
    return render(request,'public/dashboard.html')

def complaints_list(request):
    complaints_list = Complaints.objects.all()
    context = { 'complaints_list': complaints_list }
    return render(request, 'public/complaints-list.html', context)

def complaints_add(request):
    if request.method == 'POST':
        data_record = request.POST
        complaints = Complaints(
        complaints_subject=data_record['subject'],
        complaints_text=data_record['complaint'],
        selected_department=Departments.objects.filter(unique_id=data_record['department_list']).get(),
        public_user=Registration.objects.filter(unique_id=request.session['user_id']).get(),
        status='open',
        )
        complaints.save()
        messages.success(request, 'Complaint added!')
        return redirect(reverse('public:complaints_list'))
    department_list = Departments.objects.all()
    context = { 'department_list' : department_list }
    return render(request, 'public/complaints-add.html', context)

def complaints_delete(request, id):
    Complaints.objects.filter(unique_id=id).delete()
    messages.error(request, 'Complaints deleted successfully!')
    return redirect(reverse('public:complaints_list'))

def complaints_view(request, id):
    complaints = Complaints.objects.filter(unique_id=id).get()
    user_messages = Messages.objects.filter(complaints=Complaints.objects.filter(unique_id=id).get()).all()
    context = { 'complaints': complaints, 'user_messages': user_messages, 'complaint_id': id }
    return render(request, 'public/complaints-view.html', context)

def add_messages(request, id):
    if request.method == 'POST':
        data_record = request.POST
        mess_app = Messages(
        messages_text=data_record['message'],
        complaints=Complaints.objects.filter(unique_id=id).get(),
        department_user_id=0,
        public_user_id=request.session['user_id'],
        status=request.session['usertype'],
        )
        mess_app.save()
        messages.success(request, 'Added')
    return redirect(reverse('public:complaints_views', args=[id]))
