from django.shortcuts import render
from django.template import loader
from .models import Article
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    all_blogs = Article.objects.all()
    paginator = Paginator(all_blogs, 3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
		"all_blogs":page_obj
	}
    
    return render(request, 'blog/index.html', context)

def article(request, blog_id):
    blog = Article.objects.get(pk=blog_id)
    context = {
		'blog':blog
	}
    return render(request, 'blog/article.html', context)
 
def admin(request):
    all_blogs = Article.objects.all()
    context = {
		"all_blogs":all_blogs
	}
 
    return render(request, 'blog/admin.html', context)


def new(request):
    
    new_title = request.POST.get('title')
    new_pub_date = request.POST.get('datetime')
    new_content = request.POST.get('content')
    try:
        new_blog = Article(article_title=new_title,pub_date=parse_datetime(new_pub_date), article_content=new_content)
        new_blog.save()     
    except:
        return render(request, 
                      'blog/new.html',
                      {
                          
            'error_message':'Form not submitted'
            })
    else:
        return HttpResponseRedirect(reverse('blog:index'))
    
    
def edit(request,blog_id):
    blog = Article.objects.get(pk=blog_id)
    context = {
		'blog':blog
	}
    if request.method == 'POST':
        article_title = request.POST.get('title')
        pub_date_str = request.POST.get('datetime')
        article_content = request.POST.get('content')
        
        if not article_title:
            return render(request, 'blog:edit.html', {
				'blog':blog,
                 'error_message': 'Title is required'
			})
        pub_date = parse_datetime(pub_date_str) if pub_date_str else None
        blog.article_title = article_title
        blog.pub_date = pub_date
        blog.article_content = article_content
        blog.save()
        
        return HttpResponseRedirect(reverse('blog:admin'))
            
        
    return render(request, 'blog/edit.html', context)

    

def delete(request, blog_id):
    blog = Article.objects.get(pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return HttpResponseRedirect(reverse('blog:admin'))
    context={
		'blog':blog
	}
    return render(request, 'blog/confirm_delete.html', context)
          