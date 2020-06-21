import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from profiles.models import Employee, Employer, Company, Tag
from profiles.utils import get_employee_dict, get_employer_dict

# Index Function
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def employee(request):
    if request.method == 'POST':
        name = request.POST["name"]
        photo = request.POST["photo"]
        bio = request.POST["bio"]
        github_url = request.POST["github_url"]
        linkedin_url = request.POST["linkedin_url"]

        new_employee = Employee(name=name, photo=photo,
                                bio=bio, github_url=github_url, linkedin_url=linkedin_url, user=request.user)
        new_employee.save()
        return redirect('employee')

    elif request.method == 'GET':
        if request.user.is_authenticated:
            if hasattr(request.user, 'employee_profile'):
                if hasattr(request.user.employee_profile, 'tags') and request.user.employee_profile.tags.all().exists():
                    qs = Employer.objects.filter(tags__in=request.user.employee_profile.tags.all())
                else:
                    qs = Employer.objects.all()
                cards = [get_employer_dict(employer) for employer in qs]
                return render(request, 'cards.html', {'cards': json.dumps(cards)})
            else:
                render(request, 'employee.html')
        else:
            return redirect('/accounts/register')

    else:
        return redirect('/')


def employer(request):
    if request.method == 'POST':
        name = request.POST["name"]
        photo = request.POST["photo"]
        company = request.POST["company"]
        company_name = request.POST["company_name"]
        company_photo = request.POST["company_photo"]
        company_bio = request.POST["company_bio"]
        company_website = request.POST["company_website"]
        company_linkdin = request.POST["company_linkedin"]
        company_creator = request.POST["company_creator"]

        new_employer = Employer(name=name, photo=photo,
                              company=company)
        new_company = Company(name=company_name, photo=company_photo, bio=company_bio, website_url=company_website, linkedin_url=company_linkdin, creator = company_creator)

        new_employer.save()
        new_company.save()
        return redirect('employer')
    elif request.method == 'GET':
        if hasattr(request.user, 'employer_profile'):
            if hasattr(request.user.employer_profile, 'tags') and request.user.employer_profile.tags.all().exists():
                qs = Employee.objects.filter(tags__in=request.user.employer_profile.tags.all())
            else:
                qs = Employee.objects.all()
            cards = [get_employee_dict(employee) for employee in qs]
            return render(request, 'cardsForEmployer.html', {'cards': json.dumps(cards)})
        else:
            return render(request, 'employer.html')
    else:
        return redirect('/')
