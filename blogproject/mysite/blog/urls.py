from importlib.resources import path
from unicodedata import name
from django.conf.urls import url
from django.urls import URLPattern
from blog import views

URLPatterns=[
    path('',views.PostListView.as_view(),name='post_List'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view,name='post_new'),
    path('post/(?p<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post-edit'),
    path('post/(?p<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post-remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/(?p<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/(?p<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    path('comment/(?p<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    path('post/(?p<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]