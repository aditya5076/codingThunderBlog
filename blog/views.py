from django.shortcuts import render
from blog.models import Blog, Contact
import math

# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    # conditions for pagination accord to no post
    no_of_posts = 5
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    '''logic to build the page accorfinh to n. post:
    page1:1-3
    page2:3-6
    page3:6-9
    
    in words
    page1:0-0 to no.ofposts
    page2:no.ofposts to no.ofposts+no.ofposts
    page3:no.ofposts+no.ofposts to no.ofposts+no.ofposts+no.ofposts
    
    i.e
    (page-1)*noofpost to page*noofpost
    '''
    # this is uused to g-fetch all the blogs from Blog class in db
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page - 1) * no_of_posts: page * no_of_posts]
    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length / no_of_posts):
        nxt = page_1
    else:
        nxt = None

    # context is used t display the db's elements in webpage
    context = {'blogs': blogs, prev: 'prev', nxt: 'nxt'}
    return render(request, 'blog.html', context)


def blogpost(request, slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context = {'blogs': blogs}
    return render(request, 'blogpost.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        instance = Contact(name=name, email=email,
                           number=phone, message=message)
        instance.save()

    return render(request, 'contact.html')
