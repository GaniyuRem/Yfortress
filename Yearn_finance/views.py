from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from Yearn_finance.models import Contact
from django.views.decorators.csrf import csrf_exempt

# from django.
# from django.contrib import

# Create your views here.


def index(request):
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({"result": "success", "message": "We have <Strong> successfully </Strong> received your message. We'll get back to you soon."})
    else:
        return render(request, 'index.html')
