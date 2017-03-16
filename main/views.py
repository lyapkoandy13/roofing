from django.http import HttpResponse
from django.shortcuts import render
from main.models import Good
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


def index(request):
	goods = Good.objects.all()
	return render(request, 'main/index.html', { 'goods' : goods } )

def ajax_get_goods(request):
	try:
		some_filter = request.POST.get("filter")
		if (some_filter is None) or (some_filter == "default"):
			goods = Good.objects.all()
		elif some_filter == "price_asc":
			goods = Good.objects.order_by('price')
		elif some_filter == "price_desc":
			goods = Good.objects.order_by('-price')
		elif some_filter == "name_asc":
			goods = Good.objects.order_by('name')
		elif some_filter == "name_desc":
			goods = Good.objects.order_by('-name')
		else:
			goods = Good.objects.filter(name__contains=some_filter)
		paginator = Paginator(goods, 10)
		goods = paginator.page(int(request.POST.get("page")))
		some_i = 1
		html = ""

		for good in goods:
			if (some_i % 3) == 1 or some_i == 1:
				html += "<div class=\"row\">"
			

			html += ("<div class=\"col-sm-4 item\">"
					+	"<div class=\"panel\">"
						
						+	"<div class=\"row good-image\">"
						+		"<img src=\""+"media/"+str(good.image)+"\" id=\"good-image\" alt=\"Черепиця\">"
						+	"</div>"

						+	"<div class=\"row good-name\">"
						+		"<h3>"+good.name+"</h3>"
						+	"</div>"
						
						+	"<div class=\"row good-description\">"
						+		"<span>"+good.description+"</span>"
						+	"</div>"

						+	"<div class=\"row good-price\">"
						+		"<h4>Ціна: "+str(good.price)+"€</h4>"
						+	"</div>"
			
					+	"</div>"
					
				+"</div>")
			
			if (some_i % 3) == 0:
				html += "</div>"

			some_i = some_i + 1
	except Exception:
		return HttpResponse("no")

	return HttpResponse(html)
