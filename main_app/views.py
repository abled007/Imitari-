from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ImageForm
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirm.html"
    success_url = "/posts"

def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums_index.html', {'albums': albums})

def albums_show(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'album_show.html', {'album': album})

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    template_name = "album_form.html"
    success_url = '/albums'

def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'posts': posts})

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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/posts') 

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