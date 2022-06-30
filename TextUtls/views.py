from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    analyze=""
    punctuations=string.punctuation
    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyze=analyze+char

        Textutils={
            "purpose":"text analyze",
            "text_analyze":analyze
        }
        return render(request,'analyze.html',Textutils)
    else:
        return HttpResponse("Sorry you did not click on remove punctuation option")
