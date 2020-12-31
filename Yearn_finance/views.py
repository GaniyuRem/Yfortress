from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from Yearn_finance.models import Contact
from django.views.decorators.csrf import csrf_exempt

# from django.
# from django.contrib import

# Create your views here.


def homepage(request):
    if request.method == "POST":
        print(request.POST)
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message_box")
        Contact.objects.create(
            full_name=full_name, email=email, message=message).save()
        return JsonResponse({"result": "success", "message": "We have <Strong> successfully </Strong> received your message. We'll get back to you soon."})

    return render(request, 'homepage.html')
