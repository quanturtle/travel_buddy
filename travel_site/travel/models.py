from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    planned_by = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()
    users_joining = models.ManyToManyField(User)