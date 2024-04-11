# data_analyzer/models.py
from django.db import models
from django.contrib.auth.models import User

class FavoriteQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_name = models.CharField(max_length=100)
    query_params = models.TextField()

    def __str__(self):
        return self.query_name
