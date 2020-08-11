from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/overview', views.overview, name='overview'),
    path('project/assign_for_me', views.assign_for_me, name='assign_for_me'),
    path('project/my_create', views.my_create, name='my_create'),
    path('project/bugs_all', views.bugs_all, name='bugs_all'),
    #path('project/project_member', views.project_member, name='project_member'),
    path('project/project_info', views.project_info, name='project_info'),
    path('project/add_bug', views.add_bug, name="add_bug"),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('personal_data/', views.personal_data, name='personal_data'),
    path('project/guidang/', views.guidang, name='guidang')
]