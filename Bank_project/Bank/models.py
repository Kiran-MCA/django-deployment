from django.db import models

class Bank(models.Model):


    def __str__(self):
        return self.bank_name + ' - ' + self.city + ' -' + self.bank_ifsc

    bank_name = models.CharField(max_length=100)
    bank_ifsc = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

