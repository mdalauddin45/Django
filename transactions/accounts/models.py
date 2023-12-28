from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE

# Create your models here.
#django amder user make korar facility dei
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices =GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    
    def __str__(self) :
        return f"Account No: {self.account_no}, Balance: {self.balance}"
    
    def money_transfer(self, recipient, amount):
        if recipient:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                # self.transaction_history += f"Transferred ${amount} to {recipient.user.username}.\n"
                # recipient.transaction_history += f"Received ${amount} from {self.user.username}.\n"
                self.save()
                recipient.save()
                print(f"${amount} transferred to {recipient.user.username} successfully.")
            else:
                print("You don't have enough balance for this transfer.")
        else:
            print("Recipient account does not exist.")

class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name="address",on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)



            