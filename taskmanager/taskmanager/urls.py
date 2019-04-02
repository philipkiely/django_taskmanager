from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('all/', views.all_tasks, name='all_tasks'),
    path('new/', views.new_task, name='new_task'),
    path('update/', views.update_task, name='update_task'),
    path('delete/', views.delete_task, name='delete_task'),
    path('signin/', views.signin, name='signin'),
]
