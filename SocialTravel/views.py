from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from SocialTravel.models import Post,Profile
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request,"SocialTravel/index.html",context)

class PostList(ListView):
    model = Post
    #Post.objects.all() se utiliza la query para buscar lista   

class PostDetail(DetailView):
    model = Post
    #Post.objects.get(id=pk)

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__' #o si quiere usarse algunos campos , se usa lista con los nombres de los campos 
    # ['carousel_caption_tittle','carousel_caption_description']

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request,"SocialTravel/not_found.html")

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request,"SocialTravel/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')

class Login(LoginView):
    next_page = reverse_lazy("post-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'
    

