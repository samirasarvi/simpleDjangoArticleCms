from django.urls import path
from .views import article_detail, home
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"
urlpatterns= [
    path('',home, name = "home"),
    path('article/<slug:slug>/',article_detail, name = "article_detail"),

   
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
