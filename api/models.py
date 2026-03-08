from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import models as auth_model





class JobApplication(models.Model):
    REJECTED = 'Rejected'
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'


    STATUS_CHOICES = [
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
    ]



    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    application_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.company_name} - {self.user.username}"

