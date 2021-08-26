from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    """
    로그인
    """
    return render(request, 'common/login.html')


def signup(request):
    """
    계정생성
    """
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/qna/list')
        return render(request, 'signup.html')
    return render(request, 'common/signup.html')