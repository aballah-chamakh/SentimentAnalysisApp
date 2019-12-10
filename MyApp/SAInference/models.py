from django.db import models
from django.contrib.auth.models import User

class SentimentAnalysisInference(models.Model):
  user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
  text = models.CharField(max_length=2000,blank=True,null=True)
  result = models.CharField(max_length=255,blank=True,null=True)
