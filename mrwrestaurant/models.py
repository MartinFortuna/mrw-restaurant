from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class tbBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    guests = models.SmallIntegerField()
    status = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
