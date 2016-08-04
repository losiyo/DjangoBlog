def archives(request):
	try:
		post_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'post_list': post_list, 'error': False})

def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag):
	try:
		post_list = Article.objects.filter(category__iexact = tag)
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'tag.html', {'post_list': post_list})