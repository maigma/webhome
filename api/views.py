from django.shortcuts import render

# Create your views here.

def apina(request):
	
    template = "api/api-view.html"
    context = {}
    return render(request, template, context)
