from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
      path('', views.register, name='register'),  # Map the root URL to the register view
    path('stage2/', views.stage2, name='stage2'),  # Map /stage2/ to the stage2 view
    path('success/', views.success, name='success'),  # Map /success/ to the success view
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
