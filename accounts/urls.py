from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('blog/', views.blogs),
    path('blog-details/', views.blog_details),
    path('contact/', views.contact),
    path('checkout/', views.checkout),
    path('about-us/', views.about),
    path('product-details/', views.product_details),
    path('terms/', views.terms),
]
