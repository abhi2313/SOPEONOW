from django.contrib import admin

# Register your models here.
from .models import Employee,Department,Post

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Post)