from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    # 최신글 맨위에 올리는 법
    posts = Post.objects.all().order_by('-pk')

    # 데이터베이스에 쿼리를 날려 원하는 레코드 가져옴
    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )