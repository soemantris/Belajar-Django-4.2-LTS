from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Blog',
    }
    return render(request, 'blog/index.html', context)

def detail_blog(request):
    context = {
        'title':'Detail Blog',
    }
    return render(request, 'blog/detail_blog.html', context)