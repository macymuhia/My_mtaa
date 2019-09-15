from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login/profile/", views.profile, name="profile"),
    path("login/profile/edit/", views.edit_profile, name="edit_profile"),
    path("search/", views.search_results, name="search_results"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
