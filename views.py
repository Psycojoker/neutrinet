from feedparser import parse
from django.shortcuts import render
from django.http import HttpResponseBadRequest

def tweets(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    rss = parse('https://identi.ca/api/statuses/user_timeline/292360.rss')
    return render(request, 'tweets.html', {"tweets": rss.entries[:7]})
