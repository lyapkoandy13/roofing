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
		html = ""

		for good in goods:
			html += ("<div class=\"item\">"
				
					+ "<div class=\"col-sm-6\">"
					+	"<div class=\"row\">"
					+		"<img src=\""+"media/"+str(good.image)+"\" id=\"good-image\" alt=\"Черепиця\">"
					+	"</div>"
					+	"<div class=\"row\">"
					+		"<span class=\"good-price\">Ціна: "+str(good.price)+"</span>"
					+	"</div>"

					+ "</div>"

					+ "<div class=\"col-sm-6\">"
					+	"<div class=\"row\">"
					+		"<span class=\"good-name\">"+good.name+"</span>"
					+	"</div>"
					+	"<div class=\"row\">"
					+		"<span class=\"good-description\">"+good.description+"</span>"
					+	"</div>"
					+ "</div>"
			
				+"</div>")
	except Exception:
		return HttpResponse("no")

	return HttpResponse(html)
