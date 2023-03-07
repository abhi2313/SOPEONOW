from django.urls import path
from .views import create_employee,update_employee,all_employees,get_employee,home,remove_employee,employees_on_leave
urlpatterns = [
    path('',home,name='home'),
    path('create_employee',create_employee,name='create_employee'),
    path('update_employee/<int:id>',update_employee,name='update_employee'),
    path('get_employee/<int:id>',get_employee,name='get_employee'),
    path('remove_employee/<int:id>',remove_employee,name='remove_employee'),
    path('all_employees',all_employees,name='all_employees'),
    path('employees_on_leave',employees_on_leave,name='employees_on_leave')
]
