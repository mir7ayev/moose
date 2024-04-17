from django.urls import path
from .views import (
    home_view, blog_view, about_view,
    blog_single_view,
)

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('blog-single/<int:pk>/', blog_single_view),
    path('about/', about_view),
]
