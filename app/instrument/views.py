from django.shortcuts import render


# Create your views here.
def starting_page(request):
    """Docstring"""
    return render(request, 'instrument/index.html')


def instruments(request):
    """Docstring"""
    pass


def instrument_detail(request, instrument):
    """Docstring"""
    pass
