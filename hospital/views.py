from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import  Doctor

def homepage(request):
    return render(request, 'hospital/index.html')

def doctor_dashboard(request):
    return render(request, 'hospital/doctor_dashboard.html')



def create_account_page(request):
    error = ""

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        gender = request.POST["gender"]
        phonenumber = request.POST["phonenumber"]
        birthdate = request.POST["birthdate"]
        rank = request.POST["rank"]
        specialty = request.POST["specialty"]

        try:
            if password == confirm_password:
                # Create a new CustomUser object
                user = User.objects.create_user(
                    first_name=name,
                    email=email,
                    password=password,
                    username=username
                )

                # Create a new Doctor object
                doctor = Doctor.objects.create(
                    user=user,
                    name=name,
                    phonenumber=phonenumber,
                    birthdate=birthdate,
                    gender=gender,
                    rank=rank,
                    specialty=specialty
                )

                # Assign the user to the "Doctor" group
                doctor_group, _ = Group.objects.get_or_create(name="Doctor")
                doctor_group.user_set.add(user)

                error = 'no'
            else:
                error = "yes"
        except Exception as e:
            error = "yes"

    d = {
        'error': error
    }
    return render(request, 'hospital/create_account.html', d)


def login_page(request):
    return render(request, 'hospital/login.html')
