# urls.py
from django.urls import path
from .views import homepage
from django.urls import path
from .views import doctor_dashboard
from hospital.views import create_account_page, login_page



app_name='hospital'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('create-account/', create_account_page, name='create_account'),
    path('login/', login_page, name='login'),
]
