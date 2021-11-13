from django.urls import path
from cms_app import views


app_name="cms_app"

urlpatterns = [
    path('', views.about, name='about'),
    path('about-detail/<int:abt_id>/', views.about_detail, name='ekene_detail'),
    path('service-page/', views.service, name='service'),
    path('posts/', views.post_list, name='post_list'),
    path('single-post/<int:post_id>/', views.single_post, name='single_post'),
    path('post-from-cat/<int:cat_id>/', views.post_from_cat, name='post_from_cat'),
    path('contact-page/', views.contact, name='contact'),
]