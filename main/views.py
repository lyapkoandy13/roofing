from django.http import HttpResponse
from django.shortcuts import render
from main.models import Good
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def index(request):
	goods = Good.objects.all()
	return render(request, 'main/index.html', { 'goods' : goods } )

@csrf_exempt
def get_goods(request):
	goods = serializers.serialize('json', Good.objects.order_by("name")[:10])
	return HttpResponse(goods, content_type='application/json')
