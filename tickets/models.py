from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
