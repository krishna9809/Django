from django.contrib import admin
from django.urls import path
from cool.views import *

urlpatterns = [

    path('', home),
    path('swag/',swag),
    path('swag/me/',swagme),
    path('swag/me/and/you/',swagmeandyou),
    path('admin/', admin.site.urls),
]
