from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.core.paginator import Paginator
from common.models import User
# Create your views here.

#전체 groups
def my_groups(request,group_slug=None):

    username=None
    current_group=None

    #권한관리. 로그인이 된 유저만 groups 찾기 가능 (왜냐하면 안 그러면 user부터 에러 날테니까!)
    if request.user.is_authenticated:
        username=request.user.username
    user=User.objects.get(username=username)
    groups=user.groups.all() #유저가 속한 그룹의 object

    #페이지 관리
    paginator=Paginator(groups,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    #슬러그를 써서 my groups페이지에 group마다 요약 카드를 띄우고 싶었지만 실패!
    if group_slug:
        current_group=get_object_or_404(Group,slug=group_slug)
        groups=groups.filter(group=current_group)

    return render(request,'my_groups.html',{'page_obj':page_obj, 'current_group':current_group,'groups':groups})

#디테일 per group
'''
#함수로 된 detail 시도
def group_detail(request,group_name,group_slug=None):
    group=get_object_or_404(Group,group_name=group_name,slug=group_slug)
    return render(request,'group_detail.html',{'group':group})
'''
#generic view로 된 detail 시도
from django.views.generic import DetailView
class GroupDetailView(DetailView):
    model=Group
    template_name='group_detail.html'
    
#new group
from django.forms import modelformset_factory

def new_groups(request):
    #model form을 쓸 때는 인자가 blank일 수 없어서 쓰게 된 함수
    GroupForm=modelformset_factory(Group,fields=('group_name','deposit','fine','reward','rule'))
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GroupForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            obj=form.save(commit=False)
            obj.leader=request.user
            obj.save()
            # process the data in form.cleaned_data as required
                # redirect to a new URL:
            #자꾸 register 페이지로 가는데 왤까?
            return HttpResponseRedirect(reversed('new_groups/'),{'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroupForm()

    return render(request, 'new_groups.html',{'form':form})
''''
#각 개인당 속한 그룹별로 낼 벌금을 계산하는 함수

def pay_fine(request):
   #later
   #user와 group 오브젝트 가져오기
   user=User.objects.get(user=request.user)
   #current_group=request.group
   current_group=Group.objects.filter(entry__teammates__contains=user)
    #유저의 balance, paid_fine 배열을 새로구하기
   balance=user.balance-current_group.fine
   paid_fine=user.paid_fine
   
   if group_name in user.paid_fine:
       paid_fine[group_name]=user.paid_fine[group_name]+group.fine
   else:
       paid_fine[group_name]=group.fine

    #update user with user
   User.objects.get(username=username).update(balance=balance,paid_fine=paid_fine)
   return render(request,'group_detail.html')
'''


#**later**use Permission mixin decorator for only leader to access
#**later**possibly attempt to use django provided Manager model for leaders

def edit(request):
    #disable pay_fine button
    return HttpResponseRedirect('edit_group.html/')
