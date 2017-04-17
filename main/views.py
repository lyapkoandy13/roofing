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
			goods = Good.objects.filter(name__icontains=some_filter.lower())
		paginator = Paginator(goods, 15)
		goods = paginator.page(int(request.POST.get("page")))
		some_i = 1
		html = ""

		for good in goods:
			if (some_i % 3) == 1 or some_i == 1:
				html += "<div class=\"row\">"
			

			html += ("<div id=\""+ str(good.id) +"\" class=\"col-sm-6 col-md-4 item\">"
					+	"<div class=\"panel\">"
						
						+	"<div class=\"row good-image\">"
						+		"<img src=\"media/"+str(good.images.all()[0].image)+"\" id=\"good-image\" alt=\"Черепиця\">"
						+	"</div>"

						+	"<div class=\"row good-name\">"
						+		"<h3>"+good.name+"</h3>"
						+	"</div>"
						
						+	"<div style=\"display: none;\" class=\"row good-description\">"
						+		"<p>"+good.description+"</p>"
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

def ajax_get_images(request):
	if request.method == "POST":
		some_id = request.POST.get('some_id')
		good = Good.objects.filter(id=some_id)
		images = good[0].images.all()
		some_obj = list()
		for image in images:
			some_obj.append(str(image.image))
		import json
		return HttpResponse(json.dumps(some_obj), content_type="application/json")
	else:
		return HttpResponse('no')

