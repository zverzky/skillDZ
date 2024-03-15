from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

@login_required
def admin_page(request):
    return render(request, 'admin_page.html')
