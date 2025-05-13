from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),  # добавляем URL'ы контактного API
    path('api/', include('project.urls'))
]
