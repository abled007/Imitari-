from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView
from .forms import ImageForm
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    template_name = "post_update.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    template_name = "post_create.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})  

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'post_create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'post_create.html', {'form': form})

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