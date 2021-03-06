#GROUPS URLS.PY
from django.urls import path
from . import views

app_name = 'groups' #REFERENTIERE PE VIITOR CU URL TEMPLATE TAGGING

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all'),
    path('new/',views.CreateGroupView.as_view(),name='create'),
    path('posts/in/<slug>/',views.SingleGroup.as_view(),name='single'),
    path('join/<slug>/',views.JoinGroup.as_view(),name='join'),
    path('leave/<slug>/',views.LeaveGroup.as_view(),name='leave'),
]
