from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'past_job')

admin.site.register(Job, JobAdmin)