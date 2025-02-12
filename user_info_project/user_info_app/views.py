# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect

from .forms import UserInfoForm
from django.http import HttpResponse
from .models import UserInfo
from django.views.decorators.csrf import csrf_exempt

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
    
    return render(request, 'index.html', {'form': form})

def home(request):
    return render(request=request, template_name='index.html')

def profile(request):
    return HttpResponse("User Profile Page")

def get_data(request):
    data = UserInfo.objects.all()  # Fetch all user records
    print("data: ", data)
    return render(request=request, template_name='data_list.html', context={'data': data})

def style(request):
    return render(request, 'style.css')

@csrf_exempt
def delete_users(request):
    if request.method == "POST":
        user_ids = request.POST.getlist("delete_ids")  # Get selected user IDs
        if user_ids:  # Ensure at least one checkbox is selected
            UserInfo.objects.filter(id__in=user_ids).delete()
    return redirect("get_data")  # Redirect back to data list page

def update_user(request, user_id):
    user = get_object_or_404(UserInfo, id=user_id)  # Fetch user by ID

    if request.method == "POST":
        form = UserInfoForm(request.POST, instance=user)  # Populate form with existing data
        if form.is_valid():
            form.save()
            return redirect("get_data")  # Redirect back to user list after updating
    else:
        form = UserInfoForm(instance=user)  # Pre-fill form with user data

    return render(request, "update_user.html", {"form": form, "user": user})
