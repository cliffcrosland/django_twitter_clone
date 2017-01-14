from django.db import models

from profiles.models import Profile

class Tweet(models.Model):
  author = models.ForeignKey(Profile, related_name='tweets', on_delete=models.CASCADE)
  body = models.CharField(max_length=140, default='')
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

class FeedEntry(models.Model):
  profile = models.ForeignKey(Profile, related_name='feed_entries', on_delete=models.CASCADE)
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)