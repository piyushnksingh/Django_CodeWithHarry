from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,"text_utils/index.html")

def remove_punc(request):
    print(request.GET.get("text","default"))
    return HttpResponse("remove_punc")

def capitalize_first(request):
    return HttpResponse("capitalize_first")

def new_line_remove(request):
    return HttpResponse("new_line_remove")

def space_remove(request):
    return HttpResponse("space_remove")

def char_count(request):
    return HttpResponse("char_count")
    