from django.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.blog_index, name='blog_index'),
    url(r'blog/home/$', views.blog_home, name='blog_home'),
    url(r'blog/post/$', views.notice_list, name='notice_list'),
    url(r'blog/post/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'blog/login/$', auth_views.LoginView.as_view(), name='blog_login'),
    url(r'blog/logout/$', auth_views.LogoutView.as_view(), name='blog_logout'),
    url(r'blog/login/register/$', views.registerPage, name='blog_reg'),
    url(r'blog/board/$', views.board_list, name='board_list'),
    url(r'blog/board/write/$', views.board_write, name='board_write'),
    url(r'blog/board/(?P<pk>[0-9]+)/$', views.board_detail, name='board_detail'),
]