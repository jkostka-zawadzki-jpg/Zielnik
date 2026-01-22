from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import models
from .models import Post, TeaProduct
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)

def landing(request):
    return render(request, 'Blog/landing.html')

def shop(request):

    query = (request.GET.get('q') or '').strip().lower()
    category = (request.GET.get('category') or '').strip()
    benefit = (request.GET.get('benefit') or '').strip()
    caffeine = (request.GET.get('caffeine') or '').strip()
    max_price = (request.GET.get('max_price') or '').strip()

    filtered = TeaProduct.objects.all()
    if query:
        filtered = filtered.filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )
    if category:
        filtered = filtered.filter(category=category)
    if benefit:
        filtered = filtered.filter(benefits__icontains=benefit)
    if caffeine == 'free':
        filtered = filtered.filter(caffeine_free=True)
    elif caffeine == 'contains':
        filtered = filtered.filter(caffeine_free=False)
    if max_price:
        try:
            price_limit = float(max_price.replace(',', '.'))
        except ValueError:
            price_limit = None
        if price_limit is not None:
            filtered = filtered.filter(price__lte=price_limit)

    categories = list(TeaProduct.objects.values_list('category', flat=True).distinct())
    categories.sort()
    benefits = sorted({
        b.strip()
        for p in TeaProduct.objects.values_list('benefits', flat=True)
        for b in p.split(',')
        if b.strip()
    })

    context = {
        'products': filtered,
        'categories': categories,
        'benefits': benefits,
        'filters': {
            'q': query,
            'category': category,
            'benefit': benefit,
            'caffeine': caffeine,
            'max_price': max_price,
        },
    }
    return render(request, 'Blog/shop.html', context)

def tea_detail(request, pk):
    product = get_object_or_404(TeaProduct, pk=pk)
    return render(request, 'Blog/tea_detail.html', {'product': product})

def search(request):
    query = (request.GET.get('q') or '').strip()
    scope = (request.GET.get('scope') or 'user').strip()
    if not query:
        return redirect('site-home')
    if scope == 'shop':
        matches = TeaProduct.objects.filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )
        if not matches.exists():
            return render(
                request,
                'Blog/search_no_results.html',
                {'query': query, 'scope': 'shop'},
            )
        return redirect(f"/shop/?q={query}")
    if not User.objects.filter(username=query).exists():
        return render(
            request,
            'Blog/search_no_results.html',
            {'query': query, 'scope': 'user'},
        )
    return redirect('user-posts', username=query)

class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']  
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']  
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DeleteView):
    model = Post
    template_name = 'Blog/post_detail.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'Blog/about.html', {'title': 'O Nas'})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'Blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
