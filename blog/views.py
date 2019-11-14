from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def homepage_view(request):
	return render(request, 'blog/index.html', {})

def contact_view(request):
	return render(request, 'blog/contact.html', {})
