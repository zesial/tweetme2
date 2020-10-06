from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
import random

def home_view(request, *args, **kwargs):
    return  render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()
    return render(request, 'components/form.html',context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{'id':x.id, 'content': x.content, "likes":random.randint(0,129)} for x in qs] 
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)


def tweet_detail_view(request,tweet_id, *args, **kwargs):
    data = {"id": tweet_id}
    status = 200
    try:
        obj = Tweet.objects.get(pk = tweet_id)
        data['content'] = obj.content
    except:
        status = 404
        data['message'] = "Not found"

    return JsonResponse(data, status=status)

