# Import necessary libraries
from django.shortcuts import render

# Define the view function for the homepage
def homepage(request):
    return render(request, 'hospital/index.html')  # Render the index.html template


from django.shortcuts import render

def doctor_dashboard(request):
    return render(request, 'hospital/doctor_dashboard.html')


def create_account_page(request):
    return render(request, 'hospital/create_account.html')


def login_page(request):
    return render(request, 'hospital/login.html')



