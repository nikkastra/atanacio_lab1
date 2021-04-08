from django.contrib import admin

from .models import *


class NameAdmin(admin.ModelAdmin):
	model = Name


class TasksAdmin(admin.ModelAdmin):
	model = Tasks


admin.site.register(Name, NameAdmin)
admin.site.register(Tasks, TasksAdmin)