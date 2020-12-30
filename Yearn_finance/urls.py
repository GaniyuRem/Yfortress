from django.contrib import admin
from django.urls import path
from django.urls import include
from Yearn_finance import views
urlpatterns = [
<<<<<<< HEAD
    # path('', views.index, name="index"),
=======
    path('', views.index, name="index"),
>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557
    # path('admin/', admin.site.urls),

]
