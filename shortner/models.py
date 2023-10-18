from django.db import models

# Create your models here.
# creates two tables, link and uuid
# uuid is a generated id for each link


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
