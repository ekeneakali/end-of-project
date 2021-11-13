import email
from django.shortcuts import render
from django.http import HttpResponse
from cms_app.models import *
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
    latest_post = Post.objects.order_by('-created_at')[:3]
    return render(request, 'cms_app/index.html', {'latest':latest_post})

def about(request):
    team = Team.objects.all()
    return render(request, 'cms_app/about.html', {'team':team})

def about_detail(request, abt_id):
    team_detail = Team.objects.get(id=abt_id)
    return render(request, 'cms_app/detail.html', {'detail':team_detail})

def post_list(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'cms_app/post-list.html', {'show_post':post})

def single_post(request, post_id):
    single = Post.objects.get(id=post_id)
    get_comment = Comment.objects.filter(post__id=post_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, comment=comment, post=single)
        messages.success(request, 'Comment created')
    return render(request, 'cms_app/single-blog.html', {'single':single, 'comment':get_comment})

def post_from_cat(request, cat_id):
    count = Post.objects.filter(category__id=cat_id).count()
    single = Category.objects.get(id=cat_id)
    post_cat = Post.objects.filter(category__id=cat_id)
    return render(request, 'cms_app/post-cat.html', {'post':post_cat, 'count':count, 'single':single})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        referer = request.POST.get('referer')
        message = request.POST.get('message')
        subject = 'From CMS APP'
        context = {
            'name':name,
            'phone':phone,
            'email':email,
            'referer':referer,
            'message':message,
        }
        html_message = render_to_string('cms_app/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <slimchibenedict@gmail.com>'
        mail.send_mail(subject, plain_message, from_email, ['nonwaz78@gmail.com', ], html_message=html_message)
        messages.success(request, 'Mail Sent')
    return render(request, 'cms_app/contact.html')

def service(request):
    return render(request, 'cms_app/services.html')