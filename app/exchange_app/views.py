from django.shortcuts import render
import requests

def exchange(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
    return render(request=request, template_name='exchange_app/index.html', context=context)
