from django.urls import path

from main_app.views import IndexPageView


urlpatterns = [path("index/", IndexPageView.as_view(), name="index")]
