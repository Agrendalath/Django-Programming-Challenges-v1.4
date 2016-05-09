import random

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameGenerationForm
from .models import FirstName, LastName


def generate_name(sex, country):
    first_name = random.choice(FirstName.objects.filter(sex=sex, country=country))
    last_name = random.choice(LastName.objects.filter(country=country))

    return str(first_name.name + ' ' + last_name.get_correct_form(sex))


def index(request):
    """
    Just hello site.
    """
    if request.method == 'POST':
        form = NameGenerationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse(
                'NameGenerator:names',
                args=(request.POST['sex'], request.POST['country']))
            )

    else:
        form = NameGenerationForm()

    return render(request, 'NameGenerator/index.html', {'form': form})


def display(request, sex, country):
    """
    View random name.
    """
    try:
        name = generate_name(sex, country)
    except KeyError:
        return render(request, 'NameGenerator/index.html', {
            'error_message': 'Wrong choice.'
        })
    else:
        return render(request, 'NameGenerator/names.html', {'name': name})
