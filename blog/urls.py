from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# http://127.0.0.1:8000/ => Hom page
# http://127.0.0.1:8000/index => Hom page
# http://127.0.0.1:8000/blogs => blogs
# http://127.0.0.1:8000/blogs/3 => blog-details


urlpatterns = [
    path("", views.index, name="Home"),
    path("index", views.index),
    path("blogs", views.blogs, name="Blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="Blog_Details")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
