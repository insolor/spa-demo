from django.shortcuts import render
from django.views import View

from myblog_app.models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'myblog_app/home.html', context={
            'posts': posts
        })
