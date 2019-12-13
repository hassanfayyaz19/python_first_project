from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(response):
    dict_my={"insert_me":"Hello i'm in template"}
    return render(response, 'first_app/index.html', context=dict_my)