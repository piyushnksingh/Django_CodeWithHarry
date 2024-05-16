from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,"text_utils/index.html")

def analyze(request):
    djtext = request.GET.get("text","default")
    remove_punc = request.GET.get("remove_punc","off")
    uppercase = request.GET.get("uppercase","off")
    new_line_remover = request.GET.get("new_line_remover","off")
    capitalize_first = request.GET.get("capitalize_first","off")
    remove_extra_space = request.GET.get("remove_extra_space","off")
    char_count = request.GET.get("char_count","off")
    
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
        
    elif uppercase=='on':
        analyzed_text=""
        for char in djtext:
            analyzed_text = analyzed_text + char.upper()
            
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "UPPERCASE",
        })
        
    if new_line_remover=='on':
        analyzed_text=djtext.replace('\n', '')
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "New Line Remove",
        })

        
    if capitalize_first=='on':
        analyzed_text=djtext.title()
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "Capitalize First",
        })
        
    if remove_extra_space=='on':
        analyzed_text = ' '.join(djtext.split())
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "Remove Extra Space",
        })
        
    if char_count=='on':
        analyzed_text = len(djtext)
        return render(request,"text_utils/analyze.html",{
            "analyzed_text": analyzed_text,
            "purpose": "Char Count",
        })
        
    
        
    # else:
    #     return HttpResponse("Error")