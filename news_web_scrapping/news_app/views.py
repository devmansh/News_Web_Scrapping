from django.shortcuts import render
import requests


API_KEY = 'f1e9a926ed2744c6892dc6bd49b69a89'
# Create your views here.

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
    context = {
        'articles' : articles   
    }
    
    return render(request, 'home.html', context)