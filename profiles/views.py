from django.shortcuts import render, redirect
from django.http import HttpResponse

from profiles.models import Employee, Employer, Company, Tag

# Index Function
def index(request):
    return render(request, 'index.html')


def employee(request):
    if request.method == 'POST':
        name = request.POST["name"]
        photo = request.POST["photo"]
        bio = request.POST["bio"]
        github_url = request.POST["github_url"]
        linkedin_url = request.POST["linkedin_url"]

        new_employer = Employer(name=name, photo=photo,
                                bio=bio, github_url=github_url, linkedin_url=linkedin_url)
        new_employer.save()
        return redirect('employee')
    else:
        return render(request, 'employee.html')


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
    else:
        return render(request, 'employer.html')
