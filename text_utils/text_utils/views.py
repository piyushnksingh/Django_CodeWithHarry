from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def remove_punc(request):
    return HttpResponse("remove_punc")

def capitalize_first(request):
    return HttpResponse("capitalize_first")

def new_line_remove(request):
    return HttpResponse("new_line_remove")

def space_remove(request):
    return HttpResponse("space_remove")

def char_count(request):
    return HttpResponse("char_count")
    