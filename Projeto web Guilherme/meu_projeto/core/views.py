from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def how_to_play(request):
    return render(request, 'core/howtoplay.html')

def settings_view(request):  # ✅ novo nome
    return render(request, 'core/settings.html')

def about(request):
    return render(request, 'core/about.html')

def play(request):
    return render(request, 'core/play.html')

def signup(request):
    return render (request, 'core/signup.html')
        