from django.contrib.auth import get_user_model
from django.db import models

from profiles.utils import photo_path


class Employee(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    bio = models.TextField()
    github_url = models.CharField(max_length=300, blank=True)
    linkedin_url = models.CharField(max_length=1000, blank=True)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    interested_employers = models.ManyToManyField("profiles.Employer", related_name="interested_in")


class Company(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    bio = models.TextField()
    website_url = models.CharField(max_length=1000, blank=True)
    linkedin_url = models.CharField(max_length=1000, blank=True)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="companies",
    )


class Employer(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="employer_profile",
    )
    interested_employees = models.ManyToManyField(Employee, related_name="interested_in")


class Tag(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, related_name="tags")
    employers = models.ManyToManyField(Employer, related_name="tags")
