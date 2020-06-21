from django.contrib import admin

from profiles.models import Employee, Employer, Company, Tag

admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.site_header = "Swype Administration"
