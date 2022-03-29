from django.shortcuts import render
import requests


API_KEY = 'your api key here'
# Create your views here.

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    
        
    context = {
        'articles' : articles   
    }
    
    return render(request, 'home.html', context)