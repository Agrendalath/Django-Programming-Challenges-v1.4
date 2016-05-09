from django.shortcuts import render


def index(request):
    """
    Just hello site.
    """
    return render(request, 'base.html')
