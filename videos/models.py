from django.db import models

class Song(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=50)
    description=models.CharField(max_length=2000,null=True)
    path=models.CharField(max_length=200)
    

class review(models.Model):
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    description=models.CharField(max_length=300,null=False)

class Audio(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    path=models.CharField(max_length=50)
     