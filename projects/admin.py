from django.contrib import admin

from .models import Skill, Job, Project, Technology

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Technology)
