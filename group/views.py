from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.core.paginator import Paginator
# Create your views here.

#전체 groups
def my_groups(request,group_slug=None):
    current_group=None
    groups=Group.objects.all()
    paginator=Paginator(groups,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    if group_slug:
        current_group=get_object_or_404(Group,slug=group_slug)
        groups=groups.filter(group=current_group)

    return render(request,'my_groups.html',{'page_obj':page_obj, 'current_group':current_group,'groups':groups})

#디테일 per group
def group_detail(request,group_name,group_slug=None):
    group=get_object_or_404(Group,group_name=group_name,slug=group_slug)
    return render(request,'group_detail.html',{'group':group})

#new group
def new_groups(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
                # redirect to a new URL:
             return HttpResponseRedirect('my_groups/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroupForm()

    return render(request, 'new_groups.html', {'form': form})

def pay_fine(request,group_name,user_id):
   #later
    return render(request,'group_detail.html')


def edit(request):
    #disable pay_fine button
    return HttpResponseRedirect('edit_group.html/')
