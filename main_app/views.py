from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
class Clip:
    def __init__(self, streamer, game, description, date, url):
        self.streamer = streamer
        self.game = game
        self.description = description
        self.date = date
        self.url = url

clips = [
    Clip('streamer2', 'game2', 'description1','date2', 'url2'),
    Clip('streamer1', 'game1', 'description2','date1', 'url1'),
    Clip('streamer3', 'game3', 'description3','date3', 'url3'),
    Clip('streamer4', 'game4', 'description4','date4', 'url4'),
]

def home(request):
    return HttpResponse("hi")

def about(request):
    return render(request, 'about.html')

def clips_index(request):
    return render(request, 'clips/index.html', {'clips' : clips})