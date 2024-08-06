from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('details/<pk>',views.products_Details,name='details'),

    path('images',views.products, name='images'),
    path('dash',views.dashboard_view, name='dash'),
    path('post',views.post_image, name='post'),
    path('category',views.category_post, name='category'),
    path('edit/<pk>',views.edit_item,name='edit'),
    path('about/<pk>',views.images_Details,name='about'),
    path('delete/<pk>',views.delete_item,name='delete'),

    path('login',views.login_view,name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('signup',views.signup_view,name='signup')
]