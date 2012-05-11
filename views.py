from feedparser import parse
from django.shortcuts import render

def tweets(request):
    rss = parse('https://identi.ca/api/statuses/user_timeline/292360.rss')
    return render(request, 'tweets.html', {"tweets": rss.entries[:7]})
