from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import chatbot as bot


def index(request):
    return render(request, 'index.html')


def run_script(request):
    user_message = request.GET.get('userMessage', '')
    response = bot.output(user_message) 
    return JsonResponse({'response': response})