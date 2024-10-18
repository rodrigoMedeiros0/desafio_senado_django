from django.contrib import admin
from django.urls import path
from tarefa import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefa.urls')),
]
