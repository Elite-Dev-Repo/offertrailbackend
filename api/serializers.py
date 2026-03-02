from rest_framework import serializers
from .models import JobApplication
from django.contrib.auth.models import User




class JobApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = JobApplication
        fields = 'id', 'user', 'company_name', 'role', 'application_date', 'status', 'notes', 'created_at',
        extra_kwargs = {'user': {'read_only': True}}



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email', 'password'
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user