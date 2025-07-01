from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Gig(models.Model):
    CATEGORY_CHOICES = [
        ('writing', 'Writing'),
        ('design', 'Design'),
        ('tech', 'Tech'),
        ('marketing', 'Marketing'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.PositiveIntegerField(help_text="Delivery time in days")
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gigs')

    def __str__(self):
        return self.title
    