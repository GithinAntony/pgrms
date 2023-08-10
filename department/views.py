from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from site_admin.models import *
from public.models import Registration as User_Registration, Complaints as User_Complaints, Messages as User_Messages

# department
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
                    request.session['dep_id'] = user_details.working_department_id
                    request.session['mobilenumber'] = user_details.mobilenumber
                    request.session['usertype'] = 'department_user'
                    return redirect(reverse('department:dashboard'))
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect(reverse('department:signin'))
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect(reverse('department:signin'))
    return render(request,'department/signin.html')

def signup(request):
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect(reverse('department:signup'))
        elif Registration.objects.filter(mobilenumber=data_record['mobilenumber']):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect(reverse('department:signup'))
        else:
            registration = Registration(
            firstname=data_record['firstname'],
            lastname=data_record['lastname'],
            email=data_record['email_address'],
            mobilenumber=data_record['mobilenumber'],
            address=data_record['address'],
            password=data_record['password'],
            working_department=Departments.objects.filter(unique_id=data_record['department_list']).get(),
            status='active',
            )
            registration.save()
            messages.success(request, 'Department user registered successfully!')
            return redirect(reverse('department:signin'))
    department_list = Departments.objects.all()
    context = { 'department_list' : department_list }
    return render(request,'department/signup.html', context)

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    del request.session['mobilenumber']
    del request.session['usertype']
    del request.session['dep_id']
    return redirect(reverse('department:signin'))

def dashboard(request):
    return render(request,'department/dashboard.html')

def complaints_list(request):
    complaints_list = User_Complaints.objects.filter(selected_department=Departments.objects.filter(unique_id=request.session['dep_id']).get()).all()
    context = { 'complaints_list': complaints_list }
    return render(request, 'department/complaints-list.html', context)

def complaints_view(request, id):
    complaints = User_Complaints.objects.filter(unique_id=id).get()
    if request.method == 'POST':
        data_record = request.POST
        complaints.reply = data_record['reply']
        complaints.status = data_record['change_status']
        complaints.save()
        messages.success(request, 'Replied successfully!')
        return redirect(reverse('department:complaints_views', args=[id]))
    user_messages = User_Messages.objects.filter(complaints=User_Complaints.objects.filter(unique_id=id).get()).all()
    context = { 'complaints': complaints, 'user_messages': user_messages, 'complaint_id': id }
    return render(request, 'department/complaints-view.html', context)

def add_messages(request, id):
    if request.method == 'POST':
        data_record = request.POST
        mess_app= User_Messages(
        messages_text=data_record['message'],
        complaints=User_Complaints.objects.filter(unique_id=id).get(),
        department_user_id=request.session['user_id'],
        public_user_id=0,
        status=request.session['usertype'],
        )
        mess_app.save()
        messages.success(request, 'Added')
    return redirect(reverse('department:complaints_views', args=[id]))
