from django.shortcuts import render


def admin_home(request):
    return render(request, 'custom-admin/admin_home.html')
