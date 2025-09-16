from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stud_list", views.stud_list, name="student"),
    path("add_student", views.add_student, name="add"),
    path("create_student", views.create_student, name="create"),
    path("edit_student/<id>", views.edit_student, name="edit"),
    path("update_student/<id>", views.update_student, name="update"),
    path("delete_student/<id>", views.delete_student, name="delete"),
]
 
