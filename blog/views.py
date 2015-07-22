# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse
from django.conf import settings

def index(request):
	uid = request.session.get('user')

	if uid is None:
		return HttpResponse("You are not our member yet, please log in first!")
	else:
		all_posts = Post.objects.all()
		paginator = Paginator(all_posts, 5)
		page = request.GET.get('page')

		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		return render(request, 'blog/blog_index.html', {'posts': posts, 
			'swiftype_engine_key': settings.SWIFTYPE_ENGINE_KEY})

def post(request, slug):
	uid = request.session.get('user')

	if uid is None:
		return HttpResponse("you are not our member yet, please log in first!")
	else:
		post = get_object_or_404(Post, slug=slug)
		return render(request, 'blog/post.html', {'post': post})


###Authentication for reference:
#def index(request):
#	uid = request.session.get('user')

#	if uid is None:
#		return render_to_response('index.html')
#	else:
#		return render_to_response(
#				'user.html',
#				{'user': User.objects.get(pk=uid)}
#			)