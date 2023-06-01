from django.shortcuts import render
from django.http import HttpResponse

def first_page(request):
    text = 'Hello World'
    return HttpResponse(text)


def get_cards(request):
    return render(request,template_name='test.html')