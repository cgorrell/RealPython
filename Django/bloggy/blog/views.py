# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index.html')
	context_dict = {'latest_posts': latest_posts, 'popular_posts':popular_posts,}
	for post in latest_posts:
		post.url = post.title.replace(' ', '_')
	for popular_post in popular_posts:
		popular_post.url = popular_post.title.replace(' ', '_')
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_name):
	single_post = get_object_or_404(Post, title=post_name.replace('_', ' '))
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post})
	return HttpResponse(t.render(c))

def encode_url(url):
	return url.replace(' ', '_')

def add_posts(request):
	context = RequestContext(request)
	if request.method == 'Post':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect(index)
		else:
			print form.errors
	else:
		form = PostForm()
	return render_to_response('blog/add_posts.html', {'form': form}, context)