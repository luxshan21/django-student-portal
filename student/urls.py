from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('insert_student/', views.insert_student, name='insert_student'),
    path('view-students/', views.view_students, name='view_students'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('update-student/<int:id>/', views.update_student, name='update_student'),
]