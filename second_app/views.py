from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index1(response):
    return HttpResponse("<h1 style='font-size:15em'>Phir Kam Pay Gaya</h1><p style='font-size:100px'>&#128540;</p>")