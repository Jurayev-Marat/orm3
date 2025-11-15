from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def company(request):
    return render(request, 'company.html')

def design(request):
    return render(request, 'design.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search_results.html')

def subscribe(request):
    return render(request, 'subscribe_success.html')