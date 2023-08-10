from django.urls import path
from . import views

app_name='site_admin'
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-location', views.add_location, name="add_location"),
    path('delete-location/<int:id>', views.delete_location, name="delete_location"),
    path('add-department', views.add_department, name="add_department"),
    path('delete-department/<int:id>', views.delete_department, name="delete_department"),
    path('list-public-user', views.list_public_user, name="list_public_user"),
    path('list-dep-user', views.list_dep_user, name="list_dep_user"),
    path('list-complaints', views.list_complaints, name="list_complaints"),    
]
