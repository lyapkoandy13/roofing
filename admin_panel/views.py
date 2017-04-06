from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import redirect
from main.models import Good
from main.models import Image
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
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = float(request.POST.get('price'))
        images = request.FILES.getlist('images')
        
        good = Good()
        good.name = name
        good.description = description
        good.price = price
        good.save()

        for image in images:
            imageModel = Image()
            imageModel.image = image
            imageModel.save()
            good.images.add(imageModel)

        return redirect('/admin/')
    else:
        pass
    return render(request, 'admin_panel/good.html')

def edit_good(request):

    if request.method == 'POST':
        good = Good.objects.filter(id=int(request.POST.get("good-id")))[0]
        good.name = request.POST.get("name")
        good.description = request.POST.get("description")
        good.price = float(request.POST.get("price"))
        good.save()

        if len(request.FILES) != 0:
            images = request.FILES.getlist('images')
            for image in images:
                imageModel = Image()
                imageModel.image = image
                imageModel.save()
                good.images.add(imageModel)

        return redirect('/admin/')
    else:
        good_id = request.GET.get('good-id')

        good = Good.objects.get(id=int(good_id))
        
        name = good.name
        description = good.description
        price = good.price
        images = good.images.all()

        # form = GoodForm()
    
    return render(request, 'admin_panel/good.html', { 'good_id' : good_id, 'state' : 'edit', 'name' : name, 'price' : price, 'images' : images, 'description' : description })

def ajax_remove_good(request):
    good = Good.objects.filter(id=int(request.POST.get('id')))
    for some_good in good:
        for image in some_good.images.all():
            image.delete()
    good.delete()
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

def ajax_delete_image(request):
    try:
        some_id = request.POST.get('some_id')
        Image.objects.filter(id=int(some_id)).delete()
    except:
        return HttpResponse('no')
    return HttpResponse('ok')

