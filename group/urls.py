from django.urls import path
from .views import *
urlpatterns = [
    path('my_groups/', my_groups, name='mygroupspage' ),
    path('<slug:group_slug>/',my_groups,name="groupsslugpage"),
    path('<int:pk>/<slug:group_slug>/',group_detail,name='groupdetailpage'),
    path('new_groups/',new_groups,name='newgroupspage'),
]