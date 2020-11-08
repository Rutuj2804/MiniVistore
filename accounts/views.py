from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def blogs(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about-us.html')


def product_details(request):
    return render(request, 'product-details.html')


def terms(request):
    return render(request, 'terms.html')


def testimonials(request):
    return render(request, 'testimonials.html')
