from django.shortcuts import render, redirect
from django.http import HttpResponse
def index_page(request):
    return render(request, 'index.html')