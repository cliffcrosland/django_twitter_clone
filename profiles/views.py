from django.http import HttpResponse
from django.shortcuts import render

from .models import Profile

def index(request):
  return HttpResponse("Hello, Twitter!")

def detail(request, handle):
  try:
    profile = Profile.objects.get(handle=handle)
  except Profile.DoesNotExist:
    raise Http404("Profile does not exist")
  return render(request, 'profiles/detail.html', {'profile': profile})
