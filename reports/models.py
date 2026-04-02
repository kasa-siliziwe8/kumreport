from django.db import models


class Report(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Assigned', 'Assigned to Field Team'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    ref_number = models.CharField(max_length=20, unique=True)
    street_address = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ref_number} – {self.issue_type} ({self.status})"
