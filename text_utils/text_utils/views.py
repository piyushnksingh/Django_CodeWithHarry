from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,"text_utils/index.html")

def analyze(request):
    djtext = request.GET.get("text","default")
    remove_punc = request.GET.get("remove_punc","off")
    if remove_punc=='on':
        Punctuation='''.,?!:;'"-–()[]{}.../\|*&@#%^_~`<>+=$€£¥'''
        analyzed_text=""
        for char in djtext:
            if char not in Punctuation:
                analyzed_text = analyzed_text + char
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "Remove Punctuation",
        })
    else:
        return HttpResponse("Error")