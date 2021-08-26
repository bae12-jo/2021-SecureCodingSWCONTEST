from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import *
from django.contrib.auth.hashers import make_password

# Create your views here.

def login(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
    else:
        form=CustomUserCreationForm()
    return render(request,'login.html',{'form':form})


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password =make_password(form.cleaned_data.get('password'))
            #if form.clean_password2:
            user = authenticate(username=username, password=password)  # 사용자 인증
            login(request)  # 로그인
            #return redirect('qna/list')
            return HttpResponseRedirect("groups/my_groups")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


