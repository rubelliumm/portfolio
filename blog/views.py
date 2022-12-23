from django.shortcuts import render

# Create your views here.


def render_blog_homepage(request):
    return render(request, 'blog/homepage.html')
