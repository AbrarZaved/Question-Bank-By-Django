from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("index", views.index, name="index"),
    path("contribute", views.contribute, name="contribute"),
    path("leaderboard", views.leaderboard_view, name="leaderboard"),
    path("site_rules", views.site_rules, name="site_rules"),
    path("get_departments", csrf_exempt(views.get_departments), name="get_departments"),
    path("upload_questions", csrf_exempt(views.upload_questions), name="upload_questions"),
    path(
        "question_results", csrf_exempt(views.question_results), name="question_results"
    ),
    path(
        "attributeSetup", csrf_exempt(views.attributeSetup), name="attributeSetup"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
