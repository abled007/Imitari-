from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class PostList(TemplateView):
    template_name = 'postlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all() # Here we are using the model to query the database for us.
        return context