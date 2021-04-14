from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, CategoryForm, AddPostForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
# def home(request):
#   return render(request, 'home.html', {})
# we gonna use class based views !!!!


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]
    # ordering = ["-id"]
    # ordering the viewing order i guess default is "id"
    # id field was created auto by django

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()        
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu        
        return context
        # bu fonksiyon class based view a html e göndermelik bilgi ekledik


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, "categories.html", {"cat_menu_list": cat_menu_list})


class PostView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = 'published'
    # context object name html templatede kullanacağımız objenin ismini belirliyor

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        like_object = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_object.total_likes()
        liked = False
        if like_object.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))


def CategoryView(request, cats):
    # cats is coming from <str:cats>
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.replace('-', ' '), 'cat_posts': category_posts})


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = "addpost.html"
    # fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "editpost.html"
    # fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy("home")


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "addcategory.html"
    # fields = "__all__"

def SearchView(request):
    if request.method == "POST":
        search_key = request.POST["search_key"]
        search_result = Post.objects.filter(Q(body__contains=search_key) | Q(title__contains=search_key))
        # i combined two query!!!
        print(request.POST, type(search_result))

        return render(request, 'search.html', {'search_result' : search_result, 'search_key' : search_key})
    else:
        return render(request, 'search.html', {})
