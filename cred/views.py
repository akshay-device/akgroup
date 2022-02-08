from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from newsapi import NewsApiClient


# Create your views here.

def home(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        print(e)


def login_user(request):
    try:
        if request.method == "POST":
            UserName = request.POST['username']
            UserPassword = request.POST['password']
            user = authenticate(username=UserName, password=UserPassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'User Successfully Login')
                return render(request, 'valid.html')
            else:
                messages.error(request, 'Invalid user credentials')
                return redirect('home')
        else:
            messages.error(request, '404 not found')

    except Exception as e:
        print(e)


def logout_user(request):
    try:
        logout(request)
        messages.info(request, 'User Successfully Logout')
        return redirect('home')
    except Exception as e:
        print(e)


def reg_user(request):
    try:
        if request.method == "POST":
            UserName = request.POST['reguser']
            UserPassword1 = request.POST['regpwd']
            # UserPassword2 = request.POST['password2']
            myuser = User.objects.create_user(username=UserName, password=UserPassword1)
            myuser.save()
            messages.success(request, 'User Successfully Register')
            return redirect('home')
        else:
            return redirect('home')
    except Exception as e:
        print(e)

def search(request):
    try:
        if request.method == "GET" and request.user.is_authenticated :
                keyword = request.GET['keyword']

                newsapi = NewsApiClient(api_key='c6139e6def1440fa817bb2b21646902f')
                top = newsapi.get_everything(q=keyword,sources='bbc-news')
                l = top['articles']
                desc = []
                news = []
                img = []
                for i in range(len(l)):
                    f = l[i]
                    news.append(f['title'])
                    desc.append(f['description'])
                    img.append(f['urlToImage'])
                mylist = zip(news, desc, img)
                return render(request, 'valid.html', context={"mylist": mylist})
        else:
            return redirect('home')

    except Exception as e:
        print(e)
