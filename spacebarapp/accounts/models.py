from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
from django.contrib.auth.models import User

class User(model.Model, auth.Model):

    def __str__(self):
        return "@{}".format(self.username)