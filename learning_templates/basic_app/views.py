from django.shortcuts import render
from basic_app import views
# Create your views here.
def index(request):
    basic_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', basic_dict)

def base(request):
    return render(request, 'basic_app/base.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

def other(request):
    return render(request, 'basic_app/other.html')