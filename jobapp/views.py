from django.shortcuts import render


def render_jobapp_home(request):
    return render(request, 'jobapp/jobapp_home.html')
