from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def health(request):
    return HttpResponse('Ok', status=200)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('rooms/', include('rooms.urls')),
    path('health/', health),
]
