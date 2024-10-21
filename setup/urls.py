from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefa.urls')),
    path('tempo_trabalho/', include('tempo_trabalho.urls')),
]
