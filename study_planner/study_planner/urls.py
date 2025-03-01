from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('notes/', include('notes.urls')),
    path('homework/', include('homework.urls')),
    path('todo/', include('todo.urls')),
    path('resources/', include('resources.urls')),
    path('users/', include('users.urls')),
     path('dashboard/', include('dashboard.urls'), name='dashboard'),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
