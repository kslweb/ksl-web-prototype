from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, render, HttpResponseRedirect
from .models import Post, AboutUs, ContactUs

def redirect(request):
    return HttpResponseRedirect('/blog/')

def tagpage(request, tag):
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response('tag.html', {'posts':posts, 'tags':tag})

def detail_artikel(request, id_artikel):
	detail = Post.objects.get(id=int(id_artikel))
	return render_to_response('detail.html', {'detail':detail})

def about_us(request):
	aboutus = AboutUs.objects.get(id=1)
	return render_to_response('aboutus.html', {'aboutus':aboutus})

def contact_us(request):
    contactus = ContactUs.objects.get(id=1)
    return render_to_response('contactus.html', {'contactus':contactus})

def listing(request):
    post_list = Post.objects.published().order_by('-created')
    paginator = Paginator(post_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'pages': pages})

def search(request):
    query = request.GET.get('s')
    if query:
        results = Post.objects.filter(title__contains=query)
    else:
        return HttpResponseRedirect('/blog/')
    return render_to_response('search.html', {'results':results})

def author(request):
    author = request.user
    return render_to_response('search.html', {'author':author})