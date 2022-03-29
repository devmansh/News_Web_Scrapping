from django.shortcuts import render
import requests


API_KEY = 'your api key here'
# Create your views here.

def home(request):
    country = request.GET.get('country')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    
        
    context = {
        'articles' : articles   
    }
    
    return render(request, 'home.html', context)