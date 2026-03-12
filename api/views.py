
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import JobApplication
from .serializers import JobApplicationSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class JobApplicationListCreateView(ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class Meta:
        ordering = ['-created_at']



    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class JobApplicationUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class UserCreateView(CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

  

class JobApplicationListView(RetrieveAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)