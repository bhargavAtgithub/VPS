from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex = r'\d{10}')
# Create your models here.
class User(models.Model):
    aadhar = models.IntegerField(max_length= 12, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(validators=[phone_regex],max_length = 10)
    email = models.EmailField()

    def _str__(self):
        return self.aadhar

    def get_absolute_url(self):
        return reverse("PrimaryUser:PrimaryUser")

class FIR(models.Model):
    user = models.ForeignKey(User, on_delete  = models.CASCADE)
    description = models.CharField(max_length= 500)
    time_stamp = models.DateTimeField()
    state = models.CharField(max_length=30)
    district = models.CharField(max_length= 50)
    policeStation = models.CharField(max_length= 50)
    def save(self):
        self.time_stamp = timezone.now()
        return super(FIR, self).save()

    def get_absolute_url(self):
        return reverse("PrimaryUser: PrimaryUser")