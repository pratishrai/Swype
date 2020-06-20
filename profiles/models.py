from django.db import models

from profiles.utils import photo_path


class Employee(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    bio = models.TextField()
    github_url = models.CharField(max_length=300, blank=True)
    linkedin_url = models.CharField(max_length=1000, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    bio = models.TextField()
    website_url = models.CharField(max_length=1000, blank=True)
    linkedin_url = models.CharField(max_length=1000, blank=True)


class Employer(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=photo_path, blank=True)
    company = models.OneToOneField(Company)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, related_name="tags")
    employers = models.ManyToManyField(Employer, related_name="tags")
