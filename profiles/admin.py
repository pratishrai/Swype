from django.contrib import admin

from profiles.models import Employee, Employer, Company, Tag

admin.register(Employee)
admin.register(Employer)
admin.register(Company)
admin.register(Tag)
