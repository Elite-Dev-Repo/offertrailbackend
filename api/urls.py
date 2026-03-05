from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='user-create'),
    path('myjobs/', views.JobApplicationListCreateView.as_view(), name='job-application-list-create'),
    path('myjobs/<int:pk>/', views.JobApplicationUpdateDeleteView.as_view(), name = 'job-application-update-delete'),
    path('job/<int:pk>/', views.JobApplicationListView.as_view(), name='job-application-list'),
]