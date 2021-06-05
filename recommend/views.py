from django.shortcuts import render

# Create your views here.

def recommendView(request):
    return render(request, 'recommend/Q&A(1).html')

def recommendResultView(request):
    price = request.GET.id('price')
    who = request.GET.id('who')
    size = request.GET.id('size')
    return render(request, 'recommend/service.html')
