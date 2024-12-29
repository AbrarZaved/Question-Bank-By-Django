from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.sign_in, name="sign_in"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("profile", views.profile, name="profile"),
    path("register", csrf_exempt(views.register), name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
