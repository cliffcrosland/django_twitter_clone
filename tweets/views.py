from django.shortcuts import render
from profiles.models import Profile

from .models import FeedEntry, Tweet

# actions

def create(request):
  print("hi")

# helpers

def create_tweet(author, body):
  tweet = Tweet.objects.create(author=author, body=body)
  # send tweet to all @ handles in the tweet
  handles = parse_handles(body)
  profiles = Profile.objects.filter(handle__in=handles)
  for profile in profiles:
    try:
      FeedEntry.objects.create(profile=profile, tweet=tweet)
    except:
      pass
  # send tweet to followers, unless it is a direct @ message
  if not body.startswith('@'):
    for follow in author.followers.all():
      profile = follow.follower
      if profile.handle in handles:
        continue
      try:
        FeedEntry.objects.create(profile=profile, tweet=tweet)
      except:
        pass

def parse_handles(body):
  words = body.split(' ')
  handles = filter(lambda word: word.startswith('@'), words)
  return set(handle.split('@')[1] for handle in handles)

