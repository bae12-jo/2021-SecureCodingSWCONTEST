from django.urls import path
from .views import *
app_name="group"
urlpatterns = [
    path(r'my_groups/', my_groups, name='mygroupspage'),
    path(r'new_groups/',new_groups,name='newgroupspage'),
    path('<int:pk>',GroupDetailView.as_view(),name='groupdetail'),

]
