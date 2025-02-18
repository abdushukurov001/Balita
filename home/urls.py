from django.urls import path
from .views import home_view, postDetail_view


urlpatterns = [
    path("", home_view, name="home"),
    path("post/<int:id>/", postDetail_view, name='post-detail')
]