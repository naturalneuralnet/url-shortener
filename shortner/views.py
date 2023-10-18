from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
# these seem to be like controllers


def index(request):
    return render(request, 'index.html')


def shorten(request):
    if request.method == 'POST':
        link = request.POST['link']
        # this shortens the unique id to 5 characters
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

# pk is the name of the string variable in the url, could have a better name


def go(request, pk):
    # search for the uuid and return the link with that id to the user
    url_details = Url.objects.get(uuid=pk)

    return redirect(url_details.link)
