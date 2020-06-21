from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.index, name='index'),
    path('profile/employee/', views.employee, name='employee'),
    path('profile/employer/', views.employer, name='employer'),
    path('profile/registerCompany/', views.registerCompany, name='registerCompany'),
]
