from django.http.response import HttpResponse
from django.shortcuts import render
from blog import models
from blog.models import Category, Blog

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Django Kursu",
            "img": "1.jpg",
            "is_active": True,
            "is_home": True,
            "description": "cok iyi bir kurs"
        },
        {
            "id": 2,
            "title": "Python",
            "img": "2.png",
            "is_active": True,
            "is_home": False,
            "description": "cok iyi bir kurs"
        },
        {
            "id": 3,
            "title": "Darth Vader",
            "img": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "cok iyi bir kurs"
        }
    ]
}


# Create your views here.

def index(request):
    context = {
        "blogs": models.Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": models.Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    blog = models.Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })


def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        # "blogs": models.Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)
