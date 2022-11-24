from django.shortcuts import render


def view_home(request):
    """
    View Home Page
    """
    return render(request, 'index.html')
