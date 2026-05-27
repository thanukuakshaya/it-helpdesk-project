from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='In Progress'
    )

    def __str__(self):
        return self.title
