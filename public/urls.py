from django.urls import path
from . import views

app_name='public'
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('list-complaints', views.complaints_list, name="complaints_list"),
    path('add-complaints', views.complaints_add, name="complaints_add"),
    path('view-complaints/<int:id>', views.complaints_view, name="complaints_views"),
    path('delete-complaints/<int:id>', views.complaints_delete, name="complaints_delete"),
    path('add-messages/<int:id>', views.add_messages, name="add_messages"),     
]
