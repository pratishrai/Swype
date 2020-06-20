from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/employee/', views.employee, name='employee'),
    path('profile/employer/', views.employer, name='employer'),
]
