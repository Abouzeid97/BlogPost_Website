from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView
from .models import Post
from .form import PostForm, CommentForm
from datetime import date
from django.utils.text import slugify

# Create your views here.

class indexView(ListView):
    template_name = "blogpost/index.html"
    model = Post
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-time_posted')[:3]
        return context

class InputView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blogpost/input.html"
    success_url = "/all_posts"


    def form_valid(self, form):
        form.instance.time_posted = date.today()
        title = form.cleaned_data['title']
        form.instance.slug = slugify(title)
        return super().form_valid(form)
    
    
class all_postView(ListView):
    template_name = "blogpost/all_posts.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-time_posted')
        context['Num_of_Posts'] = Post.objects.all().__len__()
        return context
    

class post_detailView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
    
        
        context = {
            "post": post,
            "comment_form" : CommentForm(),
            "saved_for_later": self.is_stored_post(request, post.id)

        }
        return render(request, "blogpost/post_detail.html", context)

    def post(self, request, slug):
       
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))
        else:
            
            context = {
                "post": post,
                "comment_form" : CommentForm(),
                "saved_for_later": self.is_stored_post(request, post.id)
            }
            return render(request, "blogpost/post_detail.html", context)

class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blogpost/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_posts:
          stored_posts.append(post_id)
          request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
