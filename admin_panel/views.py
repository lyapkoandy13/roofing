from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import redirect
from main.models import Good
from admin_panel.forms import GoodForm
import os

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        goods = Good.objects.all()
        return render(request, 'admin_panel/index.html', { 'goods' : goods })
    else:
        return render(request, 'admin_panel/login.html')

def check_user(request):
    if request.method == "POST":
        username = request.POST.get('user_login','')
        password = request.POST.get('user_password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return HttpResponse('yes', content_type='text/html')
        return HttpResponse('', content_type='text/html')
    else:
        return HttpResponse('', content_type='text/html')

def logout(request):
    auth.logout(request)
    return redirect('/admin/')

def add_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = GoodForm()
    return render(request, 'admin_panel/good.html', { 'form' : form })

def edit_good(request):

    if request.method == 'POST':
        good = Good.objects.filter(id=int(request.POST.get("some_id")))[0]
        good.name = request.POST.get("name")
        good.description = request.POST.get("description")
        good.price = float(request.POST.get("price"))
        good.image.delete()
        good.save()
        good.image = request.FILES.get("image")
        good.save()

        return redirect('/admin/')
    else:
        some_id = request.GET["some_id"]

        good = Good.objects.get(id=int(some_id))
        
        name = good.name
        description = good.description
        price = good.price
        image = good.image

        form = GoodForm()
    
    return render(request, 'admin_panel/good.html', { 'form' : form, 'some_id' : some_id, 'state' : 'edit', 'name' : name, 'price' : price, 'image' : image, 'description' : description })

def ajax_remove_good(request):
    Good.objects.filter(id=int(request.POST.get('id'))).delete()
    return HttpResponse('OK')

def ajax_move_up(request):
    try:
        good_higher = Good.objects.filter(id__lt=int(request.POST.get("id"))).order_by('-id')[0]
        good_current = Good.objects.filter(id=int(request.POST.get("id")))[0]
        
        name = good_current.name
        description = good_current.description
        price = good_current.price
        image = good_current.image
        
        good_current.name = good_higher.name
        good_current.description = good_higher.description
        good_current.price = good_higher.price
        good_current.image = good_higher.image
        good_current.save()
       
        good_higher.name = name
        good_higher.description = description
        good_higher.price = price
        good_higher.image = image
        good_higher.save()
    except Exception:
        pass

    return HttpResponse(good_higher.id)

def ajax_move_down(request):
    try:
        good_lower = Good.objects.filter(id__gt=int(request.POST.get("id"))).order_by('id')[0]
        good_current = Good.objects.filter(id=int(request.POST.get("id")))[0]
        
        name = good_current.name
        description = good_current.description
        price = good_current.price
        image = good_current.image
        
        good_current.name = good_lower.name
        good_current.description = good_lower.description
        good_current.price = good_lower.price
        good_current.image = good_lower.image
        good_current.save()
       
        good_lower.name = name
        good_lower.description = description
        good_lower.price = price
        good_lower.image = image
        good_lower.save()
    except Exception:
        pass

    return HttpResponse(good_lower.id)
