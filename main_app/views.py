from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.edit import CreateView
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    template_name = "post_create.html"
    success_url = "/posts"

class PostList(TemplateView):
    template_name = 'postlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["posts"] = Post.objects.filter(title__icontains=title)
        else:
            context["posts"] = Post.objects.all()
        return context