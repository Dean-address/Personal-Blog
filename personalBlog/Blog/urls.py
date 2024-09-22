from django.urls import path
from . import views
app_name='blog'
urlpatterns =[
	path('', views.index, name='index'),
	path('article/<int:blog_id>', views.article, name='article'),
	path('blog_admin', views.admin, name='admin'),
	path('confirm_delete/<int:blog_id>', views.delete, name='delete'),
	path('edit/<int:blog_id>', views.edit, name='edit'),
 	path('new', views.new, name='new')
]