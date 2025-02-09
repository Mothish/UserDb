
# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserInfoForm
from django.http import HttpResponse
from .models import UserInfo


''''def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            return redirect('success')  # Redirect to a success page after form submission
        else:
            print("Form is invalid:", form.errors) 
    else:
        form = UserInfoForm()

    return render(request, 'user_info_form.html', {'form': form})'''

def user_info_view(request):
    print("View accessed!")  # Check if the view is hit
    if request.method == 'POST':
        print("Form submission detected!")
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")
            return redirect('/index')  # Redirect after saving
        else:
            print("Form validation failed:", form.errors)  # Print errors if form is invalid
    else:
        form = UserInfoForm()
        print("GET request detected, showing the form.")
    
    #return render(request, 'user_info_form.html', {'form': form})
    return render(request, 'index.html', {'form': form})
    
    

def home(request):
    return render(request=request,template_name='index.html')

def profile(request):
    return HttpResponse("User Profile Page")

def get_data(request):
    data = UserInfo.objects.all()  # Fetch all user records
    print("data: ",data)
    return render(request=request, template_name='data_list.html', context={'data': data})

def style(request):
    return render(request,'style.css')
# def data_list_view(request):
#     # Logic to display list
#     user = UserInfo.objects.all()
#     print(user)
#     return render(request, template_name='data_list.html',context={'data':user})