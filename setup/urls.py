from django.contrib import admin
from django.urls import path
from tarefa import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_tarefa, name='home'),
]
