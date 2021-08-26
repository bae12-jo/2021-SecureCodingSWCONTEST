from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import NameForm,RegiForm
#DataFlair #Views #TemplateInheritance
# Create your views here.


def login(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            identifier=form.cleaned_data['identifier']
            secret=form.cleaned_data['secret']
            user=authenticate(username=identifier,password=secret)
            if user is not None:
            # redirect to a new URL:
                return HttpResponseRedirect('my_groups/')
        else:
            return HttpResponseRedirect('registration/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})

def registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
                # redirect to a new URL:
            return HttpResponseRedirect('my_groups/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegiForm()

    return render(request, 'registration.html', {'form': form}) 
