from django.shortcuts import render

# Create your views here.

def index(request):
    about = 'Django site on Heroku'
    return render(response, 'index.html', {'about':about} )
