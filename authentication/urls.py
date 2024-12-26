from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.sign_in,name='sign_in'),
    path('register',views.register,name='register')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
