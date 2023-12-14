from django.db import models
from django.contrib.auth.models import User
from card.models import Card

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Card, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    # Other fields or methods you might need
