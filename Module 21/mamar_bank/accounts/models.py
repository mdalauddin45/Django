from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACCOUNT_TYPE=(
    ('Saving','Savings'),
    ('Current','Current'),
)
GENDER_TYPE=(
    ('Male','Male'),
    ('Female','Female'),
)
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, decimal_places=2,max_digits=12)