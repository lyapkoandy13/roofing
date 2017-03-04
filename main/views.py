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
		goods = Good.objects.all()
		paginator = Paginator(goods, 10)
		goods = paginator.page(int(request.POST.get("page")))
		some_i = 1
		html = ""

		for good in goods:
			if (some_i % 2) == 1:
				html += "<div class=\"row\">"
			

			html += ("<div class=\"col-sm-6 item\">"
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
						+		"<h4>Ціна: "+str(good.price)+"</h4>"
						+	"</div>"
			
					+	"</div>"
					
				+"</div>")
			
			if (some_i % 2) == 0:
				html += "</div>"

			some_i = some_i + 1
	except Exception:
		return HttpResponse("no")

	return HttpResponse(html)
