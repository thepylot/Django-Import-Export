from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass