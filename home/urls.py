from django.urls import path
from .views import home_view, postDetail_view, category_view


urlpatterns = [
    path("", home_view, name="home"),
    path("post/<int:post_id>/", postDetail_view, name='post-detail'),
    path("category/<int:id>/", category_view, name='category'),
 

]