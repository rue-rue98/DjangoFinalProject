from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTopicForm, PostForm
from .models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    query = request.GET.get('q', '').strip()
    topics = board.topics.order_by('-last_updated')
    if query:
        topics = topics.filter(subject__icontains=query)

    paginator = Paginator(topics, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'boards/topics.html',
        {'board': board, 'page_obj': page_obj, 'query': query},
    )


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = Topic.objects.create(
                subject=form.cleaned_data['subject'],
                board=board,
                created_by=request.user,
            )
            Post.objects.create(
                message=form.cleaned_data['message'],
                topic=topic,
                created_by=request.user,
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    posts = topic.posts.order_by('created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'boards/topic_posts.html',
        {'topic': topic, 'page_obj': page_obj},
    )


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                message=form.cleaned_data['message'],
                topic=topic,
                created_by=request.user,
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'boards/reply_topic.html', {'topic': topic, 'form': form})


@login_required
def edit_post(request, pk, topic_pk, post_pk):
    post = get_object_or_404(Post, pk=post_pk, topic__pk=topic_pk, topic__board__pk=pk)
    if post.created_by != request.user:
        return redirect('topic_posts', pk=pk, topic_pk=topic_pk)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.message = form.cleaned_data['message']
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm(initial={'message': post.message})
    return render(request, 'boards/edit_post.html', {'topic': post.topic, 'post': post, 'form': form})