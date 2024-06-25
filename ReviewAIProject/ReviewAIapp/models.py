from django.db import models

# Create your models here.
class Reviewcont(models.Model):
    review_pers = models.CharField("review perspective",max_length=10)
    review_dir = models.CharField("review direction",max_length=100)

