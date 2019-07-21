from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment
from .forms import NewBlog, CommentForm


#처음 실행화면
def welcome(request):
    return render(request, 'index.html')

#지금까지 쓴 글 읽기
def read(request):
    blogs = Blog.objects.all()
    return render(request, 'crud.html', {'blogs':blogs})

#글쓰기
def create(request):
    # 입력받은 값을 저장해주는 과정
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 페이지를 로드해주는 과정
    else:
        form = NewBlog()
        return render(request, 'new.html', {'form':form})

def update(request,pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk=pk)

    # 해당하는 블로그 객체 pk에 맞는 입력공간을 가져오기
    form = NewBlog(request.POST, instance=blog)

    if request.method == "POST":
        if form.is_valid(): #폼 검증 메소드
            post = form.save(commit = False)
            post.update_date=timezone.now()
            post.save()
            return redirect('home') #url의 name
        else:
            form = NewBlog(instance=blog) # forms.py의 NewBlog 클래스의 인스턴트
            return render(request, 'new.html', {'form' : form})

    return render(request, 'new.html', {'form':form})

def delete(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, board_id):
    board_detail = get_object_or_404(Blog, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id)
    return render(request, 'detail.html', {'board':board_detail})

# 댓글
def comment_write(request, pk):

    if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.board = Blog.objects.get(pk=pk)
                    comment.created_at = timezone.now()
                    comment.save()
                    return redirect('detail', pk)
    else:
            comment_form = CommentForm()
    return render(request, 'comment_form.html', {'comment_form' : comment_form})
    
def comment_edit(request, board_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)

            if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.board = Blog.objects.get(pk=board_pk)
                    comment.save()
                    return redirect('detail', board_pk)

    else:
            comment_form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'comment_form' : comment_form}) 