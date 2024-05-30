# from django.urls import path
# from . import views

# # app_name = 'groups'

# # urlpatterns = [
# #     path('', views.ListGroups.as_view(), name="all"),
# #     path("new/", views.CreateGroup.as_view(), name="create"),
# #     path("posts/in/<slug>/",views.SingleGroup.as_view(),name="single"),
# #     path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
# #     path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
# # ]
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),  # ListGroups
    path('new/', views.CreateGroup.as_view(), name='create'),  # CreateGroup
    path('<slug:slug>/', views.SingleGroup.as_view(), name='single'),  # SingleGroup
    path('<slug:slug>/join/', views.JoinGroup.as_view(), name='join'),  # JoinGroup
    path('<slug:slug>/leave/', views.LeaveGroup.as_view(), name='leave'),  # LeaveGroup
]
