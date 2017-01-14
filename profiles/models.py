from django.db import models

class Profile(models.Model):
  handle = models.CharField(db_index=True, max_length=50, default='')
  picture_url = models.CharField(max_length=200, default='')
  name = models.TextField(default='')
  email = models.TextField(db_index=True, default='')
  bio = models.TextField(default='')
  city = models.TextField(default='')
  website_url = models.TextField(default='')
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

class Follow(models.Model):
  following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
  follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)