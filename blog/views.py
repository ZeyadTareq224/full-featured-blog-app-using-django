from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Post, Comment
from .forms import PostForm, CommentForm



def blog_home(request):
	posts = Post.objects.all()

	paginator = Paginator(posts, 3)
	page = request.GET.get('page')
	try:
		posts_per_page = paginator.page(page)
	except PageNotAnInteger:
		posts_per_page = paginator.page(1)
	except EmptyPage:
		posts_per_page = paginator.page(paginator.num_pages)

	context = {'posts': posts_per_page, 'page': page}
	return render(request, 'blog/home.html', context)


def post_details(request, pk):
	post = Post.objects.get(id=pk)
	user = request.user
	tags = post.tag.all()
	comments = post.comment_set.all()
	no_of_comments = comments.count()
	new_comment = None
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.post = post
			new_comment.user = user
			new_comment.save()
			return redirect('blog-home')


	context = {
	'post': post,
	'tags': tags,
	'form': form,
	'comments': comments,
	'no_of_comments': no_of_comments,
	'user': user
	}

	return render(request, 'blog/post_details.html', context)

@login_required(login_url='login-page')
def create_post(request):
	user = request.user
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.user = user
			form.save()
		return redirect('blog-home')	
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)

@login_required(login_url='login-page')
def update_post(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('blog-home')		
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)

@login_required(login_url='login-page')
def delete_post(request, pk):
	post = Post.objects.get(id=pk)
	if request.method =="POST":
		post.delete()
		return redirect('blog-home')
	context = {'post': post}
	return render(request, 'blog/delete_form.html', context)

@login_required(login_url='login-page')
def dashboard(request):
	user = request.user
	posts = user.post_set.all()
	no_of_posts = posts.count()

	context = {'posts': posts, 'no_of_posts': no_of_posts}
	return render(request, 'blog/dashboard.html', context)